import random
from django.shortcuts import redirect, render
from allauth.account.forms import LoginForm
from django.core.mail import send_mail
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from tatbikat.mustahdimin.forms import MustecirForm, TarihceForm


from .models import (
    Tarihce,
)

def custom_login(request):
    context = {
        'current_os': request.user_agent.os.family,
        'current_os_version': request.user_agent.os.version,
        'current_browser': request.user_agent.browser.family,
        'current_browser_version': request.user_agent.browser.version
    }
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        email = request.POST.get('login')
        history = Tarihce.objects.filter(email=email).last()
        user = history.mustahdim
        history_qs = Tarihce.objects.filter(
            mustahdim=user,
            current_os=context['current_os'],
            current_os_version=context['current_os_version'],
            current_browser=context['current_browser'],
            current_browser_version=context['current_browser_version'],
        )
        last_history = Tarihce.objects.filter(
            mustahdim=user,
        ).last()
        if not history_qs.exists() or not last_history.logged_in_at == history_qs.last().logged_in_at:
            otp = str(random.randint(100000 , 999999))
            request.session['email'] = email
            current_history = Tarihce.objects.create(
                mustahdim=user,
                current_os=context['current_os'],
                current_os_version=context['current_os_version'],
                current_browser=context['current_browser'],
                current_browser_version=context['current_browser_version'],
                otp=otp
            )
            send_mail(
                'Herkobi Kullanıcı Doğrulama',
                f"""İşletim Sistemi: {context['current_os']} {context['current_os_version']} \n 
                Tarayıcı: {context['current_browser']} {context['current_browser_version']}. \n
                Yukarıdaki cihazla giriş yapabilmeniz için doğrulama kodu: {otp}
                """,
                'necipmuzaffer@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('mustahdimin:otp')
        Tarihce.objects.create(
            mustahdim=user,
            current_os=context['current_os'],
            current_os_version=context['current_os_version'],
            current_browser=context['current_browser'],
            current_browser_version=context['current_browser_version']
        )
        login(request, user)
        return redirect('mustahdimin:profile')
    context['form'] = form
    return render(request, 'account/login.html', context)


def otp(request):
    context = {}
    history = Tarihce.objects.filter(email=request.session["email"]).last()
    form = TarihceForm(request.POST or None)
    if form.is_valid():
        otp = request.POST.get('otp')
        if otp == history.otp:
            user=history.mustahdim
            login(request , user)
            return redirect('mustahdimin:profile')
        else:
            context = {'message' : 'Doğrulama kodunu hatalı girdiniz. Lütfen tekrar deneyiniz.' , 'class' : 'danger'}
            return render(request, 'account/otp.html', context)
    context["form"] = form
    return render(request, 'account/otp.html', context)


@login_required
def profile(request):

    context={}

    if not request.user.mustecir:
        if not request.user.mumtaz:
            return render(request, 'mustahdimin/sirketsiz.html')
        form = MustecirForm(request.POST or None)
        if form.is_valid():
            kiraci = form.save()
            user = request.user
            user.mustecir=kiraci
            user.save()
            return redirect('mustahdimin:profile')

        context["form"] = form
        return render(request, 'account/tenant.html', context)
    
    if len(request.user.mesuliyetler.all()) <= 0:

        return redirect('ruyet:mustahdimin')

    return render(request, 'ruyet/serlevha.html', context)

