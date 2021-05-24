from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'title':'About',
        'heading':'byCode.Id',
        'tagline':'Digital Electronic and Software Developer',
    }
    return render(request,"about/index.html",context)
