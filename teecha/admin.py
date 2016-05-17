from django.contrib import admin
from .models import Lesson

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



