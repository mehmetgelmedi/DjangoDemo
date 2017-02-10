from django.shortcuts import render
from django.utils import timezone
from webblog.models import Haber

# Create your views here.

def layout(request):
	haberler=Haber.objects.all().filter().order_by('-id')
	return render(request,'webblog/haber.html',{'haberler':haberler})
