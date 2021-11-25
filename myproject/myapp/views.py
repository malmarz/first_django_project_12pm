from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("request:", dir(request))
    name = "mohammad"

    return HttpResponse(f"""
    <html>
     <head></head>
     <body>
     <h1>Hello {name}</h1>
    <h2>
     This is my first
     </h2>
      HTML page
     </body>
    </html>
    """)
