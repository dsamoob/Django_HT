from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user.id
        method = self.context['request'].method
        adv_status = self.initial_data.get('status')
        count_open = Advertisement.objects.filter(creator=user, status='OPEN').count()
        if count_open >= 10 and method in ['POST', 'PUT'] and adv_status == 'OPEN' or not adv_status:
            raise serializers.ValidationError({'Error': 'U have already posted 10 advs'})
        elif count_open >= 10 and adv_status == 'OPEN':
            raise serializers.ValidationError({'Error': 'U already have 10+ opened advs'})

        return data

