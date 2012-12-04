from haystack.views import SearchView

# Subclass of SearchView
# Doing this just to add extra_context
class CustomSearchView(SearchView):

    def __name__(self):
        return "CustomSearchView"

    def extra_context(self):
        result_count = {
            'lobbyist': 0,
            'firm': 0,
            'principal': 0,
            'official': 0
        }

        for result in self.results:
            print result.content_type
            if result.content_type() == 'lobbyingph.official':
                result_count['official'] += 1
            elif result.content_type() == 'lobbyingph.lobbyist':
                result_count['lobbyist'] += 1
            elif result.content_type() == 'lobbyingph.firm':
                result_count['firm'] += 1
            elif result.content_type() == 'lobbyingph.principal':
                result_count['principal'] += 1

        extra = {
            'result_count': result_count
        }

        return extra
