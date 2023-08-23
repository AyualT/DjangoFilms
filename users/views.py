from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, get_user_model
from django.contrib.auth.models import User, Group
from .forms import SignUpForm, CaptchaForm

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        captcha = CaptchaForm(request.POST)
        if form.is_valid() and captcha.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_mail(user,request)
            return HttpResponse('Please confirm your email address to complete the registration')
            # user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            # login(request,user)
            # return redirect('/')
    else:
        form = SignUpForm()
        captcha = CaptchaForm()
    return render(request, 'registration/create_user.html', {'form':form, 'captcha':captcha})

def send_activation_mail(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Activation link has been send to your email'
    message = render_to_string(
        'registration/acc_active_mail.html',
        {
            'user':user,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user)
        }
    )
    to_email = user.email
    email = EmailMessage(
        mail_subject,
        message,
        to = [to_email]
    )
    email.send()

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, OverflowError, ValueError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request,user)
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')    
    
def get_moderator_status(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            username = request.user.username
            user = User.objects.get(username = username)
            moderator_group = Group.objects.get(name = 'Moderator')
            user.groups.add(moderator_group)
            return HttpResponse('Вы успешно получили статус Модератора')
    else:
        form = CaptchaForm()
    return render(request, 'registration/get_moderator.html', {'form':form})
