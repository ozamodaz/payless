from grab import Grab
import re
log = []


def ua101domain(all_domains):
    prices = {}
    g = Grab()

    def error_handler(g):
        message = 'Unknown Error'
        known_err = (
            '//*[@id="single_header"]/div[2]/div[2]/div/div/p',                 # Registration Unavailable
            '/html/body/div[1]/div/div[3]/div/section[3]/div/div[1]/span/span'  # 404
                    )
        for xpath in known_err:
            if g.doc.select(xpath).exists():
                message = g.doc.select(xpath).text()
                break
        log.append('url: {}\n{} - {}\n'.format(g.doc.url, domain, message))

    for domain in all_domains:
        path = domain.replace('.', '_').replace('-', '_')
        g.go('https://www.101domain.ua/%s.htm' % path)
        if g.doc.select('//*[@id="price_dropdown"]/a').exists():
            price = g.doc.select('//*[@id="price_dropdown"]/a').text()
            price = re.search('[0-9] ?[0-9]+.[0-9]{2}', price).group()
            price = float(price.replace(' ', ''))
            prices[domain] = price
        else:
            error_handler(g)
    return prices


if __name__ == '__main__':
    import test
    test.test_ua101domain
