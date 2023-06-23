from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Dsensor
from django.forms.models import model_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt
import hashlib
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import User
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import face_recognition


from .models import *
from .utils import Calendar
from .forms import EventForm

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})



def main(request):
    data = Dsensor.objects.all()
    data_list = [entry for entry in data]
    last_data=data_list[-12:]

    return render(request, 'main.html', {'last_data': last_data})


def login(request):
    user_data = User.objects.all()
    user_list = [entry for entry in user_data]
    last_user=user_list[-1] if user_data else None

    return render(request,'login.html', {'user_data':last_user})




def home(request):
    data = Dsensor.objects.all()
    data_list = [entry for entry in data]
    last_data=data_list[-12:]

    return render(request, 'home.html', {'last_data': last_data})

def cam(request):
    context={}
    
    return render(request, "cam.html",context)
    
def user(request):
    user_data = User.objects.all()
    user_list = [entry for entry in user_data]
    last_user=user_list[-1] if user_data else None

    return render(request, 'user.html', {'user_data':last_user})

@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")

@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")




