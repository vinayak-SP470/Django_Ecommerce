from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Home page view
def homePage(request):
    return render(request, template_name="home.html")

# User signup logic
def user_signup(request):
    if request.method == 'POST':
        user_reg_form = UserRegistrationForm(request.POST)
        if user_reg_form.is_valid():
            new_user = user_reg_form.save(commit=False)
            new_user.set_password(user_reg_form.cleaned_data['password'])
            new_user.save()
            return render(request,'home.html',{'user_reg_form':user_reg_form})
    else:
        user_reg_form = UserRegistrationForm()
    return render(request,'signup.html',{'user_reg_form':user_reg_form})

# user login logic
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

# user logout logic
def logout_user(request):
    logout(request)
    return redirect('home')

# Custom error message for invalid username or password
class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Please enter a correct username and password. Both fields may be case-sensitive.",
    }
