
from main_system.database_controllers.parameter_handler import get_valid_parameter_list
from main_system.custom_classes.status_control import StatusControl
from django.db import connection

"""
    This function executes a function in the database
    name: The name of the function to execute
    parameters: The parameters of the function to execute
    paginated: If the result should be paginated (defining the limit and offset)

    Returns a StatusControl object with the result of the execution
"""

def sql_exec_function(name: str, parameters: dict, paginated: bool = False)-> StatusControl:
    status = get_valid_parameter_list(name, parameters, 'f', paginated)
    if status.statusCode == 200:
        try:
            preparedParameters = status.body
            placeholders = ', '.join(['%s'] * len(preparedParameters))
            query = f"SELECT * FROM {name}({placeholders})"
            with connection.cursor() as cursor:
                cursor.execute(query, preparedParameters)
                result = cursor.fetchall()
            status.ok_body(result)
        except Exception as e:
            status.error_message(str(e))
    return status
