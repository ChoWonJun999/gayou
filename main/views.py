from django.shortcuts import render


def main_page(request):
    numbers = list(range(5))
    return render(request, 'main/main.jsp', {'numbers': numbers})
