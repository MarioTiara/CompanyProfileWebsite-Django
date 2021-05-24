from django.shortcuts import render

def index(request):
    context={
        'title':'byCode.id',
        'heading':'Welcome',
        'subheading':'to our Website',
    }

    return render(request,'index.html',context)