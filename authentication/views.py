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
# from .models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string 
# from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

from .forms import RegistrationForm

from .utils import TokenGenerator
# Create your views here.

class login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        new_user = User.objects.create_user(username, email, password)
        return HttpResponseRedirect('/registration_success/')
    
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
                token = TokenGenerator.make_token(user)
                link = reverse('authentication:activate',kwargs={'uidb64':uidb64,'token':token})

                activate_url = 'http://'+domain+link





                email_body=f'Hi {user.username},\n Use the link below to verify your email \n {activate_url}'
                email = EmailMessage(
                        "activate your account",
                        email_body,
                        "from@example.com",
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
        return render(request, 'authentication/register.html',context)
    

        
      
        # Redirect to a success page
        # return render(request, 'authentication/register.html')  # Assuming you have a template named('/registration/success/')
    



# class RegistrationSuccessView(TemplateView):
#     template_name = 'registration_success.html'  # Assuming you have a template named 'registration_success.html'


from django.views.generic import TemplateView

class RegistrationSuccessView(TemplateView):
    template_name = 'authentication/registration_success.html'  # Assuming you have a template named 'registration_success.html'


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             # Create a new user
#             User.objects.create_user(username=username, email=email, password=password)
#             # Redirect to a success page or login page
#             return redirect('login')  # Assuming you have a URL pattern named 'login'
#     else:
#         form = RegistrationForm()
#     return render(request, 'authentication/register.html', {'form': form})

class verification(View):
    def get(self,request,uid64,token):
        return redirect('login')

