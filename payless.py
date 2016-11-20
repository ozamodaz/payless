import datetime
import parsers
import shelve


def get_data(force_refresh=False):
    db = shelve.open('data')

    def sort_providers(data):
        cmp_result = {provider: 0 for provider in data.keys()}
        sets = (set(data[provider].keys()) for provider in data)
        cmp_domains = set.intersection(*sets)

        for domain in cmp_domains:
            compare = ((data[provider][domain], provider) for provider in data)
            cheaper = min(compare)
            cmp_result[cheaper[1]] += 1

        order = sorted(cmp_result, key=cmp_result.get, reverse=True)
        return order, cmp_domains, cmp_result

    def refresh():
        data = {}
        for provider in parsers.lst:
            data[provider.__name__] = provider()
        sets = (set(data[provider].keys()) for provider in data)
        all_domains = set.intersection(*sets)
        data['ua101domain'] = parsers.ua101domain(all_domains)
        db['data'] = data
        db['order'], db['cmp_domains'], db['cmp_result'] = sort_providers(data)
        db['creation_date'] = datetime.datetime.now()
        return db

    if force_refresh:
        return refresh()
    try:
        created = db['creation_date']
        if len(parsers.lst) + 1 != len(db['data']):
            return get_data(force_refresh=True)
        elif datetime.datetime.now() - created < datetime.timedelta(days=1):
            return db
        else:
            return refresh()
    except KeyError:
        return refresh()
