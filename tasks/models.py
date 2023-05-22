from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="images/%Y/%m/%d", null = False, blank = True)
    nombreDecanato = models.TextField(blank=True)
    parroquia = models.TextField(blank=True)
    ciudad = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Parro(models.Model):
    title = models.CharField(max_length=100)
    nombreParroco = models.TextField(blank=True)
    ubicacion = models.TextField(blank=True)
    horasanta = models.TextField(blank=True)
    dia1 = models.TextField(blank=True)
    eucaristia = models.TextField(blank=True)
    dia2 = models.TextField(blank=True)
    confesiones = models.TextField(blank=True)
    dia3 = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Notidi(models.Model):
    title = models.CharField(max_length=100)
    noticia = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username

class Notiuni(models.Model):
    title = models.CharField(max_length=100)
    noticia = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Notisub(models.Model):
    title = models.CharField(max_length=100)
    noticia = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Evan(models.Model):
    title = models.CharField(max_length=100)
    evangelio = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Acerca(models.Model):
    title = models.CharField(max_length=100)
    acerca = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username
    
class Dio(models.Model):
    title = models.CharField(max_length=100)
    obispo = models.TextField(blank=True)
    informacion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username   
    
class Org(models.Model):
    title = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="images/%Y/%m/%d", null = False, blank = True)
    informacion = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return self.title + '- by' + self.user.username 