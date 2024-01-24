from django.shortcuts import render, redirect
from .models import SetSession
from .forms import SessionForm
from django.views import View
from django.core.mail import send_mail
from django.urls import reverse
# Create your views here.
 
class ScheduleSession(View):
    def get(self, request):
        form = SessionForm()
        return render(request, 'session/schedule_session.html', {'form': form})

    def post(self, request):
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()

            return redirect('live_session:list_session')
        
        else:
            print(request.POST)
            
        return render(request, 'session/schedule_session.html', {'form': form})

class SessionList(View):
    def get(self, request):
        list_session = SetSession.objects.filter(user=request.user)
        return render(request, 'session/list_session.html', {'list_session': list_session})

class SessionDetails(View):
    def get(self, request, session_id):
        session_number = SetSession.objects.get(pk=session_id)
        return render(request, 'session/session_details.html', {'session_number': session_number})
