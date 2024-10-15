from celery import shared_task


@shared_task
def add_product(article: int):
    print(article)
