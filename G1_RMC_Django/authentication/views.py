import json
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib.auth.models import User

# Create your views here.
class loginView(View):
    def get(self,request):
        return render(request,'authentication/login.html')

class registerView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
class emailValidation(View):
    import json
    def post(self,request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error' : 'Email is invalid'}, status = 400) 
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_invalid' : 'Sorry, Email already in Use, Choose another'}, status = 400)
        return JsonResponse({'email_valid' : True})

        