from grab import Grab
g = Grab()

def regnames_ua():
    prices = {}
    g.go('https://regnames.ua/ru/domeny/ceny-domenov/')
    repl = (
           (',', '.'),
           (' ', '')
           )
    index = ((x, y) for x in range(1, 6) for y in range(1, 500))
    for table, row in index:
        try:
            tld_xpath = '//*[@id="content"]/div[2]/div[1]/section[2]/div/div/div/div[2]/div[1]/div[%s]/table/tbody/tr[%s]/td[1]/a' % (table, row)
            price_xpath = '//*[@id="content"]/div[2]/div[1]/section[2]/div/div/div/div[2]/div[1]/div[%s]/table/tbody/tr[%s]/td[3]' % (table, row)
            #import ipdb; ipdb.set_trace()
            tld = g.doc.select(tld_xpath).text().lower()[1:]
            price = g.doc.select(price_xpath).text().split(' UAH')[0]
            for i in repl:
                price = price.replace(*i)
            prices[tld] = float(price)
        except IndexError:
            pass
    return prices


if __name__ == '__main__':
    prices = regnames_ua()
    for tld in prices:
        print('{:<20s}{:>8} '.format(tld, prices[tld]))
    print(len(prices))
