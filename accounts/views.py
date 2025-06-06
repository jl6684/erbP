from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
           if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('accounts:register')
           else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('accounts:login')
           
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
        # Handle registration logic here
    else:
        return render(request, 'accounts/register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:    
        return render(request, 'accounts/login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You have been logged out')
    return redirect('pages:index')

def dashboard(request):
    # Assuming user is authenticated, you can access user info like this:
    if request.user.is_authenticated:
        from contacts.models import Contact
        user = request.user
        contacts = Contact.objects.filter(user=user).order_by('-contact_date')
        context = {
            'user': user,
            'contacts': contacts,
        }
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('accounts:login')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        
        # Check if email is already taken by another user
        if User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, 'This email is already taken by another user')
            return redirect('accounts:profile')
        
        # Update user information
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/profile.html')