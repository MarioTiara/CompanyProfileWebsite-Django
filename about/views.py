from django.shortcuts import render

# Create your views here.

def index(request):
    
    context={
        'title':'About',
        'heading':'Welcome',
        'subheading':'byCode.id',
    }
    return render (request,'about/index.html',context)
