from .nic_ua import nic_ua
from .ukraine_com_ua import ukraine_com_ua
from .imena_ua import imena_ua
from .ua101domain import ua101domain

'''You should not put ua101domain in following list because
this parser requires a set of domain names. This set is being generated
dynamically as a union of domains of all providers.
'''
lst = [nic_ua, ukraine_com_ua, imena_ua]
