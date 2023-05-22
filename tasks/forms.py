from django.forms import ModelForm
from django.forms import *
from .models import Task
from .models import Parro
from .models import Notidi
from .models import Notiuni
from .models import Notisub
from .models import Evan
from .models import Acerca
from .models import Dio
from .models import Org
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'imagen', 'nombreDecanato', 'parroquia', 'ciudad']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),

            'nombreDecanato': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),

            'parroquia': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Parroquia',
                    'autocomplete': 'off',
                }
            ),

            'ciudad': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Ciudad',
                    'autocomplete': 'off',
                }
            ),
            
        }

class ParroForm(ModelForm):
    class Meta:
        model = Parro
        fields = ['title', 'nombreParroco', 'ubicacion', 'horasanta', 'eucaristia', 'confesiones']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
            'nombreParroco': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
            'ubicacion': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese Ubicacion',
                    'autocomplete': 'off',
                }
            ),
            'horasanta': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha y hora',
                    'autocomplete': 'off',
                }
            ),
            'eucaristia': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha y hora',
                    'autocomplete': 'off',
                }
            ),
            'confesiones': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha y hora',
                    'autocomplete': 'off',
                }
            ),
            
        }


class NotidiForm(ModelForm):
    class Meta:
        model = Notidi
        fields = ['title', 'noticia']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
            'noticia': Textarea(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingresar Noticia',
                    'autocomplete': 'off',
                }
            ),
        }


class NotiuniForm(ModelForm):
    class Meta:
        model = Notiuni
        fields = ['title', 'noticia']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
            'noticia': Textarea(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese Noticia',
                    'autocomplete': 'off',
                }
            ),
        }


class NotisubForm(ModelForm):
    class Meta:
        model = Notisub
        fields = ['title', 'noticia']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
        }


class EvanForm(ModelForm):
    class Meta:
        model = Evan
        fields = ['title', 'evangelio']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
        }


class AcercaForm(ModelForm):
    class Meta:
        model = Acerca
        fields = ['title', 'acerca']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
        }


class DioForm(ModelForm):
    class Meta:
        model = Dio
        fields = ['title', 'obispo', 'informacion']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
        }


class OrgForm(ModelForm):
    class Meta:
        model = Org
        fields = ['title', 'imagen', 'informacion']
        widgets = {
            'title': TextInput(
                attrs={
                    'name': 'Nombre de decanato:',
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre',
                    'autocomplete': 'off',
                }
            ),
        }


