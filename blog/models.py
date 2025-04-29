from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='articles/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
