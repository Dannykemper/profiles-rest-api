from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Een serializer vertaalt complexe Python-objecten (zoals modellen) naar JSON (en andersom).
    Dit is belangrijk voor API’s, want browsers of frontend apps begrijpen alleen JSON of andere standaardformaten."""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    """Voor een user profiel serializer in combinatie met een ModelViewSet is create() en update() nodig als je met wachtwoorden werkt."""

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
