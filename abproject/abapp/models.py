from django.db import models

# Create your models here.
class emp1(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    salary=models.BigIntegerField()
    contact=models.BigIntegerField()
    class Meta:
        db_table="hiii1"

class emp2(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    class Meta:
        db_table="login"
