from django.db import models

# Create your models here.
class booking(models.Model):  
    name=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField(null='not'),

class HomeHomechoose(models.Model):
    id = models.BigAutoField(primary_key=True)
    where = models.CharField(max_length=100)
    when = models.DateField()

    class Meta:
        managed = False
        db_table = 'home_homechoose'

class HomeEnquiry(models.Model):
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    textarea = models.TextField()

    class Meta:
        managed = False
        db_table = 'home_enquiry'

