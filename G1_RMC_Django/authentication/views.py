import json
from django.views import View
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

class forgotpasswordView(View):
    def get(self,request):
        return render(request,'authentication/forgotpassword.html')

class loginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('invoices')  # Redirect to invoices page
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'authentication/login.html')


class registerView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']

        # Check if a user with this email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
            return render(request, 'authentication/register.html')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        messages.success(request, 'User created successfully.')
        return render(request,'authentication/login.html')
        


class emailValidation(View):
    import json
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error' : 'Email is invalid'}, status = 400) 
        
        # The below error is with user module (Not sure how it is used) 

        # if User.object.filter(email=email).exists():
        #     return JsonResponse({'email_invalid' : 'Sorry, Email already in Use, Choose another'}, status = 409)
        return JsonResponse({'email_valid' : True})

        