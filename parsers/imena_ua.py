from grab import Grab
g = Grab()

def imena_ua():
    prices = {}
    g.go('http://www.imena.ua/site/domains/prices')
    index = ((x, y) for x in range(2, 11, 2) for y in range(1, 500))
    for table, row in index:
        try:
            tld_xpath = '/html/body/center/table[3]/tr/td[2]/table[%s]/tbody/tr[2]/td[2]/table/tbody/tr[%s]/td[1]' % (table, row)
            if table == 10:
                price_xpath = '/html/body/center/table[3]/tr/td[2]/table[%s]/tbody/tr[2]/td[2]/table/tbody/tr[%i]/td[5]/div' % (table, row)
            else:
                price_xpath = '/html/body/center/table[3]/tr/td[2]/table[%s]/tbody/tr[2]/td[2]/table/tbody/tr[%s]/td[4]/div' % (table, row)
            # import ipdb; ipdb.set_trace()
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
