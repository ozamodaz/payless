from grab import Grab
g = Grab()

def imena_ua():
    prices = {}
    g.go('http://www.imena.ua/site/domains/prices')
    index = ((x, y) for x in range(1, 5) for y in range(1, 500))
    for table, row in index:
        try:
            tld_xpath = '/html/body/div[1]/section/div/table[%s]/tr[%s]/td[1]/a' % (table, row)
            if table == 5:
                price_xpath = '/html/body/div[1]/section/div/table[%s]/tr[%s]/td[5]/div' % (table, row)
            else:
                price_xpath = '/html/body/div[1]/section/div/table[%s]/tr[%s]/td[4]/div' % (table, row)
            #import ipdb; ipdb.set_trace()
            tld = g.doc.select(tld_xpath).text().lower()
            price = g.doc.select(price_xpath).text()
            prices[tld] = float(price.split(' ')[0])
        except IndexError:
            pass
    return prices


if __name__ == '__main__':
    prices = imena_ua()
    for tld in prices:
        print('{:<20s}{:>8} '.format(tld, prices[tld]))
    print(len(prices))
# 339 TLDs
