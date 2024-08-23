
from django.urls import include, path
from core_tasks.core import urls as core_urls

urlpatterns = [
    path('test/', include(core_urls)),
]
