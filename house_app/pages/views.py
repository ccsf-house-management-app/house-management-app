from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {})

# Create your views here.
