
from main_system.database_controllers.procedure import sql_exec_procedure
from main_system.database_controllers.function import sql_exec_function
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class TestApiView(APIView):

    @api_view(('GET',))
    def test_func(request):
        result = sql_exec_function('core_func_do_nothing', request)
        return result.to_response()

    @api_view(('GET',))
    def test_func_two(request):
        print('hello world.')
        result = sql_exec_procedure('core_proc_do_nothing', request)
        return result.to_response()
    
    @api_view(('GET',))
    def test_proc(request):
        result = sql_exec_procedure('core_proc_do_nothing', request)
        return result.to_response()
    
    @api_view(('GET',))
    def test_func_2(request):
        result = sql_exec_function('core_func_do_nothing_2', request)
        return result.to_response()
    
    @api_view(('GET',))
    def test_func_3(request):
        result = sql_exec_function('core_func_do_nothing_3', request, True)
        return result.to_response()