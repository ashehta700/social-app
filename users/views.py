from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import userRegisterForm , UserUpdateForm ,ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST' :
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request , f'welcome {username} To Or WebSite we are happy to be here :) , You must to be Login !')    
            return redirect('login')
    else:    
        form = userRegisterForm()
    return render(request, 'users/register.html' , {'form':form} )


#that you must be login first before you see the profile
@login_required
def profile(request):
    if request.method == 'POST' :
        # update user and profile update and get instance to see the input value and then Check the invalid form for POST method ?!
        # save this form for user and profile and get the sucess message for both 
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST ,request.FILES , instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request , f'Your Profile has been Updated !')    
            return redirect('profile')
            
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    
    return render(request , 'users/profile.html' ,context )
    