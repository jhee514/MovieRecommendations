from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    audience = models.IntegerField()
    open_data = models.DateField(auto_now=False, auto_now_add=False)
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=50)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return reverse("cinema:movie_detail", kwargs={"movie_id": self.id})
    

class Review(models.Model):
    content = models.CharField(max_length=300)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
