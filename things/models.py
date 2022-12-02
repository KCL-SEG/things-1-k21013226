from django.db import models
# Create your models here.

from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120,blank=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])



#name  must not be blank,

#description need not be unique,

#quantity need not be unique, and must be an integer value between 0 and 100 (inclusive).
#quantity may be 0 and it may be 100, but not less than 0 and not more than 100.
