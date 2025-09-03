from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406347424',
        'name': 'Bermulya Anugrah Putra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)