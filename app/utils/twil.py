from twilio.rest import Client
from app.config import settings

client = Client(settings.account_sid, settings.auth_token)

def check_the_phone_line(): 
    # check if any conferences in progress
    in_progress = client.conferences.list(status='in-progress')
    if len(in_progress) >= 1:
        return
    create_create_conference()

def create_create_conference():
    call = client.calls.create(
        to=settings.conference_phone, #conference number
        from_=settings.agent_phone, # agent
        url='http://demo.twilio.com/docs/voice.xml',
        timeout=15
    )


def dial_office_in(conference_sid: str):
    p = client.conferences(conference_sid).participants.create(
            from_=settings.agent_phone, # agent
            to=settings.office_phone, #google number 
            #to='+17372105443', # busy number
            timeout=15,
            end_conference_on_exit=True,
            status_callback='https://5a0a6464.ngrok.io/office_events',
            status_callback_event='ringing',
        )


def dial_me_in(conference_sid: str) -> None:
    """Dials your personal phone number into a conference"""

    p = client.conferences(conference_sid).participants.create(
            from_=settings.agent_phone,
            to=settings.personal_phone,
            end_conference_on_exit=True,
            timeout=15
        )
