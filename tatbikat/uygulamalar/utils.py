from tatbikat.mesanid.models import Fihrist
from tatbikat.mustahdimin.models import Mesuliyet, Salahiyet, Vazife
from tatbikat.mustecirin.models import Tatbik

def fihrist_yap(tatbik, mustecir):
    fihrist, oldu  = Fihrist.objects.get_or_create(
        mustecir=mustecir,
        isim=tatbik.isim,
        sebike=tatbik.sebike,
        meshur_isim=tatbik.meshur_isim,
        sened_isim=tatbik.sened_isim,
        mesuliyet_isim=tatbik.mesuliyet_isim,
        salahiyet_isim=tatbik.salahiyet_isim,
        kufl=tatbik.miftah,
        faaldir=True
    )
    return fihrist


def herkobi_fihristi_yap_veya_getir(mustecir):
    fihrist, oldu = Fihrist.objects.get_or_create(
        mustecir=mustecir,
        isim="Herkobi A.Ş.",
        sebike="herkobi-a-s",
        sened_isim="Herkobi A.Ş.",
        mesuliyet_isim="Herkobi A.Ş.",
        salahiyet_isim="Herkobi A.Ş.",
        kufl=323,
        faaldir=True
    )
    return fihrist


def herkobi_yap_veya_getir(mustecir):
    herkobi, oldu = Herkobi.objects.get_or_create(
        mustecir=mustecir,
        fihrist=herkobi_fihristi_yap_veya_getir(mustecir),
        isim="Herkobi A.Ş.",
        kufl=323,
    )
    return herkobi





def abonelik_yap_veya_getir(tatbik, mustecir):
    herkobi, oldu = Abonelik.objects.get_or_create(
        mustecir=mustecir,
        fihrist=fihrist_yap(tatbik, mustecir),
        isim=tatbik.meshur_isim,
        kufl=tatbik.miftah,
    )
    return herkobi

def mesuliyet_yap(fihrist):
    mesuliyet = Mesuliyet.objects.create(
        mustecir=fihrist.mustecir,
        isim=fihrist.meshur_isim,
        fihrist=fihrist,
    )
    return mesuliyet

def salahiyet_yap(miftah, mesuliyet):
    tatbik = Tatbik.objects.get(miftah=miftah)
    uygulama = fihrist_yap(tatbik, mesuliyet.mustecir)
    salahiyet = Salahiyet.objects.create(
        mustecir=mesuliyet.mustecir,
        isim=tatbik.salahiyet_isim,
        fihrist=uygulama,
        mesuliyet=mesuliyet
    )
    return salahiyet

def vazife_yap(miftah, salahiyet):
    tatbik = Tatbik.objects.get(miftah=miftah)
    uygulama = fihrist_yap(tatbik, salahiyet.mustecir)
    vazife = Vazife.objects.create(
        mustecir=salahiyet.mustecir,
        isim=salahiyet.mesuliyet.isim,
        fihrist=uygulama,
        salahiyet=salahiyet,
    )
    return vazife


def vazifelerini_tevdi_et(mustahdim, tatbik):
    mustecir = mustahdim.mustecir
    fihrist = fihrist_yap(tatbik, mustecir)
    mesuliyet = mesuliyet_yap(fihrist)
    for m in tatbik.teallukat.split(", "):
        salahiyet = salahiyet_yap(int(m), mesuliyet)
        vazife_yap(salahiyet)
    
    mustahdim.mesuliyetler.add(mesuliyet)

    return True