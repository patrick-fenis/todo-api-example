
from .models import Todo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]


