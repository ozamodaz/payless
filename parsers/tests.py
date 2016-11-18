''' usage: python -m pytest tests.py
'''
import pytest
from .ua101domain import ua101domain
from .nic_ua import nic_ua
from .ukraine_com_ua import ukraine_com_ua
from .imena_ua import imena_ua

from domains_list import domains_list

prices_101 = ua101domain(domains_list)
prices_nic_ua = nic_ua()
prices_imena = imena_ua()
prices_ukraine = ukraine_com_ua()

''' Test if prices dicts not empty
'''
@pytest.mark.parametrize("provider_prices", [
    (prices_101),
    (prices_nic_ua),
    (prices_imena),
    (prices_ukraine)
])
def test_zero_length(provider_prices):
    assert len(provider_prices) > 0

''' Test if there wrong keys
'''
@pytest.mark.parametrize("provider_prices", [
    (prices_101),
    (prices_nic_ua),
    (prices_imena),
    (prices_ukraine)
])
def test_zero_length(provider_prices):
    assert '' not in provider_prices.keys()

''' Tests for NIC.UA
'''
@pytest.mark.parametrize("key, type", [
    ('com', float),
    ('укр', float),
    ('club', float),
    ('tel', float),
    ('co', float),
    ('so', float),
    ('pp.ua', float),
    ('kiev.ua', float),
    ('nikolaev.ua', float)

])
def test_nic_ua(key, type):
    assert isinstance(prices_nic_ua[key], type)

''' Tests for IMENA.UA
'''
@pytest.mark.parametrize("key, type", [
    ('com', float),
    ('укр', float),
    ('academy', float),
    ('zone', float),
    ('cherkassy.ua', float),
    ('zt.ua', float),
    ('aero', float),
    ('travel', float),
    ('ae', float),
    ('co.za', float)
])
def test_imena(key, type):
    assert isinstance(prices_imena[key], type)

''' Tests for UKRAINE.COM.UA
'''
@pytest.mark.parametrize("key, type", [
    ('com', float),
    ('укр', float),
    ('biz', float),
    ('biz.ua', float),
    ('tv', float),
    ('cherkassy.ua', float),
    ('zhitomir.ua', float),
    ('academy', float),
    ('ae.org', float),
    ('za.com', float)
])
def test_ukraine(key, type):
    assert isinstance(prices_ukraine[key], type)

''' Tests for 101DOMAIN.UA
'''
@pytest.mark.parametrize("key, type", [
    ('com', float),
    ('укр', float)
])
def test_ua101domain(key, type):
    assert isinstance(prices_101[key], type)
