from __future__ import unicode_literals
from django.db import models


#===============================================================================
#                                         Create a Model
#===============================================================================
class Lesson(models.Model):
    # --------------------------------------------------------------------------
    #                                                            REQUIRED FIELDS
    # --------------------------------------------------------------------------
    name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=200, blank=False)
    short_description = models.CharField(max_length=250, blank=False)

    # --------------------------------------------------------------------------
    #                                                            OPTIONAL FIELDS
    # --------------------------------------------------------------------------
    description = models.CharField(max_length=500, blank=True, null=False)
    content = models.TextField(blank=True, null=False)
    video = models.CharField(max_length=200, blank=True, null=False)
    # TODO: video will be a Foreing key to a video model later on.

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

