import datetime
from haystack import indexes
from lobbyingph.models import Principal, Firm, Lobbyist

class PrincipalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Principal

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class FirmIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Firm

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

