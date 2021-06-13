from django.shortcuts import render

def index(request):
    context={
        'title':'Home',
        'heading':'Build and customize your project here',
        'subheading':'Your dificulty is our challanges, byCode.id is always here to make your "software and digital electronic" project come true.',
    }

    return render(request,'index.html',context)