"""
Serializers for the user API view
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
        try:
            validators.validate_password(password=entered_password, user=user)
        except ValidationError as e:
            errors['password'] = list(e.messages)
        
        if errors:
            raise serializers.ValidationError(errors)
        
        return data


    def create(self, validated_data):
        """Upon data being validated as correct, create and return user with encrypted password"""
        password = validated_data.pop('password', None)
        created_user = get_user_model().objects.create_user(**validated_data)
        if password is not None:
            created_user.set_password(password)
        created_user.save()
        return created_user