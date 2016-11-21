from grab import Grab
g = Grab()


def ukraine_com_ua():
    prices = {}
    g.go('http://www.ukraine.com.ua/domains/')
    for i in range(1000):
        try:
            tld_xpath = '//*[@id="domain_zone_item_%s"]/div[1]/label/text()' % i
            price_xpath = '//*[@id="domain_zone_item_%s"]/div[2]/a/span' % i
            tld = g.doc.select(tld_xpath).text()  # lower case without dot
            price = g.doc.select(price_xpath).text()
            prices[tld] = float(price)
        except IndexError:
            pass
    return prices


if __name__ == '__main__':
    prices = ukraine_com_ua()
    for tld in prices:
        print('{:<20s}{:>8} '.format(tld, prices[tld]))
    print(len(prices))
    # 326 TLDs
