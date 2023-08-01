from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        # чтобы видно было в админ панели на web название кат
        return self.title


class Tour(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=900)
    price = models.IntegerField()
    place_qty = models.IntegerField()
    image = models.ImageField(upload_to='shop/images/')
    meeting_time = models.CharField(max_length=5)
    meeting_place = models.CharField(max_length=100)
    duration = models.FloatField(blank=True)
    # free_places = models.IntegerField()
    # reserved_places = models.IntegerField()
    # pri odstraneni Categorie, automatickz se odstrani vsechny kurzy v teto Cat
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
        # return self.title + ' '+str(self.students_qty)


class Review(models.Model):
    text = models.CharField(max_length=300)
    # the current datetime will be automatically filled in. This makes the field non-editable. Once the datetime is set, it is fixed
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    stars = models.IntegerField()
    recommend = models.BooleanField()

    def __str__(self):
        return self.text
