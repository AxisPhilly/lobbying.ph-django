from django.db import models

STATE_CHOICES = (('PA','Pennsylvania'),)

class Lobbyist(models.Model):
    name = models.CharField(max_length=75)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=75)

    firm = models.ForeignKey('Firm', null=True, blank=True)

    def get_address(self):
        add_list = [self.address1, self.city, self.state, self.zipcode]
        return ', '.join(add_list)

class Firm(models.Model):
    name = models.CharField(max_length=150)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=75)

    def get_address(self):
        add_list = [self.address1, self.city, self.state, self.zipcode]
        return ', '.join(add_list)

class Principal(models.Model):
    name = models.CharField(max_length=150)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=75)

    def get_address(self):
        add_list = [self.address1, self.city, self.state, self.zipcode]
        return ', '.join(add_list)