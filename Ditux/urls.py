"""
URL configuration for Ditux project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('parros/', views.parros, name='parros'),
    path('parro/create/', views.create_parro, name='create_parro'),
    path('parros/<int:parro_id>/', views.parro_detail, name='parro_detail'),
    path('notidios/', views.notidios, name='notidios'),
    path('notidio/create/', views.create_notidio, name='create_notidio'),
    path('notidios/<int:notidio_id>/', views.notidio_detail, name='notidio_detail'),
    path('notiunis/', views.notiunis, name='notiunis'),
    path('notiuni/create/', views.create_notiuni, name='create_notiuni'),
    path('notiuni/<int:notiuni_id>/', views.notiuni_detail, name='notiuni_detail'),
    path('notisubs/', views.notisubs, name='notisubs'),
    path('evans/', views.evans, name='evans'),
    path('acercas/', views.acercas, name='acercas'),
    path('dios/', views.dios, name='dios'),
    path('orgs/', views.orgs, name='orgs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)