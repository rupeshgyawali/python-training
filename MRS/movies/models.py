from django.db import models

# def post_image(instance,filename):
#     return f'movies/poster/{filename}'

# Create your models here.
# class Gener(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__():

class Movie(models.Model):
    title = models.CharField(max_length=200)
    gener = models.CharField()
    description = models.TextField()
    trailer = models.URLField(null=True, blank=True)
    rating = models.CharField(max_length=1, choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),], null=True, blank=True)
    poster = models.ImageField(upload_to='images', default='default.png')

    def __str__(self):
        return self.title