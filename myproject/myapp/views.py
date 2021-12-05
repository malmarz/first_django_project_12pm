from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("request:", request.GET["pwd"])
  
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
