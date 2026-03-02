from django.db import models

# Create your models here.
class student_model(models.Model):
    name=models.CharField(max_length=60)
    roll=models.IntegerField()
    department=models.CharField(max_length=50)
    email=models.EmailField()
    photo=models.ImageField(
        upload_to='img/'
    )
    file=models.FileField(
        upload_to='file/'
    )

    def __str__(self):
        return self.name
