from rest_framework import serializers

from tree.models import Tree


class TreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        fields = ['id', 'name', 'children']

    def get_fields(self):
        fields = super(TreeSerializer, self).get_fields()
        fields['children'] = TreeSerializer(many=True)
        return fields


class CreateTreeSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(queryset=Tree.objects.all(), slug_field='name', write_only=True,
                                          required=False)

    class Meta:
        model = Tree
        fields = ['id', 'name', 'parent']
