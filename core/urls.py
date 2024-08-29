from django.urls import path 
from .views.test import TestApiView

urlpatterns = [
    path('proc', TestApiView.test_proc),
    path('func', TestApiView.test_func),
    path('func2', TestApiView.test_func_2),
    path('func3', TestApiView.test_func_3),
    path('test_two', TestApiView.test_func_two),
]
