from tatbikat.mesanid.models import Fihrist

def fihrist_getir(miftah):
    fihrist_qs = Fihrist.objects.filter(kufl=miftah)
    if fihrist_qs.exists:
        return fihrist_qs.first()
    return None