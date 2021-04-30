from django.shortcuts import render


def homepage(request):
    # """
    # renders landing page
    # """
    return render(request, 'home.html', {})
