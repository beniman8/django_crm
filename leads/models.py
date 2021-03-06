from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

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
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True,blank=True)
    #This means Every lead will have its own agent
    agent = models.ForeignKey("Agent",null=True,blank=True,on_delete=models.SET_NULL)
    category = models.ForeignKey("Category",related_name="leads", null=True,blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField( max_length=20)
    email= models.EmailField()

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    #every agent has one user
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
        

def post_user_created_signal(sender,instance,created,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    
post_save.connect(post_user_created_signal,sender=User)