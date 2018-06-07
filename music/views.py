from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>This is a music app homepage</h1>')

def detail(request, album_id):
    return HttpResponse('<h1>Details for album id ' + str(album_id) + ' </h1>')