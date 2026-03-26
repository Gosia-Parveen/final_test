from django.contrib import admin
from .models import Event, CertificateTemplate, Participant, Certificate

admin.site.register(Event)
admin.site.register(CertificateTemplate)
admin.site.register(Participant)
admin.site.register(Certificate)