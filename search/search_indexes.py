from haystack import indexes
from lobbyingph.models import Principal, Firm, Lobbyist, Official


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


class LobbyistIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return Lobbyist
    
    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class OfficialIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Official

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

