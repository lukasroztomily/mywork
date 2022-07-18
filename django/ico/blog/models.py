from django.db import models



class Blog(models.Model):
        title_sk = models.CharField(max_length=90)
        headline_sk = models.CharField(max_length=250)
        text_sk = models.TextField()
        title_en = models.CharField(max_length=90)
        headline_en = models.CharField(max_length=250)
        text_en = models.TextField()
        title_de = models.CharField(max_length=90)
        headline_de = models.CharField(max_length=250)
        text_de = models.TextField()
        name = models.CharField(max_length=90)
        is_published = models.BooleanField(default=True)
        date = models.DateField(blank=True, null=True)

        def __str__(self):
           return self.title_sk




class Registeruz(models.Model):
        ico = models.CharField(max_length=90)
        nazovUJ = models.CharField(max_length=90)


class Ucetnizaverka(models.Model):
        ico = models.CharField(max_length=90)
        id_zaverka = models.CharField(max_length=90)