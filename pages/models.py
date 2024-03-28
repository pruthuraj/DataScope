from djongo import models

# Create your models here.
class TestUser(models.Model):
    userFirstName = models.CharField(max_length=55)
    userLastName = models.CharField(max_length=55)
    userEmail = models.EmailField()
    userNumber = models.IntegerField()
    usergander = models.CharField(max_length=50)
    userDOB = models.CharField(max_length=11)
    userName = models.CharField(max_length=55)
    userPassword = models.CharField(max_length=20)


