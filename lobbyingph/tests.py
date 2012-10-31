from django.test import TestCase
from lobbyingph.models import *


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
            "Philadelphia, PA, 19143")


class FirmTestCase(TestCase):
    fixtures = ['principal', 'firm', 'lobbyist', 'filing', 'expenditure']

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

    def test_firm_exists(self):
        """Firm was created successfully with provided attributes"""
        self.assertEqual(self.firm.name, "Lobbying, Inc.")
        self.assertEqual(self.firm.city, "Philadelphia")
        self.assertEqual(self.firm.email, "questions@lobbyinginc.com")

    def test_get_address(self):
        """get_address method returns the firm's street address"""
        self.assertEqual(self.firm.get_address(), "The Penn Building, " +
            "Philadelphia, PA, 19107")

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
            unique_clients.append(client.pk)

        # Test uniqueness
        self.assertEqual(len(unique_clients), len(set(firm.get_clients())))

        # Test client list is inclusive, and includes no duplicates
        principal1 = Principal.objects.get(pk=4)
        principal2 = Principal.objects.get(pk=5)

        filing1 = Filing.objects.create(quarter='Q1', principal=principal1)
        filing1.save()
        filing1.firms.add(self.firm)
        filing2 = Filing.objects.create(quarter='Q2', principal=principal1)
        filing2.save()
        filing2.firms.add(self.firm)
        filing3 = Filing.objects.create(quarter='Q1', principal=principal2)
        filing3.save()
        filing3.firms.add(self.firm)

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
            unique_topics.append(topic.pk)

        # Test uniqueness
        self.assertEqual(len(unique_topics), len(set(firm.get_topics())))

        # Test topic list is inclusive, and includes no duplicates
        principal1 = Principal.objects.get(pk=4)
        category1 = Category.objects.create(name='foo')
        category2 = Category.objects.create(name='bar')

        filing1 = Filing.objects.create(quarter='Q1', principal=principal1)
        filing1.save()
        filing1.firms.add(self.firm)
        filing2 = Filing.objects.create(quarter='Q2', principal=principal1)
        filing2.save()
        filing2.firms.add(self.firm)

        Expenditure.objects.create(communication=0, category=category1,
            filing=filing1)
        Expenditure.objects.create(communication=0, category=category1,
            filing=filing2)
        Expenditure.objects.create(communication=0, category=category2,
            filing=filing2)

        self.assertEqual(len(self.firm.get_topics()), 2)

        for topic in self.firm.get_topics():
            self.assertIn(topic.pk, [category1.pk, category2.pk])