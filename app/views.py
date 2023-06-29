from django.shortcuts import render
from app.models import *
from django.db.models.functions import *
from django.db.models import Q
# Create your views here.

def display_topic(request):
    topics = Topic.objects.all()
    
    d = {'topics': topics}
    return render(request,'dt.html',d)

def display_webpage(request):

    # webpages = Webpage.objects.all()

    d = {'webpages': webpages}
    return render(request,'dw.html',d)


def display_ar(request):
    ar = AccessRecord.objects.all()
    
    
    d = {'ar': ar}
    return render(request,'dar.html',d)

def display_all(request):
    
    topics = Topic.objects.all()
    webpages = Webpage.objects.all()
    ar = AccessRecord.objects.all()
    
    d = {'topics': topics, 'webpages': webpages, 'ar': ar}
    
    return render(request,'dall.html',d)


def update_webpage(request):
    
    # webpages=Webpage.objects.all()

    #* update method:-
    #*-------------------------

    # Webpage.objects.filter(name='Dhoni').update(url='https://Mahendra.in')   ## one row satisfy 1 row updated
    # Webpage.objects.filter(topic_name='Cricket').update(url='https://IndianTeam.in')    ## multiple row satisfy multiple row updated
    # Webpage.objects.filter(topic_name='Wwe').update(url='https://wweallstar.in')     ## multiple row satisfy multiple row updated
    # Webpage.objects.filter(name='dhoni MSD').update(url='https://MSD.in')       ## no row satisfy so it will not update anything

    # #Webpage.objects.filter(name='dhoni').update(topic_name='BCCI Cricket')  ## FOREIGN KEY constraint failed (we should give the << value >>which is present in parent table)
    # Webpage.objects.filter(name='dhoni').update(topic_name='Rugby')    ## value is present in parent table so it will updated



    #* update_or_create method:-
    #*-----------------------------

    # Webpage.objects.update_or_create(name='Pqr',defaults={'url':'http://pqr.com'}) ## Error
    
    # Webpage.objects.update_or_create(topic_name='Football',defaults={'url':'http://football.com'}) 
    # Webpage.objects.update_or_create(name='Abc',defaults={'url':'http://hello.com'})

    # CTO=Topic.objects.get(topic_name='Cricket')
    
    # Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    # Webpage.objects.update_or_create(name='Virat',defaults={'topic_name':CTO,'url':'http://pandya.com'})
    
    webpages=Webpage.objects.all()
    
    d = {'webpages': webpages}
    return render(request,'dw.html',d)

def delete_webpage(request):
    # Webpage.objects.filter(name='Xyz').delete()
    # Webpage.objects.filter(name='Dhoni').delete()

    # Webpage.objects.all().delete()
    
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'dw.html',d)
    