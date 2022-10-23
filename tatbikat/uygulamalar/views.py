from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied

from tatbikat.mustahdimin.models import Mustahdim, Tarihce, Muvazzaf
from tatbikat.mesanid.models import Fihrist
from tatbikat.mustecirin.models import Tatbik
from tatbikat.esnad.forms import IstirakForm
from .forms import MuvazzafSinupForm
from .mixins import MumtazMixin

from .utils import (
    abonelik_yap_veya_getir, herkobi_yap_veya_getir, fihrist_yap, vazifelerini_tevdi_et,
)


@login_required
def mustahdimin(request):
    context = {
        'mustahdimin': Mustahdim.objects.filter(mustecir=request.user.mustecir)
    }
    return render(request, 'uygulamalar/mustahdimin.html', context)


class YeniMustahdimView(MumtazMixin, CreateView):
    model = Mustahdim
    form_class = MuvazzafSinupForm
    template_name = 'uygulamalar/mustahdim_form.html'

    def form_valid(self, form):
        mustahdim = form.save()
        Tarihce.objects.create(
            email=mustahdim.email,
            mustahdim=mustahdim,
            current_os=self.request.user_agent.os.family,
            current_os_version=self.request.user_agent.os.version,
            current_browser=self.request.user_agent.browser.family,
            current_browser_version=self.request.user_agent.browser.version,
        )
        mustecir = self.request.user.mustecir
        fihrist, oldu = Fihrist.objects.get_or_create(
            mustecir=mustecir,
            isim="Personeller",
            kufl=135,
            faaldir=True,
        )
        muvazzaf = Muvazzaf.objects.create(
            mustecir=mustecir,
            fihrist=fihrist,
            isim=f"{mustahdim.ad} {mustahdim.soyad}",
            kufl=135,            
        )
        mustahdim.mustecir=mustecir
        mustahdim.muvazzaf=muvazzaf
        mustahdim.save()
        return redirect('mustahdimin:profile')

yeni_mustahdim = YeniMustahdimView.as_view()


@login_required
def tatbikati_mustahdim(request, pk):
    if not request.user.mumtaz:
        raise PermissionDenied()

    mustahdim = get_object_or_404(Mustahdim, pk=pk)
    tatbikat = Tatbik.objects.filter(faaldir=True)

    context = {
        'mustahdim': mustahdim,
        "tatbikat": tatbikat
    }

    return render(request, 'uygulamalar/tatbikati_mustahdim.html', context)



@login_required
def tatbik_i_mustahdim(request, pk, sebike):

    if not request.user.mumtaz:
        raise PermissionDenied()
    
    mustahdim = get_object_or_404(Mustahdim, pk=pk)
    tatbik = get_object_or_404(Tatbik, sebike=sebike)

    form = IstirakForm(request.POST or None)

    if form.is_valid():
        mustened = form.cleaned_data.get('mustened')
        if mustened:
            request.user.mustecir.tatbikat.add(tatbik)
            fihrist = fihrist_yap(tatbik, request.user.mustecir)
            istirak = form.save()
            istirak.mustecir = request.user.mustecir
            istirak.hesab = abonelik_yap_veya_getir(tatbik, request.user.mustecir)
            istirak.mahsub = herkobi_yap_veya_getir(request.user.mustecir)
            istirak.save()
            vazifelerini_tevdi_et(mustahdim, tatbik)

        return redirect('uygulamalar:mustahdimin')

    tatbikat = Tatbik.objects.filter(faaldir=True)

    context = {
        "mustahdim": mustahdim,
        "form": form,
        "tatbik": tatbik,
        "tatbikat": tatbikat
    }

    return render(request, 'uygulamalar/tatbik-i_mustahdim.html', context)


