from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lname_prefix = models.CharField(max_length = 60, null = True, blank = True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    user_role = models.CharField(max_length = 60,choices=(('customer','Customer'),('artist','Artist')), default ='Customer')
    street_name = models.CharField(max_length = 60, null = True, blank=True)
    house_number = models.CharField(max_length = 60, null = True, blank=True)
    addition = models.CharField(max_length = 60, null = True, blank=True)
    postcode = models.CharField(max_length = 60, null = True, blank=True)
    city = models.CharField(max_length = 60, null = True, blank=True)
    country = models.CharField(max_length = 60, choices=(('','Country'),('netherlands','The Netherlands'),('usa','USA'),('syria','Syria'),('germany','Germany'),('uk','United Kingdom')),default = 'null', null = True, blank=True)
    language = models.CharField(max_length = 60, choices=(('english','English'),('dutch','Dutch')),default = 'English')
    sign_up_date = models.DateField(("Date"), default=datetime.date.today)
    activated_artist_date = models.DateTimeField(blank=True, null = True)
    active_email = models.BooleanField(default=True)


    def __str__(self):
        return 'User: ' + self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_size = (300,300)
            img.thumbnail(new_size)
            img.save(self.image.path)


class isArtist(models.Model):
    applicant = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    applicant_description = models.TextField(max_length=600)
    artwork_example_image = models.ImageField(upload_to='artwork_example')
    artwork_example_title = models.CharField(max_length = 60)
    artwork_example_description = models.TextField(max_length = 600)
    application_date = models.DateField(("Date"), default=datetime.date.today)

    # delete the image from the DB if object is deleted
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.artwork_example_image.storage, self.artwork_example_image.path
        # Delete the model before the file
        super(isArtist, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)

    def __str__(self):
        return 'Applicant: ' + self.applicant.user.username
