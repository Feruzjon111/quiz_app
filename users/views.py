from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Login or password is incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Now you can log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm

@login_required
def profile_view(request):
    return render(request, 'profile.html')

# users/views.py
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

def profile_edit(request):
    # Foydalanuvchining profilini olishga harakat qilamiz
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Agar profil mavjud bo'lmasa, yangi profil yaratish
        profile = UserProfile(user=request.user)
        profile.save()

    # Profilni tahrir qilish
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Profilni ko'rish sahifasiga qaytish
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile_edit.html', {'form': form})






