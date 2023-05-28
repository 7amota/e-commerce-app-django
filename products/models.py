from django.db import models
from core.models import TimeStampedModel
from django.core.validators import MaxValueValidator,MinValueValidator
class Product(TimeStampedModel):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    discount = models.DecimalField(blank=True,null=True, max_digits=4, decimal_places=1, validators=[MaxValueValidator(100),MinValueValidator(5)])
    image = models.ImageField(upload_to='product_images/%y/%m/%d')
    price_with_discount = models.DecimalField(max_digits=5, decimal_places=1,blank=True)
    @property
    def current_price(self):
        if self.discount is not None:
            return self.price - (self.discount * self.price) / 100
        else:
            return self.price
    def save(self, *args, **kwargs):
       self.price_with_discount = self.current_price
       if self.discount == None:
           self.discount = 0.0
       super().save(*args, **kwargs) # Call the real save() method
            