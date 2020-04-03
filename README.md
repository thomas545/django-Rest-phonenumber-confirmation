# django-Rest-phonenumber-confirmation
- A Django library for phone number confirmation with twilio with phone number validation 

### Quickstart
For installing django-drf-auth, just run this command in your shell

```
pip install django-Rest-phonenumber-confirmation
```

### settings
```
INSTALLED_APPS = (
    # ...
    
    'rest_framework',
    'phonenumber_field',
    'phonenumber_confirmation',
)

UNIQUE_PHONE_NUMBER = True
PHONE_CONFIRMATION_EXPIRE_MINUTES = 15

PHONENUMBER_DEFAULT_REGION = "Your region code"
PHONENUMBER_DB_FORMAT = ( 'INTERNATIONAL' or 'NATIONAL' )

# YOUR TWILIO INFORMATION
TWILIO_ACCOUNT_SID = 'xxxxxxxxxxx'
TWILIO_AUTH_TOKEN = 'xxxxxxxxxxx'
TWILIO_FROM_NUMBER = 'xxxxxxxxxxx'

```

### Dont forget do 
```
python manage.py migrate
```

### URLS

```
urlpatterns = [
    # ...
    path('phone-confirm/api/', include('phonenumber_confirmation.urls')),
]
```

#### API Endpoints: 

##### CREATE PHONE NUMBER AND SEND CONFIRMATION
Method: `POST`  
Endpoint: `/phone-number/sent/`  
Payload:  
`{  
    "phone": "PHONE NUMBER"
}`

##### CONFIRM PHON NUMBER 
Method: `POST`  
Endpoint: `/phone-number/confirmation/`  
Payload:  
`{  
    "pin": "PIN"
}`

##### RESEND CONFIRMATION TO PHON NUMBER 
Method: `POST`  
Endpoint: `/resend/<int:phonenumber_id>/confirmation/`  
Param : phonenumber_id = phone number object id
