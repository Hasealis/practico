from rest_framework.response import Response
from rest_framework import status
from main_system.custom_classes.status_control import StatusControl

def responseFromStatusControl(statusControl : StatusControl):
    """
        Genera una respuesta HTTP con la información de error o éxito contenida en un objeto ControlError.

        Parámetros:
        - controlError (ControlError): El objeto ControlError con la información de error o éxito.

        Retorna:
        - Response: Una respuesta HTTP con el mensaje de error o éxito y el código de estado correspondiente.
    """
    return Response(statusControl.to_json())