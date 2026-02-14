from django.http import HttpResponse


def archive(request, year, month=None):
    if month == None:
        return HttpResponse(f'<h1>Архив за {year}</h1>')
    else:
        return HttpResponse(f'Архив за {year}.{month}')
