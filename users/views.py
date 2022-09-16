from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from users.forms import User_registration_form, UserEditForm
from users.models import User_profile
from django.contrib.auth.decorators import login_required


def login_request (request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=clave)
            if usuario is not None:
                login(request,usuario)
                context={'message':f'Bienvenido {nombre_usuario} !!'}
                return render(request,'index.html',context=context)
        form=AuthenticationForm()
        context={'error':'Usuario o contraseña incorrectos','form':form}
        return render(request,'users/login.html',context=context)
        
    elif request.method == 'GET':
        form=AuthenticationForm()
        context={'form':form}
    return render(request,'users/login.html',context=context)

def login_request_super (request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            nombre_usuario= form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario,password=clave)
            if usuario is not None:
                login(request,usuario)
                context={'message':f'Bienvenido {nombre_usuario} !!'}
                return render(request,'index.html',context=context)
        form=AuthenticationForm()
        context={'error':'Usuario o contraseña incorrectos','form':form}
        return render(request,'users/login.html',context=context)
        
    elif request.method == 'GET':
        form=AuthenticationForm()
        context={'form':form}
    return render(request,'users/login-super.html',context=context)

def register(request):
    if request.method == 'POST':
        form=User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')            
        else:
            context={'errors':form.errors}
            form=User_registration_form()
            context['form']=[form]
            return render(request, 'users/register.html',context)

    elif request.method == 'GET':
        form=User_registration_form()
        return render (request,'users/register.html',{'form':form})

    
@login_required
def update_profile(request):

    user=request.user

    if request.method == 'POST':
        form=UserEditForm(request.POST,request.FILES)

        if form.is_valid():
            
            user.first_name=form.cleaned_data['first_name']
            user.last_name=form.cleaned_data['last_name']
            user.email=form.cleaned_data['email']
            user.phone=form.cleaned_data['phone']
            user.adress=form.cleaned_data['adress']
            user.save()

            return redirect ('index')
    
    elif request.method == 'GET':
        
        form=UserEditForm(initial={'first_name':user.first_name,
                                    'last_name':user.last_name,
                                    'email':user.first_name,
                                    })
        context={'form':form, 'user':user}
        return render (request, 'users/update-profile.html',context=context)