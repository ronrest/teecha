from django.contrib import admin
from .models import Lesson, Module, ModuleLesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "hidden_description")

    fields = ('name',
              'title',
              'published',
              'video',
              'video_service',
              'content',
              'description',
              'hidden_description',
              )


class ModuleLessonInline(admin.TabularInline):
    """
    Allows the ModuleLesson "Through" Model to appear in the admin
    for Module
    """
    model = ModuleLesson
    extra = 1

class ModuleAdmin(admin.ModelAdmin):
    # Allows you to add lessons one at a time
    inlines = (ModuleLessonInline,)

# Register your models here.
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Module, ModuleAdmin)

