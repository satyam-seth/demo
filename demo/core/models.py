from django.db import models

# Create your models here.

class Org(models.Model):
    name=models.CharField(max_length=100,unique=True)
    registered_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Emp(models.Model):
    name=models.CharField(max_length=100)
    org=models.ForeignKey(Org, on_delete=models.CASCADE)
    registered_on=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name