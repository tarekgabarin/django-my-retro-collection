"""
Serializers fopr the user API view
"""
import django.contrib.auth.password_validation as validators
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {"password": {"write_only": True, 'min_length': 5}}

    def validate(self, data):
        entered_password = data.get('password')
        errors = dict()
        user = get_user_model()
        print(entered_password)
        try:
            validators.validate_password(password=entered_password, user=user)
        except ValidationError as e:
            errors['password'] = list(e.messages)
        
        print(errors)

        if errors:
            raise serializers.ValidationError(errors)
        
        return entered_password


    def create(self, validated_data):
        """Upon data being validated as correct, create and return user with encrypted password"""
        print('create function of serializer running at line 34')
        print(validated_data)
        created_user = get_user_model().objects.create_user(**validated_data)
        return created_user