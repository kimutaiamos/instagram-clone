from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Image, Profile, Comments
from .forms import SignupForm, ImageForm, ProfileForm, CommentForm
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .emails import send_activation_email
from .tokens import account_activation_token
# Create your views here.
@login_required(login_url='/')
def home(request):
    images = Image.get_all_images()

    return render(request, 'index.html', {'images':images})


def signup(request):
    if request.user.is_authenticated():
        return redirect('home')

    else:
            if request.method == 'POST':
                form = SignupForm(request.POST)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.is_active= False
                    user.save()
                    current_site = get_current_site(request)
                    to_email = form.cleaned_data.get('email')
                    send_activation_mail(user, current_site(request))
                    return HttpResponse('confirm your email address to complete user registration')

            else:
                form = SignupForm()
                return render (request, 'registration/signup.html',{'form:form'})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError,OverflowError, User.DoesNotExist):
            user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        return HttpResponse('registration/login.html')

    else:
            return HttpResponse('Activation link is invalid')


def profile(request, username):
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'profile/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images})







