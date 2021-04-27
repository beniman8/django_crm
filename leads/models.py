from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):

    # SOURCE_CHOICES = (
    #     ('Yahoo','Yahoo'),
    #     ('Bing','Bing'),
    #     ('GitHub','GitHub'),
    # )

    first_name=models.CharField(max_length=20)
    last_name = models.CharField( max_length=20)
    age = models.IntegerField(default=0)

    # phoned= models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=50)

    # profile_pic = models.ImageField(blank=true,null=True)
    # documents=models.FileField()

    #This means Every lead will have its own agent
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    #every agent has one user
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    