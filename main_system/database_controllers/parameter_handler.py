
from main_system.custom_classes.status_control import StatusControl
from collections import defaultdict
from django.db import connection

TEMPORAL_PARAMETERS = defaultdict(dict)

"""
    This function verifies if the parameters sent in the request are valid for the object
    object_name: The name of the object that is going to be checked
    parameterListIn: The parameters that are going to be checked
    object_type: The type of the object that is going to be checked (e.g. 'f' -> 'function', 'p' -> 'procedure')
    paginated: A boolean that indicates if the object is paginated

    Returns a StatusControl object with the result of the verification
"""

def get_valid_parameter_list(object_name: str, parameterListIn: dict, object_type: str, paginated: bool = False):
    status = StatusControl(0, 'Initial status', None)
    try:
        parametersToCheck = prepare_parameter_list(parameterListIn, paginated)

        parameterListDb = get_parameters_from_temp(object_name)
        if not parameterListDb:
            parameterListDb = get_parameter_list_from_database(object_name, object_type)
            if parameterListDb == 'Inexistent':
                status.error_message('The object \'' + object_name +'\' (' + object_type + ') does not exist.')
                return status

        # if it is a procedure then the out parameters from db are add to the parameters to check with a None value
        if object_type == 'p':
            for parameter in parameterListDb:
                if parameter[4] == 'OUT':
                    parametersToCheck[parameter[2]] = None
        # if it is a function then the out parameters from db are not necessary
        elif object_type == 'f':
            parameterListDb = [parameter for parameter in parameterListDb if parameter[2] != 'OUT']

        unnecesaryParameters = [
            key + ' (' + type(parametersToCheck[key]).__name__ + ')' 
            for key in parametersToCheck 
            if key not in [item[2] for item in parameterListDb]
        ]

        missingParameters = [
            item[2] + ' (' + item[3] + ')'
            for item in parameterListDb
            if item[2] not in parametersToCheck
        ]

        if unnecesaryParameters and missingParameters:
            status.error_message(
                'The parameters ' + unnecesaryParameters.__str__() + ' are not necessary. '
                'Also, the parameters ' + missingParameters.__str__() + ' are missing.'
            )

        elif unnecesaryParameters:
            status.error_message('The parameters ' + unnecesaryParameters.__str__() + ' are not necessary.')

        elif missingParameters:
            status.error_message('The parameters ' + missingParameters.__str__() + ' are missing.')

        else:
            preparedParameters = prepare_parameter_list_for_db(parameterListDb, parametersToCheck)
            status.ok_body(preparedParameters)
    except Exception as e:
        status.error_message(str(e))

    return status

"""
    This function prepares the parameters to be sent to the database as a tuple
    parameterListDb: The parameters that are going to be sent to the database
    parametersToCheck: The parameters that are going to be checked

    Returns a list with the parameters prepared to be sent to the database
"""

def prepare_parameter_list_for_db(parameterListDb: list, parametersToCheck: dict):
    preparedParameters = tuple()
    for parameter in parameterListDb:
        key = parameter[2]
        value = parametersToCheck[key]
        preparedParameters += (value,)
    return preparedParameters

"""
    This function prepares the parameters to be checked
    parameterListIn: The parameters that are going to be checked

    Returns a list with the parameters prepared to be checked
"""

def prepare_parameter_list(parameterListIn: dict, paginated: bool):
    parameterList = []
    isRequest = type(parameterListIn).__name__ == 'Request'
    if isRequest:
        if parameterListIn.query_params:
            parameterList = parameterListIn.query_params.dict()
        else:
            parameterList = parameterListIn.data
    else:
        parameterList = parameterListIn

    if paginated:
        if parameterList.get('p_offset',None) is None:
            raise Exception('The parameter offset is missing')
        elif parameterList.get('p_limit',None) is None:
            raise Exception('The parameter limit is missing')
    
    return parameterList

"""
    This function adds a parameter to the TEMPORAL_PARAMETERS dictionary
    parameter: The parameter that is going to be added
"""

def add_parameter_to_temp(parameter: tuple):
    key = (parameter[0], parameter[2])
    TEMPORAL_PARAMETERS[key] = parameter

def get_parameters_from_temp(object_name: str):
    filtered_elements = [value for key, value in TEMPORAL_PARAMETERS.items() if key[0] == object_name]
    return filtered_elements

def get_parameter_list_from_database(object_name: str, object_type: str):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM core_func_get_parameters(%s, %s)", (object_name, object_type))
        parameterList = cursor.fetchall()
        for parameter in parameterList:
            if parameter[0] == 'Inexistent':
                return parameter[0]
            newParameter = (object_name, object_type, parameter[0], parameter[1], parameter[2])
            add_parameter_to_temp(newParameter)
    return get_parameters_from_temp(object_name)