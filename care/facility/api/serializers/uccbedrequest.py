from django.db.models import F
from rest_framework import serializers


from care.facility.models.uccbedrequest import UCCBedRequest

from care.users.api.serializers.user import UserBaseMinimumSerializer
from config.serializers import ChoiceField
from care.facility.api.serializers import TIMESTAMP_FIELDS


class UCCBedRequestSerializer(serializers.ModelSerializer):
    #id = serializers.UUIDField(source="external_id", read_only=True)

    class Meta:
        model = UCCBedRequest
        exclude = (
            "deleted",
            "modified_date",
            "external_id",
            "id"
        )
        read_only_fields = (
            TIMESTAMP_FIELDS,
            "id",
            "created_date",
        )

    def create(self, validated_data):

            bed_request = super(UCCBedRequestSerializer, self).create(validated_data)

            return bed_request
