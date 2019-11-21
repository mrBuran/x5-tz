"""Api views."""
from api.models import Application
from api.serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class ApplicationViewBase:
    """Base class of models.Application.

    Use this class as parent for API endpoints. It provides
    filtration by user, token creation and another common
    logic.

    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        """Override default method: add user context.

        Get only objects which are belong to user.
        """
        return self.queryset.filter(user=self.request.user)

    def perform_update(self, serializer):
        """Override `mixins.UpdateModelMixin.update()` method.

        We should ignore changes of key.
        """
        serializer._validated_data.pop("key")
        serializer.save()

    def get_serializer_context(self):
        """Extend serializer context."""
        context = super().get_serializer_context()
        user = context["request"].user
        token, created = Token.objects.get_or_create(user=user)
        context["request"].data["key"] = token.key
        return context

    def perform_create(self, serializer):
        """Populate fields which are not present in serializer.

        This method will run after validation.
        """
        request = serializer.context["request"]
        user = request.user
        serializer._validated_data["user"] = user
        serializer.save()


class ApplicationViewSetBasicAuth(
    ApplicationViewBase, viewsets.ModelViewSet, APIView
):
    """Handler of requests with basic auth to /api/apps."""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ApplicationViewSetTokenAuth(
    ApplicationViewBase, viewsets.ModelViewSet, APIView
):
    """Handler of requests with basic auth to /api/test."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class GenerateNewKeyBasicAuth(APIView):
    """Generate new API token."""

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """Get new API token."""
        user = request.user
        Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        Application.objects.filter(user=user).update(key=token.key)
        return Response({"key": token.key})
