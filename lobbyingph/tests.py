from django.test import TestCase
from lobbyingph.models import *
from decimal import *


class LobbyistTestCase(TestCase):
    def setUp(self):
        self.lobbyist = Lobbyist.objects.create(
            name="Joe Smith",
            address1="Tall Building",
            address2="123 Main St.",
            address3="Suite 320",
            city="Philadelphia",
            state="PA",
            zipcode="19143",
            phone="215555555",
            email="joe.smith@company.com"
        )

    def test_lobbyist_exists(self):
        """Lobbyist was created successfully with provided attributes"""
        self.assertEqual(self.lobbyist.name, "Joe Smith")
        self.assertEqual(self.lobbyist.city, "Philadelphia")
        self.assertEqual(self.lobbyist.email, "joe.smith@company.com")

    def test_get_address(self):
        """get_address method returns the lobbyists's street address"""
        self.assertEqual(self.lobbyist.get_address(), "Tall Building, " +
            "123 Main St., Suite 320, Philadelphia, PA, 19143")


class FirmTestCase(TestCase):
    fixtures = ['principal', 'firm', 'lobbyist', 'filing']

    def setUp(self):
        self.firm = Firm.objects.create(
            name="Lobbying, Inc.",
            address1="The Penn Building",
            address2="400 Market St",
            address3="Suite 500",
            city="Philadelphia",
            state="PA",
            zipcode="19107",
            phone="2150901234",
            email="questions@lobbyinginc.com"
        )

        self.principal1 = Principal.objects.get(pk=4)
        self.principal2 = Principal.objects.get(pk=5)
        self.category1 = Category.objects.create(name='foo')
        self.category2 = Category.objects.create(name='bar')
        self.filing1 = Filing.objects.create(quarter='Q1',
            principal=self.principal1)
        self.filing1.save()
        self.filing1.firms.add(self.firm)
        self.filing2 = Filing.objects.create(quarter='Q2',
            principal=self.principal1)
        self.filing2.save()
        self.filing2.firms.add(self.firm)
        self.filing3 = Filing.objects.create(quarter='Q1',
            principal=self.principal2)
        self.filing3.save()
        self.filing3.firms.add(self.firm)
        Expenditure.objects.create(communication=0, category=self.category1,
            filing=self.filing1)
        Expenditure.objects.create(communication=0, category=self.category1,
            filing=self.filing2)
        Expenditure.objects.create(communication=0, category=self.category2,
            filing=self.filing2)

    def test_firm_exists(self):
        """Firm was created successfully with provided attributes"""
        self.assertEqual(self.firm.name, "Lobbying, Inc.")
        self.assertEqual(self.firm.city, "Philadelphia")
        self.assertEqual(self.firm.email, "questions@lobbyinginc.com")

    def test_get_address(self):
        """get_address method returns the firm's street address"""
        self.assertEqual(self.firm.get_address(), "The Penn Building, " +
            "400 Market St, Suite 500, Philadelphia, PA, 19107")

    def test_get_clients(self):
        """get_clients returns a list of clients which
        1) the items in the list are all of type Principal
        2) has no duplicates, and
        3) includes all the firms clients
        Clients are defined as Principals that have hired firm.
        Clients are determined by Filing.principal where client is in
        Filing.firms
        """
        firm = Firm.objects.get(pk=30)  # Wodjak
        unique_clients = []

        for client in firm.get_clients():
            # Test client is of type Principal
            self.assertEqual(type(client), Principal)
            if client.pk not in unique_clients:
                unique_clients.append(client.pk)

        # Test uniqueness
        self.assertEqual(len(unique_clients), len(set(firm.get_clients())))

        # Test client list is inclusive, and includes no duplicates
        self.assertEqual(len(self.firm.get_clients()), 2)

        for client in self.firm.get_clients():
            self.assertIn(client.pk, [4, 5])

    def test_get_client_count(self):
        """get_client_count returns an int representing the number
        of unique clients for a firm
        """
        firm = Firm.objects.get(pk=30)  # Wodjak

        self.assertEqual(type(firm.get_client_count()), int)
        self.assertEqual(firm.get_client_count(), len(firm.get_clients()))

    def test_get_topics(self):
        """get_topics returns a list of topics which
        1) the items in the list are all of type Category
        2) has no duplicates, and
        3) includes all the topics the firm has lobbied on.
        Topics are defined as Categories of lobbying expenditures
        that are included in Filings which the firm is included in
        Filing.firms
        """
        firm = Firm.objects.get(pk=30)  # Wodjak
        unique_topics = []

        for topic in firm.get_topics():
            # Test that topic is of type Category
            assertEqual(type(topic), Category)
            if topic.pk not in unique_topics:
                unique_topics.append(topic.pk)

        # Test uniqueness
        self.assertEqual(len(unique_topics), len(set(firm.get_topics())))

        # Test topic list is inclusive, and includes no duplicates
        self.assertEqual(len(self.firm.get_topics()), 2)

        for topic in self.firm.get_topics():
            self.assertIn(topic.pk, [self.category1.pk, self.category2.pk])


