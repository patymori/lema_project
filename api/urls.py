from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DepartmentListView, EmployeeCreateView, EmployeeDeleteView

urlpatterns = {
    url(r'^department/$', DepartmentListView.as_view(), name='list'),
    url(r'^employee/$', EmployeeCreateView.as_view(), name='add'),
    url(r'^employee/$', EmployeeCreateView.as_view(), name='list'),
    url(r'^employee/(?P<pk>[0-9]+)/$', EmployeeDeleteView.as_view(), name='remove'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
