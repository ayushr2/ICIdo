from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

class Donor(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to = {'is_staff':False})

    first_name = models.CharField('FirstName', max_length=40)
    last_name = models.CharField('LastName', max_length=40)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    interest = models.ManyToManyField(Category)

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)



# class Organization(models.Model):
    # name = models.CharField(max_length=100)
    # description = models.TextField(max_length=5000)
    # # staff maybe


class Profolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor = models.OneToOneField(Donor)

    profolio = models.OneToOneField(Profolio)
    amount = models.FloatField()
    date = models.DateField()
    honor = models.TextField(max_length = 1000)

    # TODO revise to change of the recurrence
    recurrence  = models.CharField(max_length=50)

    def __str__(self):
        return "{} from {} to {}".format(self.amount, self.donor, self.profolio)

    





