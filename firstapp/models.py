from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinValueValidator,RegexValidator


# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s)" % (self.name, self.hod)


class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch, on_delete= CASCADE, null=True, blank=True)


class Profile(models.Model):
    sem = models.IntegerField(default=1, choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)))
    mark_10 = models.IntegerField(default=0, validators=[MinValueValidator(0, MinValueValidator(100))])
    mark_12 = models.IntegerField(default=0, validators=[MinValueValidator(0, MinValueValidator(100))])
    mark_aggr = models.IntegerField(default=0, validators=[MinValueValidator(0, MinValueValidator(100))])
    # rn = models.IntegerField(validators=[MinValueValidator(1)], unique=True, blank=True, null=True)
    # pn = models.CharField(validators=[RegexValidator("^0?[5-9]{1\d{9}$")], max_length=15, blank=True, default='DEFAULT VALUE')

    def __str__(self):
        return "%s (%s)" % (self.user.username, self.branch)



