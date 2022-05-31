from django.contrib import admin

from api.models import Todo, Task

admin.site.register([Todo, Task])
