from django.shortcuts import render

def schedule (request):
    return render(request, 'estab_app/schedule.html')

