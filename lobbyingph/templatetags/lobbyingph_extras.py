from django import template

register = template.Library()


@register.filter(name='quarter')
def quarter(tDate):
    """Returns the quarter for a given year as
    Q12012, for example"""

    return 'Q' + str((tDate.month - 1) / 3 + 1) + str(tDate.year)
