
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    pass

    def __str__(self):
        return self.username

    
class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000,null=True,default="",blank=True)
    publication_date=models.DateField()
    url=models.URLField(blank=True ,default="https://artsmidnorthcoast.com/wp-content/uploads/2014/05/no-image-available-icon-6.png")
    genre=models.CharField(max_length=50,blank=True)
    author=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    rating = models.PositiveIntegerField(default=0)
    is_in_cart=models.ManyToManyField(User,related_name="cart",blank=True)

    def __str__(self):
        return str(self.title)
    
    @property
    def in_cart(self,user):
        return user.cart.filter(pk=self.pk)
     




