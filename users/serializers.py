from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    """
    Serializer for registering new users.
    Uses the custom user model and ensures the password is write-only.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Serializer configuration:
        """
        model = User
        fields = ['id', 'email', 'password']

    def create(self, validated_data):

        """
        Create and return a new user instance with an encrypted password.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
