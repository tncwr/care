from django.conf import settings
from django_filters import rest_framework as filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.serializers import Serializer, UUIDField, CharField
from rest_framework.viewsets import GenericViewSet
from rest_framework.parsers import JSONParser

from care.facility.api.serializers.uccbedrequest import UCCBedRequestSerializer
from care.facility.models.uccbedrequest import UCCBedRequest
from care.utils.filters.choicefilter import CareChoiceFilter, inverse_choices
from care.utils.notification_handler import NotificationGenerator
from care.utils.queryset.facility import get_facility_queryset


class UCCBedRequestViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UCCBedRequestSerializer
    permission_classes = [IsAuthenticated]
    #lookup_field = "external_id"

    # inside OrganisationDetail
    queryset = UCCBedRequest.objects.all()

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticatedOrReadOnly])
    def public_key(self, request, *args, **kwargs):
        return Response({"public_key": settings.VAPID_PUBLIC_KEY})
    
    @swagger_auto_schema(request_body=UCCBedRequestSerializer, responses={200: UCCBedRequestSerializer()})
    @action(detail=False, methods=["POST"])
    def uccbedrequest(self, request):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = UCCBedRequestSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_200_OK)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)