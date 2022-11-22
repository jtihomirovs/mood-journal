# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This serializer defines fields for registration.
    It will try to register the user when validated.
    """
    class Meta:
        User = get_user_model()
        model = User
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True, 'allow_blank': False}
                        }

    def create(self, validated_data):
        User = get_user_model()
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
    * username
    * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )

    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        User = get_user_model()
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'image',
        ]

        extra_kwargs = {
            'username': {'read_only': True}
        }
