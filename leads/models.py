from django.db import models



class Agent(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField( max_length=20)


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

