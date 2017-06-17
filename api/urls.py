from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import EmployeeCreateView


urlpatterns = [
    url(r'^employee/$', EmployeeCreateView.as_view(), name='add'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
