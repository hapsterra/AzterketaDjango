from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import Pertsona, KotxeaPertsona, Kotxea


# Create your views here.


def pertsonakIkusi(request):
  nirePertsonak = Pertsona.objects.all().values()
  template = loader.get_template('pertsonak.html')
  context = {
    'nirePertsonak': nirePertsonak,
  }
  return HttpResponse(template.render(context, request))

def alokairuakIkusi(request):
  nireAlokairuak = KotxeaPertsona.objects.all()
  template = loader.get_template('alokairuak.html')
  context = {
    'nireAlokairuak': nireAlokairuak,
  }
  return HttpResponse(template.render(context, request))

def kotxeakIkusi(request):
  nireKotxeak = Kotxea.objects.all()
  template = loader.get_template('kotxeak.html')
  context = {
    'nireKotxeak': nireKotxeak,
  }
  return HttpResponse(template.render(context, request))

def deletePertsona(request, id):
  pertsona = Pertsona.objects.get(id=id)
  pertsona.delete()
  return HttpResponseRedirect(reverse('pertsonakIkusi'))

def deleteAlokairu(request, id):
  alokairu = KotxeaPertsona.objects.get(id=id)
  alokairu.delete()
  return HttpResponseRedirect(reverse('alokairuakIkusi'))

def deleteKotxea(request, id):
  kotxea = Kotxea.objects.get(id=id)
  kotxea.delete()
  return HttpResponseRedirect(reverse('kotxeakIkusi'))

def addPertsona(request):
  template = loader.get_template('pertsonaSartu.html')
  return HttpResponse(template.render({}, request))

def addKotxea(request):
  template = loader.get_template('kotxeakSartu.html')
  return HttpResponse(template.render({}, request))

def addAlokairua(request):
  nirePertsonak = Pertsona.objects.all().values()
  nireKotxeak = Kotxea.objects.all()
  context = {
    'nireKotxeak': nireKotxeak,
    'nirePertsonak':nirePertsonak
  }
  template = loader.get_template('alokairuaSartu.html')
  return HttpResponse(template.render(context, request))


def addrecordAlokairua(request):

  pertsonak = Pertsona.objects.all()
  kotxeak = Kotxea.objects.all()
  for x in pertsonak:
    if request.POST['dniPertsona']==x.dni:
      dn = x

  for y in kotxeak:
      if request.POST['matrikula']==y.matrikula:
        mat=y

  da = request.POST['alokairuData']
  alokairu = KotxeaPertsona(dniPertsona=dn, matrikula=mat,alokairuData=da)
  alokairu.save()
  return HttpResponseRedirect(reverse('alokairuakIkusi'))


def addrecordKotxea(request):
  ma =request.POST['matrikula']
  mar = request.POST['marka']
  mod = request.POST['modeloa']
  ur =request.POST['urtea']
  kotxea = Kotxea(matrikula=ma, marka=mar,modeloa=mod,urtea=ur)
  kotxea.save()
  return HttpResponseRedirect(reverse('kotxeakIkusi'))


def addrecordPertsona(request):
  d =request.POST['dni']
  iz = request.POST['izena']
  ab = request.POST['abizena']
  ja =request.POST['jaiotzeData']
  pertsona = Pertsona(dni=d, izena=iz,abizena=ab,jaiotzeData=ja)
  pertsona.save()
  return HttpResponseRedirect(reverse('pertsonakIkusi'))


