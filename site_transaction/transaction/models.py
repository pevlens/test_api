from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="users")

    def __str__(self) -> str:
        return self.name   

    class Meta: 
        unique_together = ['user', 'name']

class TransactionsUser(models.Model):
    summ = models.FloatField(default = 0)
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now =  True)
    organisations = models.CharField(max_length=100, blank=False, null=False)
    about = models.TextField(blank=True, null=True)
    cat = models.ForeignKey("Category", on_delete = models.SET_NULL,  blank=True, null=True, related_name="categorys")
    person = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True, related_name="person")



