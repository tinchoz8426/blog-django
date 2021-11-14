from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, DateTimeField, EmailField, SlugField, TextField

# Create your models here.
class Category(models.Model):
    title = CharField(max_length=200)
    slug = SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Activo'),
        (DRAFT, 'Borrador')
    )

    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = CharField(max_length=200)
    slug = SlugField()
    intro = TextField()
    body = TextField()
    created_at = DateTimeField(auto_now_add=True)
    status = CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s' % (self.category.slug, self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = CharField(max_length=200)
    email = EmailField()
    body = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name