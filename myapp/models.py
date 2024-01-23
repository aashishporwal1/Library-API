from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='author_profiles/')
    author_id = models.CharField(max_length=20, unique=True, editable=False)

    #Function for generating unique author ids
    def generate_author_id(self):
        city_code = self.city[:3].upper()
        authors_with_same_city = Author.objects.filter(city=self.city)
        next_id = authors_with_same_city.count() + 1
        author_id = f'AR{city_code}{next_id:04d}'
        return author_id

@receiver(pre_save, sender=Author)
def set_author_id(sender, instance, **kwargs):
    if not instance.author_id:
        instance.author_id = instance.generate_author_id()

class Book(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/')
