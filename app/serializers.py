from rest_framework import serializers
from.models import*
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','username','email','password','role']

    def validate(self,data):
        if data['username']:
            if CustomUser.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is already exists')
            
        if data['email']:
            if CustomUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is already exists')
            
        return data

    def create (self,validated_data):
            user=CustomUser.objects.create(username=validated_data['username'],email=validated_data['email'],role=validated_data.get('role', 'User'))
            user.set_password(validated_data['password'])     
            user.save()
            return user

