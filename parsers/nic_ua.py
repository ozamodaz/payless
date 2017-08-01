from grab import Grab
g = Grab()


def nic_ua():
    prices = {}
    g.go('http://nic.ua/ukr/tariffs.html')
    repl = (
           (',', '.'),  # swich separator for float() conversion
           ('\xa0', ''),  # remove space separating thousands
           ('Безкоштовно', '0.0'),
           ('—', '0.0')
           )
    for element in g.css_list('.domain-name'):
        tld = element.text_content()  # lower case without dot
        price = element.getparent().getparent().getnext().text_content()
        price = price.strip(' \xa0₴\n')
        for i in repl:
            price = price.replace(*i)
        prices[tld] = float(price)
    return prices


if __name__ == '__main__':
    prices = nic_ua()
    for tld in prices:
        print('{:<20s}{:>8} '.format(tld, prices[tld]))
    print(len(prices))
# 304 TLDs
