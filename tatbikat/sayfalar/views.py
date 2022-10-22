from django.shortcuts import render


def anasayfa(request):
    context = {}
    return render(request, 'sayfalar/anasayfa.html', context)

