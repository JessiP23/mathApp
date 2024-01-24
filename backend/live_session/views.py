from django.shortcuts import render, redirect
from .models import SetSession
from .forms import SessionForm
from django.views import View
# Create your views here.
 
class ScheduleSession(View):
    def get(self, request):
        #empty SessionForm form
        form = SessionForm()
        #Render html with SessionForm
        return render(request, 'session/schedule_session.html', {'form': form})

    #process form submission
    def post(self, request):
        #initialize SessionForm from the POST request
        form = SessionForm(request.POST)
        #save session if form is valid
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()

            return redirect('live_session:list_session')
        #if not valid will render html
        else:
            print(request.POST)
            
        return render(request, 'session/schedule_session.html', {'form': form})

class SessionList(View):
    def get(self, request):
        #Display sessions filtered by user
        list_session = SetSession.objects.filter(user=request.user)
        #add sessions in html template
        return render(request, 'session/list_session.html', {'list_session': list_session})

class SessionDetails(View):
    def get(self, request, session_id):
        #Retrieves session with the session_id
        session_number = SetSession.objects.get(pk=session_id)
        return render(request, 'session/session_details.html', {'session_number': session_number})
 