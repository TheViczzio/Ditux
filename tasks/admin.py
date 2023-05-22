from django.contrib import admin
from .models import Task
from .models import Parro
from .models import Notidi
from .models import Notiuni
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )



# Register your models here.
admin.site.register(Task, TaskAdmin)

admin.site.register(Parro)

admin.site.register(Notidi)

admin.site.register(Notiuni)
