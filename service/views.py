from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Services',
        'heading':'Find Your Custom Porject',
        'subheading':'Get competitive pricing with packages and promo ',
    }
    return render(request,"service/index.html",context)