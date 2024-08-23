
from main_system.database_controllers.parameter_handler import get_valid_parameter_list
from django.db import connection

"""
    This function executes a procedure in the database
    name: The name of the procedure to execute
    parameters: The parameters of the procedure to execute

    Returns a StatusControl object with the result of the execution
"""

def sql_exec_procedure(name: str, parameters: dict):
    status = get_valid_parameter_list(name, parameters, 'p')
    if status.statusCode == 200:
        try:
            preparedParameters = status.body
            placeholders = ', '.join(['%s'] * len(preparedParameters))
            query = f"CALL {name}({placeholders})"
            with connection.cursor() as cursor:
                cursor.execute(query, preparedParameters)
                result = cursor.fetchone()
            status.ok_body(result)
        except Exception as e:
            status.error_message(str(e))
    return status
