from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        
        "title":"product",
        "heading":"OUR PRODUCT",
        "subheading":'Suitable for your needs'
    }
    return render (request,"product/index.html",context)