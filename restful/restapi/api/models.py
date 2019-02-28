from django.db import models

# Create your models here.
class Trip(models.Model):
    trip_id = models.AutoField(max_length=30, primary_key=True)
    driver_name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=15)
    opening_milage = models.CharField(max_length=20)
    closing_milage = models.IntegerField()
    destination = models.IntegerField()
    comments= models.TextField()
    distance=models.IntegerField()
    date= models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.driver_name, self.reg_number, self.opening_milage, self.closing_milage, self.destination, self.comments, self.date)


class Users(models.Model):
    user_id = models.AutoField(max_length=15, primary_key=True)
    user_name = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=256)

    def __str__(self):
        return (self.user_name, self.name, self.user_id)
