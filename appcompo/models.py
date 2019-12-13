from django.db import models
from django.utils.text import slugify
# Create your models here.

import hashlib
# from tinymce import HTMLField


class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(max_length=255)
    titre_slug = models.SlugField(unique=True, editable=False, null=True, blank=True, max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    def save(self, *args, **kwargs):
        encoded_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.nom+' '+str(encoded_id.hexdigest()))
        super(Categorie, self).save(*args, **kwargs)
    
    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom

class Auteur(models.Model):
    """Model definition for Auteur."""

    # TODO: Define fields here
    
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='imageauteur',)
    description = models.TextField()
    titre_slug = models.SlugField(unique=True, editable=False, null=True, blank=True, max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    def save(self, *args, **kwargs):
        encoded_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.nom+' '+str(encoded_id.hexdigest()))
        super(Auteur, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Auteur."""

        verbose_name = 'Auteur'
        verbose_name_plural = 'Auteurs'

    def __str__(self):
        """Unicode representation of Auteur."""
        return self.nom

class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='categoriearticle')
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE,related_name='auteurarticle')
    titre = models.CharField(max_length=255)
    titre_slug = models.SlugField(unique=True, editable=False, null=True, blank=True, max_length=255)
    image = models.ImageField(upload_to='imagearticle',)
    description = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    def save(self, *args, **kwargs):
        encoded_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.titre+' '+str(encoded_id.hexdigest()))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre

class Commentaire(models.Model):
    """Model definition for Commentaire."""

    # TODO: Define fields here
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='articlecommentaire')
    nom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    Website = models.CharField(max_length=255)
    message = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.nom

class Tag(models.Model):
    """Model definition for Tage."""

    # TODO: Define fields here
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='articletag')
    nom = models.CharField(max_length=255)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True,)

    class Meta:
        """Meta definition for Tage."""

        verbose_name = 'Tage'
        verbose_name_plural = 'Tages'

    def __str__(self):
        """Unicode representation of Tage."""
        return self.nom






