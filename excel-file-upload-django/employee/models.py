from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    application = models.CharField(max_length=100)  
    valuation = models.CharField(max_length=15) 
    budget = models.CharField(max_length=15,null=True) 

    def __str__(self):
        return "%s " %(self.application) 
    class Meta:  
        db_table = "employee"  