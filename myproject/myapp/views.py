from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("request:", dir(request))
    name = "mohammad"
  
    c = {}
    c["username"] = name
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
