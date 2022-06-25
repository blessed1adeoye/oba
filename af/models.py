from django.db import models


class HomeCarousel(models.Model):
    img = models.ImageField(upload_to='home/carousel')
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'AMAZON CAROUSEL'

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='Products')
    url = models.URLField()
    # cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    paragraph = models.TextField()
    price = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'AMAZON PRODUCTS'




class JumiaCarousel(models.Model):
    img = models.ImageField(upload_to='home/carousel')
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'JUMIA CAROUSEL'

# class Category(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name

class JumiaProduct(models.Model):
    name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='Products')
    url = models.URLField()
    # cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    # paragraph = models.TextField()
    # price = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'JUMIA PRODUCTS'
