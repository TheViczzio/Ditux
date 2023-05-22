from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import ParroForm
from .models import Parro
from .models import Notidi
from .forms import NotidiForm
from .models import Notiuni
from .forms import NotiuniForm
from .models import Notisub
from .forms import NotisubForm
from .models import Evan
from .models import Acerca
from .models import Dio
from .models import Org
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
                
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

def tasks(request):
    tasks =Task.objects.all()

    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method =='GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form =TaskForm(request.POST, request.FILES)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
            'form': TaskForm,
            'error': 'por favor poner datos validos'
        })
 
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)    
    return render(request, 'task_detail.html', {'task': task})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET': 
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user= authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Nombre o contraseña incorrectos, si sigue pasando, contacte a un administrador con el siguiente correo: admin@admin.com'
        })
        else:
            login(request, user)
            return redirect('home')
        

def parros(request):        
    parros =Parro.objects.all()

    return render(request, 'parro.html', {'parros': parros})

@login_required
def create_parro(request):
    if request.method =='GET':
        return render(request, 'create_parro.html', {
            'form': ParroForm
        })
    else:
        try:
            form =ParroForm(request.POST, request.FILES)
            new_parro = form.save(commit=False)
            new_parro.user = request.user
            new_parro.save()
            print ('JALO EL PEDO')
            return redirect('parros')
        except ValueError:
            return render(request, 'create_parro.html', {
            'form': ParroForm,
            'error': 'por favor poner datos validos'
        })

def parro_detail(request, parro_id):
    parro = get_object_or_404(Parro, pk=parro_id)    
    return render(request, 'parro_detail.html', {'parro': parro})

def notidios(request):        
    notidios =Notidi.objects.all()

    return render(request, 'notidio.html', {'notidios': notidios})

@login_required
def create_notidio(request):
    if request.method =='GET':
        return render(request, 'create_notidio.html', {
            'form': NotidiForm, "form2":NotiuniForm
        })
    else:
        try:
            form =NotidiForm(request.POST, request.FILES)
            new_notidio = form.save(commit=False)
            new_notidio.user = request.user
            new_notidio.save()
            print ('JALO EL PEDO')
            return redirect('notidios')
        except ValueError:
            return render(request, 'create_notidio.html', {
            'form': NotidiForm, "form2":NotiuniForm,
            'error': 'por favor poner datos validos'
        })

def notidio_detail(request, notidio_id):
    notidio = get_object_or_404(Notidi, pk=notidio_id)    
    return render(request, 'notidio_detail.html', {'notidio': notidio})

def notiunis(request):        
    notiunis =Notiuni.objects.all()

    return render(request, 'notiuni.html', {'notiunis': notiunis})

@login_required
def create_notiuni(request):
    if request.method =='POST':
        try:
            form =NotiuniForm(request.POST, request.FILES)
            new_parro = form.save(commit=False)
            new_parro.user = request.user
            new_parro.save()
            print ('JALO EL PEDO')
            return redirect('notiunis')
        except ValueError:
            return render(request, 'create_notidio.html', {
            'form': NotidiForm, "form2":NotiuniForm,
            'error': 'por favor poner datos validos'
        })

def notiuni_detail(request, notiuni_id):
    notiuni = get_object_or_404(Notiuni, pk=notiuni_id)    
    return render(request, 'notiuni_detail.html', {'notiuni': notiuni})

def notisubs(request):        
    notisubs =Notisub.objects.all()

    return render(request, 'notisub.html', {'notisub': notisubs})

def evans(request):
    evans =Evan.objects.all()

    return render(request, 'evan.html', {'evans': evans})

def acercas(request):
    acercas =Acerca.objects.all()

    return render(request, 'acerca.html', {'acercas': acercas})

def dios(request):
    dios =Dio.objects.all()

    return render(request, 'dio.html', {'dios': dios})

def orgs(request):
    orgs =Org.objects.all()

    return render(request, 'org.html', {'orgs': orgs})      







