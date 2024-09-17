from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.db.models import F


# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    runtime = models.CharField(max_length=7)
    description = models.TextField()
    rating = models.FloatField()
    launch_date = models.DateField()
    Image=models.ImageField(default='defaultmovie.jpeg', upload_to='movie_img')
    id = models.AutoField(primary_key=True)
    price=models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.movie.title}"
    
# Wallet model
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Wallet"

    def deduct_funds(self, amount):
        if self.balance >= amount:
            self.balance = F('balance') - amount
            self.save()
            return True
        return False