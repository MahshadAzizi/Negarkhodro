from django.urls import path
from tree.views import TreeView, UpdateTreeView
urlpatterns = [
    path('', TreeView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='index'),
    path('<int:pk>', UpdateTreeView.as_view({
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='update')
]
