# Teecha 
## A Django App for creating and displaying Online Tutorials

This is a Django Web App for creating classes/tutorials using a 
breadcrumbs approach similar to the way Udacity breaks classes up into 
small byte-sized pieces. 

**NOTE:** This project is at it's very infancy at the moment, it is not 
ready to be used by anyone. 

The structure assumed is as follows: 

A **lesson** is a small byte-sized concept that can be taught in a short 
video or section of tutorial. It should prefereable only cover one 
concept. 

A **module** is a logically coherent set of lessons intended to teach some 
topic. 

It is designed with the assumption that a video will be the primary 
source of information for each individual lesson, and a markdown 
document can be used to suppliment the video. But this is not a 
requirement. You can have a text based lesson with no video at all if 
you like. 

