from django.shortcuts import render, HttpResponse
from django import template
import markdown
from .models import Lesson, Module, ModuleLesson

register = template.Library()
main_site_template_dir = "main"  # relative to the root static directory /static


# ==============================================================================
#                                                                    MARKDOWNIFY
# ==============================================================================
@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    extension_configs = {
        'markdown.extensions.codehilite':
            {
                'noclasses': True,
                'use_pygments': True,
                'linenums': False,
                'guess_lang': False
            }
    }
    return markdown.markdown(text, extensions=['markdown.extensions.tables',
                                               'markdown.extensions.fenced_code',
                                               'markdown.extensions.codehilite',
                                               'markdown.extensions.toc'],
                             extension_configs=extension_configs)


# ==============================================================================
#                                                                FIX LESSON URLS
# ==============================================================================
def fix_lesson_urls(content, lesson_name):
    return content.replace("LESSON_IMG_DIR", lesson_name)


# ==============================================================================
#                                                                          INDEX
# ==============================================================================
def index(request):
    context = {
        "modules": Module.objects.all(),
        "main_site_template_dir": main_site_template_dir,
    }

    return render(request, template_name="teecha/index.html", context=context)


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
        "main_site_template_dir": main_site_template_dir,
    }
    # content = lesson.content
    # title = lesson.title
    # video = lesson.video

    return render(request, template_name="teecha/lesson.html", context=context)


# ==============================================================================
#                                                                         MODULE
# ==============================================================================
def module(request, name):
    # TODO: perform error checking to make sure module is a valid lesson id.
    #       eg, it must be an integer.
    module = Module.objects.get(name=name)

    context = {
        "title": module.title,
        "lessons": module.lessons.all().order_by("modulelesson"),
        "description": module.description,
        "module": module,
        "main_site_template_dir": main_site_template_dir,

    }

    return render(request, template_name="teecha/module.html", context=context)


# ==============================================================================
#                                                                  MODULE_LESSON
# ==============================================================================
def module_lesson(request, module, lesson):
    # TODO: perform error checking to make sure module name and lesson name are
    #       valid and exist.
    module = Module.objects.get(name=module)
    lessons = module.lessons.all().order_by("modulelesson__order")
    lesson = module.lessons.get(name=lesson)
    lesson_num = lesson.modulelesson_set.get(module=module).order # assuming 1 indexing

    # TODO: enforce responsive images.
    # TODO: make video responsive

    content = markdownify(lesson.content)
    content = fix_lesson_urls(content, "/static/teecha/img")
    context = {
        "module_name": module.name,
        "module_title": module.title,
        "lesson_num": lesson_num,
        "content": content,
        "title": lesson.title,
        "video": lesson.video,
        "lessons": lessons,
        "num_lessons": len(lessons),
        "lesson_id":lesson.id,
        "next_lesson_name": lessons[lesson_num] if (lesson_num < len(lessons)) else None,
        "previous_lesson_name": lessons[lesson_num - 2] if (lesson_num > 1) else None,
        "main_site_template_dir": main_site_template_dir,

    }

    return render(request, template_name="teecha/module_lesson.html", context=context)

