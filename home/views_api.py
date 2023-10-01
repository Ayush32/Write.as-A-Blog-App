from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
from .models import Profile

from django.contrib import messages

class LoginView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'Key username not Found'
                raise Exception('Key username not Found')

            if data.get('password') is None:
                response['message'] = 'Key password not Found'
                raise Exception('Key password not Found')
            
            check_user = User.objects.filter(username= data.get('username')).first()
            if check_user is None:
                response['message'] = 'Invalid username, User not found'
                raise Exception('Invalid username, User not Found')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            if user_obj:
                login(request,user_obj )
                response['status'] = 200
                messages.success(request, 'Login successfully!')
                response['message'] = 'Welcome! Login Successfully'
            else:
                response['message'] = 'Invalid Password'
                raise Exception('Invalid Password! Try Again')
                
        except Exception as e:
            print(e)
        return Response(response)
            
LoginView = LoginView.as_view()
            
class RegisterView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'
        try:
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'Key username not Found'
                raise Exception('Key username not Found')

            if data.get('password') is None:
                response['message'] = 'Key password not Found'
                raise Exception('Key password not Found')
            
            check_user = User.objects.filter(username= data.get('username')).first()
            if check_user:
                messages.error(request, "Username already exists!")
                response['message'] = 'username already exists!'
                raise Exception('username already exists')
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            messages.success(request, 'Registration Successfully!')
            response['message'] = 'User Registered Successfully'
            # messages.success(request, "Registration Successfully!")
            
            # user_obj = authenticate(username = data.get('username'), password = data.get('password'))
            # if check_user is None:
            #     # response['status'] = 200
            #     response['message'] = 'username Already Exists'
            #     raise Exception('username Already Exists')
            
        except Exception as e:
            print(e)
        return Response(response)
            
RegisterView = RegisterView.as_view()
            