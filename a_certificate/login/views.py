
# Create your views here.
#------------------------------------LOGIN-------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        print("USER:", user)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin_dashboard/')   # ✅ correct
            else:
                return redirect('user_dashboard')  # ✅ correct
        
        else:
            return render(request, 'login/login.html', {'error':'invalid'})  # ✅ fixed
    
    return render(request, 'login/login.html')



#------------------------------------user dashboard-------------------------------
from .models import Participant, Certificate
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    user_email = request.user.email   #  user's email

    participants = Participant.objects.filter(email=user_email)

    certificates = Certificate.objects.filter(
        participant__in=participants
    )

    return render(request, 'login/user_dashboard.html', {
        'certificates': certificates
    })

#------------------------------------user dashboard EVENTS-------------------------------
from .models import Participant

@login_required
def events_page(request):
    user_email = request.user.email   # 👈 logged-in user email

    participations = Participant.objects.filter(email=user_email)

    return render(request, 'login/events.html', {
        'participations': participations
    })

#------------------------------------user dashboard CERTIFICATE-------------------------------
from django.contrib.auth.decorators import login_required
from .models import Participant, Certificate

@login_required
def certificates_page(request):
    user_email = request.user.email   # 👈 logged-in user's email

    participants = Participant.objects.filter(email=user_email)

    participations = Certificate.objects.filter(
        participant__in=participants
    )

    return render(request, 'login/certificates.html', {
        'participations': participations
    })


#------------------------------------admin dashboard -------------------------------

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_dashboard(request):
    return render(request, 'login/admin_dashboard.html')

from .models import Event
from django.contrib.admin.views.decorators import staff_member_required


#------------------------------------admin dashboard EVENTS-------------------------------
@staff_member_required
def add_event(request):
    if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        organizer = request.POST.get('organizer')
        certificate_title = request.POST.get('certificate_title')

        Event.objects.create(
            name=name,
            date=date,
            organizer=organizer,
            certificate_title=certificate_title
        )

        return redirect('admin_dashboard')

    return render(request, 'login/add_event.html')



#------------------------------------admin dashboard participant manage-------------------------------

from .models import Participant, Event

def add_participant(request):
    events = Event.objects.all()
    participants = Participant.objects.select_related('event').all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        event_id = request.POST.get('event')
        role = request.POST.get('role')

        # safety check (prevents crash)
        if event_id:
            event = Event.objects.get(id=event_id)

            Participant.objects.create(
                name=name,
                email=email,
                event=event,
                role=role
            )

        return redirect('add_participant')

    return render(request, 'login/add_participant.html', {
        'events': events,
        'participants': participants   # 👈 THIS PREVENTS CRASH
    })



#------------------------------------admin dashboard certificate generation-------------------------------
from .models import Participant, Event

def generate_certificate(request):
    events = Event.objects.all()
    participants = Participant.objects.select_related('event').all()

    if request.method == "POST":
        participant_id = request.POST.get('participant')

        # For now just test flow (no generation yet)
        if participant_id:
            return redirect('generate_certificate')

    return render(request, 'login/generate_certificate.html', {
        'events': events,
        'participants': participants
    })