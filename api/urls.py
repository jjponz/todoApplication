from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

todo_management = views.TodoViewSet.as_view({'post': 'create'})

urlpatterns = [url(r'^v1/todos/$', todo_management, name='todo_management')]

urlpatterns = format_suffix_patterns(urlpatterns)
