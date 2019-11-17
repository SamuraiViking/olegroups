from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, default="default@stolaf.edu")
    photo = models.URLField(max_length=200, default="")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.email

class Group(models.Model):
    name = models.CharField(max_length=30, default="")
    members = models.ManyToManyField(Person, through="Membership")

    class Meta:
        ordering=['name']
    
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person , on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


