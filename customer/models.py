from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/Customer/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

#model policy_claim
class policy_claim(models.Model):
    mobile_no= models.PositiveIntegerField()
    place=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    policy_name=models.CharField(max_length=200)
    discr=models.CharField(max_length=400)
    customer_id=models.CharField(max_length=200)
   
    def __str__(self):
        return self.place


