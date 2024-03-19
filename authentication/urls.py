from .views import login, registration , usernamevalidation , emailvalidation,verification
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import RegistrationSuccessView
from .import views
from django.urls import path, include
from django.views.generic import RedirectView

app_name = 'authentication'  # Define the namespace here


urlpatterns = [
    path('login/', login.as_view(), name="login"),
    path('registration/', registration.as_view(), name="registration"),
    # path('usernamevalidation', usernamevalidation.as_view(), name="usernamevalidation"),
    path('usernamevalidation/', csrf_exempt(usernamevalidation.as_view()), name="usernamevalidation"),
    path('registration/success/', RegistrationSuccessView.as_view(), name='registration_success'),
    path('emailvalidation/', csrf_exempt(emailvalidation.as_view()), name="emailvalidation"),
    # path('authentication/registration/', RedirectView.as_view(url='register/')),
    path('activate/<uid64>/<token>/',verification.as_view(), name="activate"),
    

]