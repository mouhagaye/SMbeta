from django.shortcuts import render, redirect
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import *

def index(request):
    return render(request, 'main/index.html')


def new_meeting(request):
    if request.method == 'POST':
        meetingForm = MeetingForm(request.POST)
        if meetingForm.is_valid():
            meeting = meetingForm.save()
            print('------------------------------')
            print(meeting.points)
            print(meetingForm.is_valid())
            # return render(request, )
            return new_group(request=request, meeting=meeting)
        else:
            return render(request, 'main/dashboard_meeting.html', {'meeting': meetingForm})

    meetingForm = MeetingForm()
    return render(request, 'main/dashboard_meeting.html', {'meeting': meetingForm})

    pass


def new_group(request, meeting=''):



    invitees = list(meeting.members.all())

    html_message = render_to_string('main/mail_invitation.html', {'meeting': meeting})

    existing_users = User.objects.all()

    # for invitee in invitees:
    send_mail(
        subject='Invitation SmartMeeting',
        message=strip_tags(html_message),
        from_email='mdiakhate1297@gmail.com',
        recipient_list=[invitee.email for invitee in invitees if invitee != request.user],
        html_message=html_message
    )

    return redirect('groups')

@login_required(redirect_field_name='login')
def dashboard(request):
    users = User.objects.all()
    meetings = Meeting.objects.all()

    return render(request, 'main/dashboard.html', {'users':users, 'meetings':meetings , 'page_title':'DASHBOARD'})

@login_required(redirect_field_name='login')
def meeting(request, id=False):
    if(id):
        meeting = Meeting.objects.get(pk=id)
        return render(request, 'main/dashboard_meeting_detail.html', {'meeting': meeting, 'page_title': meeting.title})
    meetings = Meeting.objects.all()
    return render(request, 'main/dashboard_meeting.html', {'meetings': meetings, 'page_title':'MEETINGS'})

def calendar(request):
    return render(request, 'main/calendar.html', {'page_title':'CALENDAR'})

@login_required(redirect_field_name='login')
def profile(request, id=False):
    if(id):
        user = User.objects.get(pk=id)
        return render(request, 'main/profile.html', {'user': user})
    return render(request, 'main/profile.html')


    # print('--------------------------------------------')
    # print(invitees)
    # print('--------------------------------------------')
    # print(request.user)
    # print('--------------------------------------------')


def transcript(request):
    return render(request, 'main/transcript.html', {'page_title': 'LIVE MEETING TRANSCRIPTION'})