from django.db import models

class exp1(models.Model):
    class Meta:
        db_table = 'exp1'
    geneName   = models.CharField(max_length=50)
    countArray = models.CharField(max_length=100)
    def __str__(self): 
        return self.geneName

class exp2(models.Model):
    class Meta:
        db_table = 'exp2'
    geneName   = models.CharField(max_length=50)
    countArray = models.CharField(max_length=100)
    def __str__(self):
        return self.geneName

# Create your models here.
