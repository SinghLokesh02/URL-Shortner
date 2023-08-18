from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Url


# Create your views here.
def index(request):
    if(request.method == "POST"):
        full_url = request.POST['input']
        obj = Url.create(full_url)
        print(full_url)
    
        return render(request,"index.html", {
            'full_url' : obj.full_url,
            'short_url' : request.get_host()+'/'+obj.short_url
        
        })
        
    return render(request,"index.html")


def routeToURL(req,key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect('index')
    # return redirect(req,"index.html")