from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

# I'll refactor this later

@api_view(["POST"])
def signup(request):
    serializer = UserSerializer(data = request.data)
    
    if serializer.is_valid():
        # If the request data is valid then we let the user sign up
        serializer.save()
        user = User.objects.get(username = request.data["username"])
        user.set_password(request.data["password"])
        token = Token.objects.create(user = user)
        user.save()
        
        return Response({
            "token" : token.key, 
            "user": serializer.data
        })
    
    # If the request is not valid then we send back an error
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    user = get_object_or_404(User, username = request.data["username"])
    
    if not user.check_password(request.data["password"]):
        # If the password doesnt match we return 404 NOT FOUND
        return Response(
            {"detail": "Not found."}, 
            status = status.HTTP_404_NOT_FOUND
        )
    
    token, created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance = user)
    
    return Response({
        "token" : token.key, 
        "user": serializer.data
    })

# Test route to check if logged in
@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    return Response({f"Passed for {request.user.username}"})