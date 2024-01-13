from django.db import models


class Member(models.Model):
    pan_number = models.CharField(
        max_length=10, unique=True, help_text='Enter PAN number')
    name = models.CharField(max_length=255, help_text='Enter member name')
    status_member = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Absen(models.Model):
    member = models.ForeignKey(Member(), on_delete=models.CASCADE)
    amal = models.PositiveBigIntegerField(default=0)
    jam_absen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.member)
