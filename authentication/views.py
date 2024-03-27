from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from json import loads
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib3 import HTTPResponse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import auth
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage,send_mail

from django.utils.encoding import force_bytes,DjangoUnicodeDecodeError
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import account_activation_token
from django.contrib.auth import get_user_model
from .utils import TokenGenerator

class usernamevalidation(View):
    def post(self, request):    
        data = loads(request.body)
        username=data['username']
        if not str(username).isalnum():
            messages.error(request, 'username should only contain letters and numbers')
            return JsonResponse({'error':'username should only contain letters and numbers <br>'},status=400)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return JsonResponse({'error':'username already exists'},status=409)
        return JsonResponse({'username_valid':True})
    
class emailvalidation(View):
    def get(self, request):    
        data = loads(request.body)
        email=data['email']
        if not validate_email(email):
            messages.error(request, 'email is not valid')
            return JsonResponse({'email_error':'email is not valid'},status=400)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return JsonResponse({'email_error':'email already exists'},status=409)
        return JsonResponse({'email_valid':True})
    

class registration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context={
            'fieldValues': request.POST
        }
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html',context)
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()

                #path to view in mail
                #-getting domain of current site
                # rrelative url to verify email
                # encode uid and token
                
                domain = get_current_site(request).domain
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)                # link = reverse('activate',kwargs={'uidb64':uidb64,'token':token})
                # link = reverse('authentication:activate',kwargs={'uidb64':uidb64,'token':token})
                link= reverse('activate', kwargs={'uid64': uidb64, 'token': token})

                activate_url = 'https://'+domain+link

                email_body={
                    'user': user,
                    'domain': domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    'link': activate_url
                }



                email = EmailMessage(
                        "activate your account",
                        email_body,
                        "HgUeh@example.com",
                        [email],
                        
                )
                # email.connection = email.get_connection()
                email.connection.open()

                email.send(fail_silently=False)
                messages.success(request, 'Account created successfully ')
                return render(request, 'authentication/register.html')
            messages.error(request, 'Email already exists')
            return render(request, 'authentication/register.html',context)
        messages.error(request, 'Username already exists')
        return render(request, 'authentication/login.html',context)
    

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class verification(View):
    def get(self, request, uid64, token):

        try:
            id = force_str(urlsafe_base64_decode(uid64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('login')

            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:

            pass
        return redirect('login')
    
      

class login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, '+ user.username)
                    return redirect(request,'/register.html')
                messages.error(request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')
        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


from django.views.generic import TemplateView

class RegistrationSuccessView(TemplateView):
    template_name = 'authentication/registration_success.html'  # Assuming you have a template named 'registration_success.html'

class LogOutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect(request,'login')
    






