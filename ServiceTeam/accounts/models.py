from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from PIL import Image as Img
from PIL import ExifTags
from io import BytesIO
from django.core.files import File


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, related_name="main_user", on_delete=models.CASCADE)

    # additional
    job_title = models.CharField(blank=True, max_length=100)
    department = models.CharField(blank=True, max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    employee_no = models.CharField(max_length=256, blank=True, null=True)
    cell_phone = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            if self.profile_pic:
                pilImage = Img.open(BytesIO(self.profile_pic.read()))
                for orientation in ExifTags.TAGS.keys():
                    if ExifTags.TAGS[orientation] == 'Orientation':
                        break
                exif = dict(pilImage._getexif().items())

                if exif[orientation] == 3:
                    pilImage = pilImage.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    pilImage = pilImage.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    pilImage = pilImage.rotate(90, expand=True)

                output = BytesIO()
                pilImage.save(output, format='JPEG', quality=75)
                output.seek(0)
                self.profile_pic = File(output, self.profile_pic.name)

            return super(UserProfileInfo, self).save(*args, **kwargs)
        except:
            return super(UserProfileInfo, self).save(*args, **kwargs)
