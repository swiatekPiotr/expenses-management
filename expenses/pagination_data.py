"""

adding data to href pagination redirect

"""


def form_pagination_data(get_data):
    get_data['date_from'] = str(get_data['date_from'])
    get_data['date_to'] = str(get_data['date_to'])

    category_substitute = ''
    for i in get_data['categories']:
        category_substitute += f'&categories={i}'

    pagination_url = \
        str(get_data) \
        .replace(f", 'categories': {get_data['categories']}", category_substitute) \
        .replace('{', '?') \
        .replace(':', '=') \
        .replace(',', '&') \
        .replace('None', '') \
        .translate({ord(i): None for i in "' }"})
    return pagination_url