class PrincipalTestCase(TestCase):

    def setUp(self):
        self.principal1 = Principal.objects.create(
            name="Special Interest",
            address1="Girard Building",
            address2="400 South St",
            address3="Suite 100",
            city="Philadelphia",
            state="PA",
            zipcode="19107",
            phone="2154444444",
            email="lobby@specialinterest.com"
        )

        self.principal2 = Principal.objects.create(
            name="Specialer Interest",
            address1="Penn Tower",
            address2="100 Market St",
            address3="",
            city="Philadelphia",
            state="PA",
            zipcode="19107",
            phone="2154444444",
            email="lobby@specialinterest.com"
        )

        self.firm1 = Firm.objects.create(name="Lobbying, Inc.")
        self.firm2 = Firm.objects.create(name="Lawyers, Co.")
        self.firm3 = Firm.objects.create(name="Lobbytown")

        self.category1 = Category.objects.create(name='Real Estate')
        self.category2 = Category.objects.create(name='Healthcare')
        self.filing1 = Filing.objects.create(quarter='Q1',
            principal=self.principal1,
            total_exp_direct_comm=5000.05,
            total_exp_indirect_comm=15000.20,
            total_exp_other=1000.30)
        self.filing1.save()
        self.filing1.firms.add(self.firm1, self.firm2)
        self.filing2 = Filing.objects.create(quarter='Q2',
            principal=self.principal1,
            total_exp_direct_comm=21000.00,
            total_exp_indirect_comm=20500.20,
            total_exp_other=2000.37)
        self.filing2.save()
        self.filing1.firms.add(self.firm2, self.firm3)
        self.issue1 = Issue.objects.create(description='School Budget')
        self.issue2 = Issue.objects.create(description='Tax Reform')
        self.bill1 = Bill.objects.create(number='000000')
        self.bill2 = Bill.objects.create(number='111111')
        self.expenditure1 = Expenditure.objects.create(communication=0,
            category=self.category1, filing=self.filing1, issue=self.issue1,
            bill=self.bill1)
        self.expenditure1.save()
        self.expenditure2 = Expenditure.objects.create(communication=0,
            category=self.category1, filing=self.filing2, issue=self.issue2,
            bill=self.bill2)
        self.expenditure2.save()
        self.expenditure3 = Expenditure.objects.create(communication=0,
            category=self.category2, filing=self.filing2, issue=self.issue2)
        self.expenditure3.save()

    def test_principal_exists(self):
        self.assertEqual(self.principal1.name, 'Special Interest')
        self.assertEqual(self.principal1.address1, 'Girard Building')
        self.assertEqual(self.principal1.phone, '2154444444')

    def test_get_address(self):
        self.assertEqual(self.principal1.get_address(),
            'Girard Building, 400 South St, Suite 100, Philadelphia, PA, 19107')
        self.assertEqual(self.principal2.get_address(),
            'Penn Tower, 100 Market St, Philadelphia, PA, 19107')

    def test_get_exp_totals(self):
        # No parameters return sum for all quarters
        totals = self.principal1.get_exp_totals()

        self.assertEqual(totals['direct'], Decimal('26000.05'))
        self.assertEqual(totals['indirect'], Decimal('35500.40'))
        self.assertEqual(totals['other'], Decimal('3000.67'))

        # Providing quarter parameter returns totals just for that quarter
        q1_totals = self.principal1.get_exp_totals(quarter='Q1', year=2012)

        self.assertEqual(q1_totals['direct'], Decimal('5000.05'))
        self.assertEqual(q1_totals['indirect'], Decimal('15000.20'))
        self.assertEqual(q1_totals['other'], Decimal('1000.30'))

    def test_get_total_exp(self):
        # sums get_exp_totals
        self.assertEqual(self.principal1.get_total_exp(), Decimal('64501.12'))

    def test_get_exp_totals_by_quarter(self):
        totals = self.principal1.get_exp_totals_by_quarter()

        self.assertEqual(totals['Q12012']['direct'], Decimal('5000.05'))
        self.assertEqual(totals['Q12012']['indirect'], Decimal('15000.20'))
        self.assertEqual(totals['Q12012']['other'], Decimal('1000.30'))
        self.assertEqual(totals['Q22012']['direct'], Decimal('21000.00'))
        self.assertEqual(totals['Q22012']['indirect'], Decimal('20500.20'))
        self.assertEqual(totals['Q22012']['other'], Decimal('2000.37'))

    def test_get_exp_percents(self):
        # No parameters return percents of total spending for each type
        percents = self.principal1.get_exp_percents()
        self.assertEqual(percents['direct'], '40.31')
        self.assertEqual(percents['indirect'], '55.04')
        self.assertEqual(percents['other'], '4.65')

        # Providing quarter parameter returns total just for that quarter
        q1_percents = self.principal1.get_exp_percents(quarter='Q1', year=2012)

        self.assertEqual(q1_percents['direct'], '23.81')
        self.assertEqual(q1_percents['indirect'], '71.43')
        self.assertEqual(q1_percents['other'], '4.76')

        # Test that percents add up to 100%
        total = (Decimal(q1_percents['direct']) + Decimal(q1_percents['indirect']) +
                Decimal(q1_percents['other']))

        self.assertEqual(total, Decimal('100.00'))

    def test_get_exp_percents_by_quarter(self):
        percents = self.principal1.get_exp_percents_by_quarter()

        self.assertEqual(percents['Q12012']['direct'], '23.81')
        self.assertEqual(percents['Q12012']['indirect'], '71.43')
        self.assertEqual(percents['Q12012']['other'], '4.76')
        self.assertEqual(percents['Q22012']['direct'], '48.28')
        self.assertEqual(percents['Q22012']['indirect'], '47.13')
        self.assertEqual(percents['Q22012']['other'], '4.60')

    def test_get_topics(self):
        for topic in self.principal1.get_topics():
            self.assertIn(topic.name, ['Real Estate', 'Healthcare'])

    def test_get_firms(self):
        self.assertEqual(len(self.principal1.get_firms()), 3)

        for firm in self.principal1.get_firms():
            self.assertIn(firm.name, ["Lobbying, Inc.", "Lawyers, Co.",
                "Lobbytown"])

    def test_get_issues(self):
        self.assertEqual(len(self.principal1.get_issues()), 3)

        for issue in self.principal1.get_issues():
            self.assertIn(issue['object'].description, ['School Budget', 'Tax Reform'])

    def test_get_unique_issues(self):
        pass

    def test_get_unique_bills(self):
        pass

    def get_issue_and_bill_count(self):
        pass


