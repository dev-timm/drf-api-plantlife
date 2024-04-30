from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.profile_image.url')

    def validate_ad_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Advertisement
        fields = [
            'id', 'owner', 'title', 'plant_type', 'availability', 'price',
            'contact', 'content', 'ad_image', 'created_on', 'updated_on',
            'is_owner', 'profile_id', 'profile_image'
        ]
