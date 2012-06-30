from django.db import models
import datetime

STATE_CHOICES = (
    ('AL','Alabama'),
    ('AR','Arkansas'),
    ('CA','Calfornia'),
    ('CO','Colorado'),
    ('DC','District of Columbia'),
    ('DE','Delaware'),
    ('IL','Illinois'),
    ('FL','Florida'),
    ('MA','Massachusetts'),
    ('MD','Maryland'),
    ('NC','North Carolina'),
    ('NJ','New Jersey'),
    ('NY','New York'),
    ('PA','Pennsylvania'),
    ('VA','Virginia'),
    ('TN','Tennessee'),
    ('TX','Texas'),
    ('WA','Washington'),
)

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

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

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

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

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

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_address(self):
        add_list = [self.address1, self.city, self.state, self.zipcode]
        return ', '.join(add_list)

POSITION_CHOICE = (
    (1, 'Support'),
    (2, 'Oppose'),
    (3, 'Amend'),
    (4, 'Proposed'),
    (5, 'Other'),
    (6, 'Monitor'),
)

QUARTER_CHOICES = (
    ('Q1','Q1'),
    ('Q2','Q2'),
    ('Q3','Q3'),
    ('Q4','Q4'),
)

class Filing(models.Model):
    quarter = models.CharField(max_length=2, choices=QUARTER_CHOICES)
    year = models.DateField(null=False, blank=False, default=datetime.date.today)
    total_exp_direct_comm = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_exp_indirect_comm = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total_exp_other = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    principal = models.ForeignKey(Principal, null=True, blank=True)
    firms = models.ManyToManyField(Firm, null=True, blank=True)
    lobbyists = models.ManyToManyField(Lobbyist, null=True, blank=True)

    def __unicode__(self):
        return str(self.year.year) + self.quarter + ': ' + self.principal.name

class Exp_Direct_Comm(models.Model):
    category = models.ForeignKey('Category')
    issue = models.ForeignKey('Issue', blank=True, null=True)
    bill = models.ForeignKey('Bill', blank=True, null=True)
    position = models.SmallIntegerField(choices=POSITION_CHOICE, blank=True, null=True)
    other_desc = models.CharField(max_length=100, blank=True, null=True)
    agencies = models.ManyToManyField('Agency', blank=True, null=True)
    officials = models.ManyToManyField('Official', blank=True, null=True)
    filing = models.ForeignKey(Filing)

class Exp_Indirect_Comm(models.Model):
    category = models.ForeignKey('Category')
    issue = models.ForeignKey('Issue', blank=True, null=True)
    bill = models.ForeignKey('Bill', blank=True, null=True)
    position = models.SmallIntegerField(choices=POSITION_CHOICE)
    other_desc = models.CharField(max_length=100, blank=True, null=True)
    agency = models.ForeignKey('Agency', blank=True, null=True)
    officials = models.ManyToManyField('Official', blank=True, null=True)
    methods = models.ManyToManyField('Communication_Method', blank=True, null=True)
    groups = models.ManyToManyField('Receipent_Group', blank=True, null=True)
    filing = models.ForeignKey(Filing)

class Exp_Other(models.Model):
    official = models.ForeignKey('Official', null=True)
    agency = models.ForeignKey('Agency', null=True)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    source = models.ForeignKey(Principal, null=True)
    filing = models.ForeignKey(Filing)

class Official(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True, default='')
    last_name = models.CharField(max_length=100, blank=False, null=False, default='')
    title = models.CharField(max_length=100, blank=True, null=True)
    agency = models.ForeignKey('Agency', blank=True, null=True)

    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return self.first_name  + ' ' + self.last_name + ': ' + self.agency.name

class Agency(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

BILL_TYPE_CHOICES = (
    (0, 'Bill'),
    (1, 'Resolution')
)

class Source(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    url = models.URLField(blank=False, null=True)
    filing = models.ForeignKey(Filing, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Bill(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=10, blank=False, null=False, default=0)
    bill_type = models.SmallIntegerField(blank=False, null=False, default=0, choices=BILL_TYPE_CHOICES)
    url = models.URLField(blank=False, null=False, default="http://legislation.phila.gov/detailreport/?key=")

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return self.number

class Issue(models.Model):
    description = models.TextField(blank=False, null=False)

    class Meta:
        ordering = ['description']

    def __unicode__(self):
        return self.description

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Communication_Method(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Receipent_Group(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

