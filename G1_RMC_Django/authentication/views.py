import json
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib.auth.models import User

# Create your views here.

class forgotpasswordView(View):
    def get(self,request):
        return render(request,'authentication/forgotpassword.html')

class loginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')

class registerView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    # messages for register page
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        # if not User.objects.filter(email=email).exists():
        #     user = User.objects.create_user(email=email)
        #     user.set_password(password)
        #     user.save()
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

        