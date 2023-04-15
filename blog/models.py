from django.db import models


class AbstractUser(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)

    class Meta:
        abstract=True


class Author(AbstractUser):
    username=models.CharField(max_length=30)
    date_register=models.DateField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title=models.CharField(max_length=150)
    author=models.ManyToManyField(Author,related_name='articles',through='Publication')

    def __str__(self):
        return self.name


class Publication(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    date_published=models.DateTimeField(auto_now_add=True)

