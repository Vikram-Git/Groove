
from django.contrib.auth.models import models, User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    location = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=12, blank=True, null=True)
    picture = models.ImageField(upload_to='profile-pictures/', blank=True, null=True)

    def __str__(self):
        return '%s'%(self.user)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)