class OfficialTestCase(TestCase):
    fixtures = ['official', 'firm', 'principal', 'lobbyist', 'filing',
        'expenditure', 'communication_method', 'receipent_group', 'agency'
    ]

    def setUp(self):
        self.official = Official.objects.create(first_name="Michael",
            last_name="Nutter", title="Mayor")
        self.principal1 = Principal.objects.get(pk=4)
        self.category1 = Category.objects.create(name='foo')
        self.category2 = Category.objects.create(name='bar')
        self.filing1 = Filing.objects.create(quarter='Q1',
            principal=self.principal1)
        self.filing2 = Filing.objects.create(quarter='Q2',
            principal=self.principal1)
        self.issue1 = Issue.objects.create(description='Foo')
        self.issue2 = Issue.objects.create(description='Bar')
        self.bill1 = Bill.objects.create(number='000000')
        self.bill2 = Bill.objects.create(number='111111')
        self.expenditure1 = Expenditure.objects.create(communication=0,
            category=self.category1, filing=self.filing1, issue=self.issue1,
            bill=self.bill1)
        self.expenditure1.save()
        self.expenditure1.officials.add(self.official)
        self.expenditure2 = Expenditure.objects.create(communication=0,
            category=self.category1, filing=self.filing2, issue=self.issue2,
            bill=self.bill2)
        self.expenditure2.save()
        self.expenditure2.officials.add(self.official)
        self.expenditure3 = Expenditure.objects.create(communication=0,
            category=self.category2, filing=self.filing2, issue=self.issue2)
        self.expenditure3.save()
        self.expenditure3.officials.add(self.official)

    def test_official_exists(self):
        """Official was created successfully with provided attributes"""
        self.assertEqual(self.official.first_name, 'Michael')
        self.assertEqual(self.official.last_name, 'Nutter')
        self.assertEqual(self.official.title, 'Mayor')

    def test_get_lobby_count(self):
        """get_lobby_counts returns a number that
        1) is an int, and
        2) represents all the times the official has been lobbied.
        Lobby count returns the number of times the official has been
        included in Expenditure (in Expenditure.officials)
        """
        #  Test that output is an int
        official = Official.objects.get(pk=18)  # Henon

        self.assertEqual(type(official.get_lobby_count()), int)

        #  Test that count is accurate
        self.assertEqual(self.official.get_lobby_count(), 3)

    def test_get_topics(self):
        """get_topics returns a list of topics which
        1) the items in the list are all of type Category
        2) has no duplicates, and
        3) includes all the topics the official has been lobbied on.
        Topics are defined as Categories of lobbying expenditures
        which the official is included in Expenditure.officials
        """
        official = Official.objects.get(pk=18)  # Henon
        unique_topics = []

        # Test that topic is of type Category
        for topic in official.get_topics():
            self.assertEqual(type(topic), Category)
            if topic.pk not in unique_topics:
                unique_topics.append(topic.pk)

        # Test uniqueness
        self.assertEqual(len(unique_topics), len(set(official.get_topics())))

        # Test that get_topic is inclusive
        self.assertEqual(len(self.official.get_topics()), 2)

        for topic in self.official.get_topics():
            self.assertIn(topic.pk, [self.category1.pk, self.category2.pk])

    def test_get_issues(self):
        """get_issues
        1) the object key is of type Issue, and
        2) includes all the issues the offical has been lobbied on
        """
        official = Official.objects.get(pk=18)  # Henon

        # Test that object key is of type Issue
        for issue in official.get_issues():
            self.assertEqual(type(issue['object']), Issue)

        # Test that get_issues is inclusive
        self.assertEqual(len(self.official.get_issues()), 3)

        for issue in self.official.get_issues():
            self.assertIn(issue['object'], [self.issue1, self.issue2])

    def test_get_bills(self):
        """get_bills
        1) the object key is of type Bill, and
        2) includes all the bills the official has been lobbed on
        """
        official = Official.objects.get(pk=18)  # Henon

        # Test that object key is of type Bill
        for bill in official.get_bills():
            self.assertEqual(type(bill['object']), Bill)

        # Test that get_bills is inclusive
        self.assertEqual(len(self.official.get_bills()), 2)

        for bill in self.official.get_bills():
            self.assertIn(bill['object'], [self.bill1, self.bill2])


