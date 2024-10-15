import logging

from celery import shared_task
from .services import WildberriesService

logger = logging.getLogger(__name__)


@shared_task
def add_product(article: int):
    WildberriesService.create_or_update_product_by_article(article)
    logger.info("Product with article %s added.", article)
