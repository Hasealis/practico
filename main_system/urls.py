
from django.urls import include, path
from core import urls as core_urls

urlpatterns = [
    path('test/', include(core_urls)),
]
