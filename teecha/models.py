from __future__ import unicode_literals
from django.db import models


#===============================================================================
#                                         Create a Model
#===============================================================================
class Lesson(models.Model):
    # name is here to make it easier to search for this lesson, and for a
    # more meaningful short descriptor than an ID number
    #
    # TODO: restrict lesson name to not contain any spaces, commas,
    #       forward slashes,colons, semi colons or other chars that
    #       might not filename friendly
    name = models.CharField(max_length=80, blank=False)

    # --------------------------------------------------------------------------
    #                                                               TEXT CONTENT
    # --------------------------------------------------------------------------
    title = models.CharField(max_length=200, blank=False)

    # The actual text content
    content = models.TextField(blank=True, null=False)

    # a publicly visible description
    description = models.TextField(max_length=1024, blank=True, null=False)

    # Description only seen by admin
    hidden_description = models.TextField(max_length=512, blank=True, null=False)

    # --------------------------------------------------------------------------
    #                                                              VIDEO CONTENT
    # --------------------------------------------------------------------------
    # Link to a video (if needed)
    # TODO: video will be a Foreing key to a video model later on.
    video = models.CharField(max_length=200, blank=True, null=False)

    # Set the options available for video service
    LEGAL_VIDEO_SERVICES = (
        ("youtube", "youtube"),
        ("vimeo", "vimeo"),
    )

    video_service = models.CharField(max_length=50,
                                     choices=LEGAL_VIDEO_SERVICES,
                                     blank=False, null=False,
                                     default="youtube")

    # --------------------------------------------------------------------------
    #                                                           DATE TIME STAMPS
    # --------------------------------------------------------------------------
    # Publication date
    published = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Time last updates (automatically populated)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    # --------------------------------------------------------------------------
    #                                     FIELDS TO BE INPLEMENTED IN THE FUTURE
    # --------------------------------------------------------------------------
    # tags = TODO: add tags to the lesson

    # hash = TODO: use this to store a hash of a file that we will automatically
    #              populate content from if the file has been updated.

    # assets = TODO: this will be for things like images, etc that appear in the
    #                content. Is it ieven necessary?

    # downloadables = TODO: this will be a many to many linking to File Models
    #                       that contain files relating to the lesson, eg code.


    # links = TODO: maybe redundant. it is intended to be links to external
    #               sources, with short and long description. But mayube this
    #               is already well served in the content section.

    # instructor = TODO: add link to a User Model for the instructor.


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']  # Specifies the default ordering of Lesson objects
                             # when listed. Here we say they should be ordered
                             # by their name. (not their id


#===============================================================================
#                                                                         MODULE
#===============================================================================
class Module(models.Model):
    name = models.CharField(max_length=80, blank=False)
    title = models.CharField(max_length=200, blank=False)

    # Lessons need to be ordered in a specific way, so they will be liked using
    # a 'through' Model
    lessons = models.ManyToManyField(
            Lesson,
            through='ModuleLesson',
            related_name='lesson',
    )

    # a publicly visible description
    description = models.TextField(max_length=1024, blank=True, null=False)

    # Description only seen by admin
    hidden_description = models.TextField(max_length=512, blank=True,
                                          null=False)

    # --------------------------------------------------------------------------
    #                                                           DATE TIME STAMPS
    # --------------------------------------------------------------------------
    # Publication date
    published = models.DateTimeField(auto_now=False, auto_now_add=False)

    # Time last updates (automatically populated)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


#===============================================================================
#                                                                  MODULE LESSON
#===============================================================================
class ModuleLesson(models.Model):
    """ This is a "Through" model so we can order Lessons """
    module = models.ForeignKey(Module)
    lesson = models.ForeignKey(Lesson)
    order = models.IntegerField(help_text=u"What order to display this lesson in the Module")

    class Meta:
        ordering = ["order",]

    def __str__(self):
        return "{mod} [{i}] {lesson}".format(mod=self.module.name,
                                             lesson=self.lesson.name,
                                             i=self.order)

    def __unicode__(self):
        return self.__str__()

