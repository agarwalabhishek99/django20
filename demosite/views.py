from django.http import HttpResponse

def index(request):
    return HttpResponse(
        "<h1><a href='https://www.google.com' target='_blank'>Open Google</a></h1>"
        "<h1><a href='https://www.yahoo.com' target='_blank'>Open Yahoo</a></h1>"
        "<h1><a href='https://www.youtube.com' target='_blank'>Open Youtube</a></h1>"
        "<h1><a href='https://www.facebook.com' target='_blank'>Open Facebook</a></h1>"
    )

def Home(request):
    return HttpResponse('<h1>Home Page</h1>')