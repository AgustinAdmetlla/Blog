from django.db import models


def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

class Post(models.Model):
    title = models.CharField(max_length=250)
    thumbnail = models.ImageField(
        upload_to = user_directory_path, 
        #default = 'blog/default.jpg'
        blank = True,
        null = True
    )
    excerpt = models.TextField(null=True)
    content = models.TextField()
    # slug es para agregar contenido
    slug = models.SlugField(max_length=250, unique_for_date='published')































