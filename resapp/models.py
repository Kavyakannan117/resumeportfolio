from django.db import models

# Create your models here.
class ModelCv(models.Model):
    name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.name)

class CreateContact(models.Model):
    aboutme=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField()
    website=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pic_pedia')
    def __str__(self):
        return '{}'.format(self.img)

class Portfolio(models.Model):

    pic_base=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pic_pedia')

    def __str__(self):
        return '{}'.format(self.pic_base)

class Education(models.Model):
    year_of_passing=models.DateField()
    education=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    description=models.CharField(max_length=200)


    def __str__(self):
        return '{}'.format(self.education)

class Skills(models.Model):
    percentage=models.IntegerField()
    skill=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.skill)

class Experience(models.Model):
    year=models.DateField()
    company_name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    role=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.experience)

