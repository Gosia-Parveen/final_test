from django.db import models

# 🔹 EVENT
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    organizer = models.CharField(max_length=200)
    certificate_title = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# 🔹 TEMPLATE
class CertificateTemplate(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    template_image = models.ImageField(upload_to='templates/')

    name_x = models.IntegerField()
    name_y = models.IntegerField()

    event_x = models.IntegerField()
    event_y = models.IntegerField()

    date_x = models.IntegerField()
    date_y = models.IntegerField()

    position_x = models.IntegerField(null=True, blank=True)
    position_y = models.IntegerField(null=True, blank=True)


# 🔹 PARTICIPANT
class Participant(models.Model):
    ROLE_CHOICES = [
        ('Participant', 'Participant'),
        ('Winner', 'Winner'),
        ('Organizer', 'Organizer'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


# 🔹 CERTIFICATE
class Certificate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    file = models.FileField(upload_to='certificates/')
    created_at = models.DateTimeField(auto_now_add=True)