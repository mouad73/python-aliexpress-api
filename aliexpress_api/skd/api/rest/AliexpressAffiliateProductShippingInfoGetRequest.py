"""
Created by mouad on 2025.01.21
"""
from ..base import RestApi


class AliexpressAffiliateProductShippingInfoGetRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.product_id = None
        self.sku_id = None
        self.ship_to_country = None
        self.target_currency = None
        self.target_sale_price = None
        self.target_language = None
        self.tax_rate = None

    def getapiname(self):
        return "aliexpress.affiliate.product.shipping.get"
