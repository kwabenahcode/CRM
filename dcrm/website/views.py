from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!! ")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in!...Try again")
    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login User
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully Registered! Welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, primaryKey):
    if request.user.is_authenticated:
        #see records
        customer_record = Record.objects.get(id=primaryKey)
        return render(request, 'record.html', {'customer_record': customer_record })
    else:
        messages.success(request, "You must log in to view that page")
        return redirect('home')

def delete_record(request, primaryKey):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=primaryKey)
        delete_it.delete()
        messages.success(request, "Successfully Deleted! ")
        return redirect('home') 
    else:
        messages.success(request, "You must log in to  delete a Record")
        return redirect('home')
        
    
        
    
    

