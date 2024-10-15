import logging

import requests

from wildberries.models import Product

logger = logging.getLogger(__name__)


class WildberriesService:
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Origin': 'https://www.wildberries.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://www.wildberries.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Priority': 'u=4',
    }

    detail_url = "https://card.wb.ru/cards/v2/detail?curr=byn&dest=-6722704&nm={}"

    @classmethod
    def create_or_update_product_by_article(cls, article: int):
        """Send a request to wb by article, analyze the response and save the data in the product model"""

        # Send request
        response = requests.get(
            cls.detail_url.format(article),
            headers=cls.headers,
        )

        # Parse request
        if response.status_code == 200:
            data: dict = response.json()
            try:
                brand = data['data']['products'][0]['brand']
                name = data['data']['products'][0]['name']
                entity = data['data']['products'][0]['entity']
                supplier = data['data']['products'][0]['supplier']
                review_rating = data['data']['products'][0]['reviewRating']
                total_quantity = int(data['data']['products'][0]['totalQuantity'])
                color = None
                price = None

                if total_quantity > 0:
                    # the answer does not have this data if the product is sold out
                    color = data['data']['products'][0]['colors'][0]["name"]
                    price = float(data['data']['products'][0]['sizes'][0]['price']['total']) / 100

                Product.objects.update_or_create(
                    article=article,
                    defaults={
                        'brand': brand,
                        'name': name,
                        'entity': entity,
                        'supplier': supplier,
                        'review_rating': review_rating,
                        'color': color,
                        'price': price,
                        'total_quantity': total_quantity,
                    }
                )
            except KeyError:
                logger.error("Couldn't get data for article %s. Response data: %s", data)
        else:
            logger.error("Couldn't get data for article %s. Response code: %s", article, response.status_code)
