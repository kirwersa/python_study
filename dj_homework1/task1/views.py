from django.http import HttpResponse


def calc(request, a, b, op):
    if op == 'add':
        return HttpResponse(f"<h2>{a} + {b} = {a+b}<h2>")
    if op == 'mul':
        return HttpResponse(f"<h2>{a} * {b} = {a*b}<h2>")
    if op == 'sub':
        return HttpResponse(f"<h2>{a} - {b} = {a-b}<h2>")
    if op == 'div':
        if b != 0:
            return HttpResponse(f"<h2>{a} / {b} = {a/b}<h2>")
        else:
            return HttpResponse(f"<h2>Делить на ноль нельзя<h2>")
    else:
        return HttpResponse(f"<h2>Неизвестная операция<h2>")
