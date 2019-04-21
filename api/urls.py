from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

todo_management = views.TodoViewSet.as_view({'post': 'create'})
complete_todo = views.TodoViewSet.as_view({'post': 'complete_todo'})
project_management = views.ProjectViewSet.as_view({'post': 'create'})

urlpatterns = [
    url(r'^v1/todos/$', todo_management, name='todo_management'),
    url(r'^v1/complete-todo/$', complete_todo, name='complete_todo'),
    url(r'^v1/projects/$', project_management, name='project_management'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
