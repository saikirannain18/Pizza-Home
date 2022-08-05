from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import SendPasswordResetEmailSerializer, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from rest_framework.decorators import api_view
from rest_framework import serializers
from django.shortcuts import get_list_or_404, get_object_or_404



# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
  renderer_classes = [UserRenderer]
  permission_classes = [IsAuthenticated]
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)

class SendPasswordResetEmailView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)

class UserPasswordResetView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def ApiOverview(request):
       api_urls = {
          'all_products':'/',
          'Search by Category ': '/?category=category_name',
          'Add':'/create',
          'Update':'/update/pk',
          'Delete': '/product/pk/delete'

       }

       return Response(api_urls)

@api_view(['POST'])
def add_products(request):
      
      product = ProductSerializer(data=request.data)

      if Product.objects.filter(**request.data).exists():
          raise serializers.ValidationError('This data already exists')

      if product.is_valid():
          product.save()
          return Response(product.data)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_products(request):

      if request.query_params:
        Products =Product.objects.filter(**request.query_param.dict())
      else:
        products =Product.objects.all()
        serializer = ProductSerializer(products, many=True)

      if products :
          return Response(serializer.data)
      else:
          return Response(status=status.HTTP_404_NOT_FOUND) 


@api_view(['POST'])
def update_products(request,pk):
      product = Product.objects.get(pk=pk)
      data = ProductSerializer(instance =product,data=request.data)

     

      if data.is_valid():
          data.save()
          return Response(data.data)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_products(request,pk):
      product = get_object_or_404(Product, pk=pk)
      product.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
  