class FilingTestCase(TestCase):

    def setUp(self):
        self.filing1 = Filing.objects.create(
            quarter='Q1',
            total_exp_direct_comm=10000.10,
            total_exp_indirect_comm=20000.20,
            total_exp_other=5000.30
        )

        self.filing2 = Filing.objects.create(
            quarter='Q1',
            total_exp_direct_comm=10000.12,
            total_exp_indirect_comm=20000.20,
            total_exp_other=5000.37
        )

    def test_filing_exists(self):
        """Filing was created successfully with provided attributes"""
        self.assertEqual(self.filing1.quarter, 'Q1')
        self.assertEqual(self.filing1.total_exp_direct_comm, 10000.10)
        self.assertEqual(self.filing1.total_exp_indirect_comm, 20000.20)
        self.assertEqual(self.filing1.total_exp_other, 5000.30)

    def test_get_total_exp(self):
        """get_total_exp returns the total expenditures that were reported
        1) always returns a decimal
        2) equals the total of the three expenditure fields
        """

        # Test that it returns a Decimal
        self.assertEqual(type(self.filing1.get_total_exp()), Decimal)
        self.assertEqual(type(self.filing2.get_total_exp()), Decimal)

        # Test that it's including all three expenditure fields in total
        self.assertEqual(self.filing1.get_total_exp(), Decimal('35000.60'))
        self.assertEqual(self.filing2.get_total_exp(), Decimal('35000.69'))
