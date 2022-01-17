from .models import Task, Tag,Table
from rest_framework import viewsets
from .serializers import TaskSerializer, TagSerializer,TableSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset=Table.objects.all()
    serializer_class=TableSerializer