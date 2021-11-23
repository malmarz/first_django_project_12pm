from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view(request):
    print("request:", dir(request))
    return HttpResponse("""
    <html>
     <head></head>
     <body>
     Hello World
     This is my first
      HTML page
     </body>
    </html>
    """)
