from django.shortcuts import render,redirect
from django.contrib import messages
#from .forms import UserRegisterationForm # imports the overloaded user regesteration form
from .forms import UserRegisterationForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required
def Register(request):
    
    if request.method =='POST':
        
        form = UserRegisterationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}')
            # save will save user into the database
            form.save()
            return redirect('login')
    else:
        form = UserRegisterationForm()
    return render(request, 'users/register.html', {'form' : form})



def Login(request):
    
    return render(request, 'users/login.html')



@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)                  # passing an instance will fill up the input fields with the current values of user info
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Changes Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)             
        p_form = ProfileUpdateForm(instance=request.user.profile) 
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    

    
    return render(request, 'users/profile.html', context)
