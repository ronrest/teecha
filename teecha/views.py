from django.shortcuts import render, HttpResponse
from django import template
import markdown
from .models import Lesson

register = template.Library()


# ==============================================================================
#                                                                    MARKDOWNIFY
# ==============================================================================
@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text, safe_mode='escape')


# ==============================================================================
#                                                                FIX LESSON URLS
# ==============================================================================
def fix_lesson_urls(content, lesson_name):
    return content.replace("LESSON_IMG_DIR", lesson_name)


# ==============================================================================
#                                                                          INDEX
# ==============================================================================
def index(request):
    return HttpResponse("This is the index for teecha")


# ==============================================================================
#                                                                         LESSON
# ==============================================================================
def lesson(request, id):
    # TODO: perform error checking to make sure lesson_id is a valid lesson id.
    #       eg, it must be an integer.
    lesson = Lesson.objects.get(id=id)

    content = markdownify(lesson.content)
    content = fix_lesson_urls(content, "/static/teecha/img")
    context = {
        "content": content,
        "title": lesson.title,
        "video": lesson.video,
    }
    # content = lesson.content
    # title = lesson.title
    # video = lesson.video

    return render(request, template_name="lesson.html", context=context)

