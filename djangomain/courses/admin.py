from django.contrib import admin
from .models import Course, Module, ModuleItem, Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(ModuleItem)
admin.site.register(Lesson)
