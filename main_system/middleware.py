# middleware.py
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from jwt import decode, InvalidTokenError
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication

from main_system.custom_classes.status_control import StatusControl

class ApiErrorMiddleware:

    """
        Middleware para capturar y manejar excepciones no controladas en vistas de Django, devolviendo una respuesta JSON con el mensaje de error.
    
        Este middleware se encarga de capturar cualquier excepción no controlada que ocurra durante el procesamiento de una solicitud y devolver una respuesta JSON con el mensaje de error. Esto es útil para APIs donde se prefiere una respuesta JSON uniforme en caso de errores.
    
        Métodos:
        - __init__(self, get_response): Inicializa el middleware con la función de respuesta proporcionada por Django.
        - __call__(self, request): Llama a la función de respuesta para procesar la solicitud.
        - process_exception(self, request, exception): Procesa cualquier excepción no controlada, encapsulándola en una respuesta JSON.
    """

    def __init__(self, get_response):
        """
            Inicializa una nueva instancia de ApiErrorMiddleware.

            Parámetros:
            - get_response (callable): La función de respuesta proporcionada por Django.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
            Procesa la solicitud y devuelve la respuesta.

            Parámetros:
            - request (HttpRequest): La solicitud HTTP entrante.

            Retorna:
            - HttpResponse: La respuesta HTTP generada por la vista.
        """
        response = self.get_response(request)
        return response

    def process_exception(self, exception):
        """
            Procesa cualquier excepción no controlada, encapsulándola en una respuesta JSON.

            Parámetros:
            - request (HttpRequest): La solicitud HTTP en la que ocurrió la excepción.
            - exception (Exception): La excepción no controlada que se lanzó.

            Retorna:
            - JsonResponse: Una respuesta JSON con el mensaje de error y un código de estado HTTP 500.
        """

        error_response = StatusControl.error_message(str(exception))

        return JsonResponse(error_response.to_json(), status=500)

class JWTCookieMiddleware(MiddlewareMixin):
    """
    Este middleware intercepta las solicitudes entrantes, extrae un JWT (JSON Web Token) 
    de la cookie 'jwt_token' si está presente, lo valida y establece el atributo 
    `request.user_id` basado en la carga útil del token, si es válido.
    """

    def process_request(self, request):
        bypassed_urls = byPassed()
        is_bypassed = request.path in bypassed_urls or '.well-known' in str(request.path) or 'api/Publico/Imagen' in str(request.path)

        if not is_bypassed:
            response = {'status': 'error'}

            jwt_token = request.COOKIES.get('jwt_token')

            if not jwt_token:
                response['message'] = 'Sin datos de autorización.'
                return JsonResponse(response, status=401)

            try:
                # Decode and verify the JWT
                payload = decode(jwt_token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=['HS256'])
                request.user_id = payload.get('user_id')
            except InvalidTokenError as e:
                response['message'] = f'Token JWT Inválido: {str(e)}'
                return JsonResponse(response, status=401)

class CustomJWTAuthentication(JWTAuthentication):
    """
    Clase de autenticación JWT personalizada que recupera el token JWT de la cookie 
    en lugar del encabezado de autorización.
    """

    def authenticate(self, request):
        jwt_token = request.COOKIES.get('jwt_token')
        if jwt_token:
            try:
                validated_token = self.get_validated_token(jwt_token)
                user = self.get_user(validated_token)
                return (user, validated_token)
            except InvalidTokenError:
                return None
        return None

    def get_user(self, validated_token):
        """
        Extrae el ID de usuario de la carga útil del token JWT validado.
        """
        user_id = validated_token.get('user_id')

        class UserInfo:
            is_authenticated = user_id is not None
            id_user = user_id

        return UserInfo()

def byPassed():
    return [
        # bypassed/public routes
    ]