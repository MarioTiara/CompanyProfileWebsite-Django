from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "title":"Blog",
        "heading":"byCode.id Blog",
        'Subheading':'We provide qualified article',
    }
    return render (request,"blog/index.html",context)