from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    
  
    c = {}
    c["username"] = request.GET.get('username')
    c["age"] = 40
    c["majors"] = [
        "MIS",
        "ORM",
        "Finance",
        "Marketing",
        "Management",
        "Economics",
        "Accounting",
        "Public Admin",
    ]

    return render(request, "template2.html", c)


def greet_view(request, user=None, a=None):
    
    # one way to define the dictionary
    # d = {}
    # d["username"] = user

    d = {
        "username": user,
        "age": a,
    }

    return render(request, "greet.html", d)
