from django.shortcuts import render, HttpResponse
# ==============================================================================
#                                                                          INDEX
# ==============================================================================
def index(request):
    return HttpResponse("This is the index for teecha")


# Create your views here.
