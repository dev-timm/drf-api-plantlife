from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import IntegrityError
from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_on = serializers.SerializerMethodField()

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

    class Meta:
        model = Report
        fields = [
            'id', 'owner', 'post', 'report_reason', 'created_on'
        ]
