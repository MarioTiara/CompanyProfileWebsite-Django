from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Portofolio',
        'heading':'OURS PORTOFOLIO',
        'subheading':'We develope Web, Android, Artificial Intelligence System and Digital Electronik Devices',
    }
    return render(request,"portofolio/index.html",context)