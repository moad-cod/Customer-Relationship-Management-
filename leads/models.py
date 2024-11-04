from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser  
from django.core.validators import MinValueValidator

# user = get_user_model()

class User(AbstractUser): #this class based on attributes of AbstractUser 
    # cellphone_number = models.CharField(max_length=15) <==> and you can add a knew attribute it does't already exist
    pass
class Lead(models.Model):

    SOURCE_CHOICES = {
        ('YT', 'Youtube'),
        ('Gl', 'Google'),
        ('NL', 'Newsletter'),
    }
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0, validators=[MinValueValidator(0)])  
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
     
    
    def __str__(self):
            return f"{self.first_name} {self.last_name}"
    
class Agent(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.user.email
        