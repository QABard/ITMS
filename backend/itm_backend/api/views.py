from django.shortcuts import get_object_or_404, redirect
from projects.models import Project, Task
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly, IsParticipantOrReadOnly
from .serializers import (
    ProjectGetSerializer,
    ProjectPostSerializer,
    TaskGetSerializer,
    TaskPostSerializer,
    TeamSerializer,
)
from .services import PROJECT_EXAMPLE_NAME, add_project_example


class ProjectViewSet(viewsets.ModelViewSet):
    """Вьюсет модели Project"""

    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ProjectGetSerializer
        return ProjectPostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get"], permission_classes=[IsAuthenticated])
    def team(self, request, pk=None):
        """Отображает команду проекта."""
        project = get_object_or_404(Project, pk=pk)
        serializer = TeamSerializer(project, context={"request": request})
        return Response(serializer.data)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def project_example(self, request):
        project = Project.objects.filter(owner=request.user, name=PROJECT_EXAMPLE_NAME).first()
        if not project:
            project = add_project_example(request.user)
        return redirect("project-detail", pk=project.id)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsParticipantOrReadOnly)
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return TaskGetSerializer
        return TaskPostSerializer

    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs["projects_id"])
        serializer.save(creator=self.request.user, task_project_id=project.id)
