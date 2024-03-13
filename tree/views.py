from tree.models import Tree
from tree.serializers import TreeSerializer, CreateTreeSerializer
from customize.views import CustomViewSet


class TreeView(CustomViewSet):
    serializer_class = TreeSerializer
    permission_classes = []
    queryset = Tree.objects.all()
    allowed_methods = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'list':
            return TreeSerializer
        else:
            return CreateTreeSerializer

    def get_queryset(self):
        return Tree.objects.filter(parent=None)


class UpdateTreeView(CustomViewSet):
    serializer_class = CreateTreeSerializer
    permission_classes = []
    queryset = Tree.objects.all()
    allowed_methods = ['patch', 'delete']
