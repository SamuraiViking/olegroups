from django.db import models

# Create your models here.
class Group(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering=['title']
    
    def __str__(self):
        return self.title


class Member(models.Model):
    display_name = models.CharField(max_length=50)
    groups = models.ManyToManyField(Group)

    class Meta:
        ordering = ['display_name']

    def __str__(self):
        return self.display_name