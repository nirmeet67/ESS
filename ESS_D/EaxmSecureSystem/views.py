from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('home')  # Replace 'home' with your desired URL
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})