from django.db import models
from django.core.files.storage import FileSystemStorage
# from django.core.urlresolvers import reverse

# fs = FileSystemStorage(location='/media/photos')
# storage=fs,
# Create your models here.
def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Post(models.Model):
    titre = models.CharField(max_length=255)
    image= models.ImageField(upload_to='post/')
    height_field= models.IntegerField(default=0)
    width_field= models.IntegerField(default=0)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add= True)
    date_upd= models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)
    Categorie_id= models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='Categorie_Post')

    def  __unicode__(self):
        return self.titre
    def __str__(self):
        return self.titre
    def get_url(self):
        return reverse("post:detail", kwargs={"id": self.id})




class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    image= models.ImageField(upload_to='categorie/')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add= True)
    date_upd= models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)

class Commentaire(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add= True)
    date_upd= models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)
    Post_id= models.ForeignKey('Post', on_delete= models.CASCADE, related_name='Post_Commentaire')
    # Utili_id= models.OneToOneField('Utili', on_delete= models.CASCADE, related_name='Utili_Commentaire')

class Utili(models.Model):
    nom= models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add= True)
    date_upd= models.DateTimeField(auto_now=True)