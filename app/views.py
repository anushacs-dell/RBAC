from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import*
from.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serial=UserSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response({'message':'Registered sucessfully'})
        else:
            return Response({'message':serial.errors})

class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)
        print(user)

        if not user:
            return Response({'message':'Invalid username or password'})
        
        refresh=RefreshToken.for_user(user)
        # access_token = str(refresh.access_token)
        
        # return Response({"message":"Login successfully","token":str(access_token)})
        return Response({'message':'Login sucessfully',"acess_token":str(refresh.access_token),"refresh_token":str(refresh)})
    
class LogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Logout Successful"})
        else:
            return Response({"message":"Invalid refresh token"})

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_view(request):
    if request.user.role !='Admin':
        return Response({"message":"You do not have permission to access this resource"})
    return Response({"message":"Welcome Admin"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_view(request):
    if request.user.role !='User':
        return Response({"message":"You do not have permission to access this resource"})
    return Response({"message":"Welcome User"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def moderator_view(request):
    if request.user.role !='Moderator':
        return Response({"message":"You do not have permission to access this resource"})
    return Response({"message":"Welcome Moderator"})

