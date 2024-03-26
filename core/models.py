from django.db import models

# Create your models here.


class CrudApp(models.Model):
    name = models.CharField(max_length= 70,blank=False,null=False)
    email = models.EmailField(max_length= 100,blank=False,null=False)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length= 25, default="male",blank=False,null=False)
   
    def __str__(self):
        
        return self.name