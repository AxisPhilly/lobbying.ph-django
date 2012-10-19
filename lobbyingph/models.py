from django.db import models
import datetime
from django.db.models import Sum
from decimal import Decimal


STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'Calfornia'),
    ('CO', 'Colorado'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('IL', 'Illinois'),
    ('FL', 'Florida'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('NC', 'North Carolina'),
    ('NJ', 'New Jersey'),
    ('NY', 'New York'),
    ('PA', 'Pennsylvania'),
    ('VA', 'Virginia'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('WA', 'Washington'),
)


class Lobbyist(models.Model):
    """
    Individual, attached to firms and principals
    """
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
    principals = models.ManyToManyField('Principal', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_address(self):
        add_list = [self.address1, self.city, self.state, self.zipcode]
        return ', '.join(add_list)


class Firm(models.Model):
    """
    Entity which is hired by Principal
    """
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

    def get_clients(self):
        unique_clients = self.filing_set.distinct(
            'principal').only('principal').select_related('principal')
        clients = []

        for row in unique_clients:
            clients.append(row.principal)

        clients.sort(key=str)
        return clients

    def get_client_count(self):
        clients = self.get_clients()
        return len(clients)

    def get_topics(self):
        topics = []

        for row in self.filing_set.all():
            direct = row.exp_direct_comm_set.distinct('category')
            indirect = row.exp_direct_comm_set.distinct('category')

            for row in indirect:
                if (row.category not in topics):
                    topics.append(row.category)

            for row in direct:
                if (row.category not in topics):
                    topics.append(row.category)

        topics.sort(key=str)
        return topics


class Principal(models.Model):
    """
    Lobbying organization who themselves lobby or pay firms
    to lobby on their behalf
    """
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

    def get_total_exp(self):
        totals = self.get_exp_totals()
        return sum(totals.itervalues())

    def get_exp_totals(self, quarter=None, year=None):
        if quarter:
            totals = self.filing_set.filter(
                    quarter=quarter, year__year=year
                ).aggregate(
                    direct=Sum('total_exp_direct_comm'),
                    indirect=Sum('total_exp_indirect_comm'),
                    other=Sum('total_exp_other')
                )
        else:
            totals = self.filing_set.aggregate(
                direct=Sum('total_exp_direct_comm'),
                indirect=Sum('total_exp_indirect_comm'),
                other=Sum('total_exp_other')
            )

        # patched until this is released:
        # https://code.djangoproject.com/ticket/10929
        for exp_type, dollars in totals.items():
            if not dollars:
                totals[exp_type] = Decimal(0.00)

        return totals

    def get_exp_totals_by_quarter(self):
        quarters = self.filing_set.distinct(
            'quarter', 'year').values('quarter', 'year')

        results = {}
        for quarter in quarters:
            totals = self.get_exp_totals(
                quarter=quarter['quarter'], year=quarter['year'].year)
            results[quarter['quarter'] + str(quarter['year'].year)] = totals

        return results

    def get_exp_percents(self, quarter=None, year=None):
        totals = self.get_exp_totals(quarter, year)
        total = sum(totals.itervalues())

        if total != 0:
            return {
                'direct': '%.2f' % ((totals['direct'] / total) * 100),
                'indirect': '%.2f' % ((totals['indirect'] / total) * 100),
                'other': '%.2f' % ((totals['other'] / total) * 100)
            }
        else:
            return {
                'direct': 0,
                'indirect': 0,
                'other': 0
            }

    def get_exp_percents_by_quarter(self):
        quarters = self.filing_set.distinct(
            'quarter', 'year').values('quarter', 'year')

        results = {}
        for quarter in quarters:
            totals = self.get_exp_percents(
                quarter=quarter['quarter'], year=quarter['year'].year)
            results[quarter['quarter'] + str(quarter['year'].year)] = totals

        return results

    def get_topics(self):
        topics = []

        for row in self.filing_set.all():
            direct = row.exp_direct_comm_set.distinct('category')
            indirect = row.exp_indirect_comm_set.distinct('category')

            for row in direct:
                if (row.category not in topics):
                    topics.append(row.category)

            for row in indirect:
                if (row.category not in topics):
                    topics.append(row.category)

        return topics

    def get_firms(self):
        firms = []
        for row in self.filing_set.all():

            unique_firms = row.firms.distinct('name')

            for firm in unique_firms:
                if firm not in firms:
                    firms.append(firm)

        return firms

    def get_issues(self):
        issues = []

        for row in self.filing_set.all():

            direct = row.exp_direct_comm_set.all()
            indirect = row.exp_indirect_comm_set.all()

            for row in direct:
                if row.issue != None:
                    issues.append({
                        'time': str(row.filing.year.year) + row.filing.quarter,
                        'issue': row.issue,
                        'position': row.get_position_display(),
                        'other': row.other_desc,
                        'target': list(row.officials.all()) +
                                    list(row.agencies.all()),
                        'comm': 'Direct'
                    })

            for row in indirect:
                if row.issue != None:
                    target = list(row.officials.all()) + list(row.groups.all())
                    if row.agency:
                        target.append(row.agency)

                    issues.append({
                        'time': str(row.filing.year.year) + row.filing.quarter,
                        'issue': row.issue,
                        'position': row.get_position_display(),
                        'other': row.other_desc,
                        'target': target,
                        'comm': 'Indirect'
                    })

        return issues

    def get_issue_count(self):
        issues = self.get_issues()

        unique_issues = []
        for issue in issues:
            if issue['issue'] not in unique_issues:
                unique_issues.append(issue['issue'])

        return len(unique_issues)

    def get_bills(self):
        bills = []

        for row in self.filing_set.all():

            direct = row.exp_direct_comm_set.all()
            indirect = row.exp_indirect_comm_set.all()

            for row in direct:
                if row.bill != None:
                    bills.append({
                        'time': str(row.filing.year.year) + row.filing.quarter,
                        'bill': row.bill,
                        'position': row.get_position_display(),
                        'other': row.other_desc,
                        'target': list(row.officials.all()) +
                                    list(row.agencies.all()),
                        'comm': 'Direct'
                    })

            for row in indirect:
                if row.bill != None:
                    target = list(row.officials.all()) + list(row.groups.all())
                    if row.agency:
                        target.append(row.agency)

                    bills.append({
                        'time': str(row.filing.year.year) + row.filing.quarter,
                        'bill': row.bill,
                        'position': row.get_position_display(),
                        'other': row.other_desc,
                        'target': target,
                        'comm': 'Indirect'
                    })

        return bills

    def get_bill_count(self):
        bills = self.get_bills()

        unique_bills = []
        for bill in bills:
            if bill['bill'] not in unique_bills:
                unique_bills.append(bill['bill'])

        return len(unique_bills)

    def get_issue_bill_count(self):
        bills = self.get_bill_count()
        issues = self.get_issue_count()

        return (bills + issues)

POSITION_CHOICE = (
    (1, 'Support'),
    (2, 'Oppose'),
    (3, 'Amend'),
    (4, 'Proposed'),
    (5, 'Other'),
    (6, 'Monitor'),
)

QUARTER_CHOICES = (
    ('Q1', 'Q1'),
    ('Q2', 'Q2'),
    ('Q3', 'Q3'),
    ('Q4', 'Q4'),
)


class Filing(models.Model):
    """
    Quarterly filing usually by Principal, but sometimes firm.
    Basically a digital representation of paper form.
    """
    quarter = models.CharField(max_length=2, choices=QUARTER_CHOICES)
    year = models.DateField(
        null=False, blank=False, default=datetime.date.today)
    total_exp_direct_comm = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    total_exp_indirect_comm = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    total_exp_other = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    principal = models.ForeignKey(Principal, null=True, blank=True)
    firms = models.ManyToManyField(Firm, null=True, blank=True)
    lobbyists = models.ManyToManyField(Lobbyist, null=True, blank=True)
    errors = models.BooleanField(default=False)
    corrected = models.BooleanField(default=False)
    error_description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.year.year) + self.quarter + ': ' + self.principal.name

    def get_total_exp(self):
        total = (self.total_exp_direct_comm +
                self.total_exp_indirect_comm +
                self.total_exp_other)

        return total


class Exp_Direct_Comm(models.Model):
    """
    Expenditure, type Direct Communication
    Filing is parent.
    """
    category = models.ForeignKey('Category')
    issue = models.ForeignKey('Issue', blank=True, null=True)
    bill = models.ForeignKey('Bill', blank=True, null=True)
    position = models.SmallIntegerField(
        choices=POSITION_CHOICE, blank=True, null=True)
    other_desc = models.CharField(max_length=200, blank=True, null=True)
    agencies = models.ManyToManyField('Agency', blank=True, null=True)
    officials = models.ManyToManyField('Official', blank=True, null=True)
    filing = models.ForeignKey(Filing)


class Exp_Indirect_Comm(models.Model):
    """
    Expenditure, type Indirect Communication
    Filing is parent.
    """
    category = models.ForeignKey('Category')
    issue = models.ForeignKey('Issue', blank=True, null=True)
    bill = models.ForeignKey('Bill', blank=True, null=True)
    position = models.SmallIntegerField(choices=POSITION_CHOICE)
    other_desc = models.CharField(max_length=200, blank=True, null=True)
    agency = models.ForeignKey('Agency', blank=True, null=True)
    officials = models.ManyToManyField('Official', blank=True, null=True)
    methods = models.ManyToManyField(
        'Communication_Method', blank=True, null=True)
    groups = models.ManyToManyField('Receipent_Group', blank=True, null=True)
    filing = models.ForeignKey(Filing)


class Exp_Other(models.Model):
    """
    Expenditure, type Other (travel, lodging, etc)
    Filing is parent.
    """
    official = models.ForeignKey('Official', null=True)
    agency = models.ForeignKey('Agency', null=True)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    source = models.ForeignKey(Principal, null=True)
    filing = models.ForeignKey(Filing)


class Official(models.Model):
    """
    City Official. Identified in Expenditures
    Work for an Agency
    """
    first_name = models.CharField(
        max_length=100, blank=True, null=True, default='')
    last_name = models.CharField(
        max_length=100, blank=False, null=False, default='')
    title = models.CharField(max_length=100, blank=True, null=True)
    agency = models.ForeignKey('Agency', blank=True, null=True)

    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Agency(models.Model):
    """
    Collection of Officials
    """
    name = models.CharField(max_length=100, blank=False, null=False)
    alias = models.CharField(max_length=100, blank=False, null=False, default='')

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

BILL_TYPE_CHOICES = (
    (0, 'Bill'),
    (1, 'Resolution')
)


class Source(models.Model):
    """
    Source document for Filing. Usually quarterly expense report
    """
    name = models.CharField(max_length=100, blank=False, null=True)
    url = models.URLField(blank=False, null=True)
    filing = models.ForeignKey(Filing, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Bill(models.Model):
    """
    City Council bill
    """
    name = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(
        max_length=10, blank=False, null=False, default=0)
    bill_type = models.SmallIntegerField(
        blank=False, null=False, default=0, choices=BILL_TYPE_CHOICES)
    url = models.URLField(
        blank=False, null=False,
        default="http://legislation.phila.gov/detailreport/?key=")

    class Meta:
        ordering = ['number']

    def __unicode__(self):
        return self.number


class Issue(models.Model):
    """
    Issue mentioned in expenditure reports.
    Sometimes attached to Bill.
    """
    description = models.TextField(blank=False, null=False)
    bill = models.ForeignKey(Bill, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    detail_view = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        ordering = ['description']

    def __unicode__(self):
        return self.description


class Category(models.Model):
    """
    Lobbying category. Defined for each expenditure.
    Source is last page of paper filing form.
    """
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Communication_Method(models.Model):
    """
    Attached to Exp_Indirect_Comm.
    Defines how lobbying was conducted (ex: social media, meeting)
    """
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Receipent_Group(models.Model):
    """
    Group targeted by a Exp_Indirect_Comm
    """
    name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

PUBLISHER_CHOICES = (
    (0, 'Inquirer'),
    (1, 'Daily News'),
    (2, 'CBS Philly'),
    (3, 'Philadelphia Weekly'),
    (4, 'City Paper'),
    (5, 'Bloomberg'),
    (6, 'PhillyMag'),
)


class Article(models.Model):
    """
    News article. Attached to Issues.
    """
    headline = models.CharField(max_length=200, blank=False, null=False)
    publisher = models.SmallIntegerField(
        blank=False, null=True, choices=PUBLISHER_CHOICES)
    url = models.URLField(blank=False, null=False)
    date = models.DateField(
        blank=False, null=False, default=datetime.date.today())
    quote = models.TextField(blank=True, null=True)
    issue = models.ForeignKey(Issue, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __unicode__(self):
        return self.headline
