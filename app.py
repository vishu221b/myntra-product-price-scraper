"""Created by Vishal Dogra on 30-06-2020"""

from src import priceScrapingService
from src.constants import BASE_URL, HEADPHONES

priceScrapingService.fetch_products_and_details_from_url(
    base=BASE_URL,
    endpoints=[HEADPHONES]
)
