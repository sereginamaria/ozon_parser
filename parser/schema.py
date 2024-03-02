from dataclasses import dataclass

@dataclass(frozen=False)
class Product:
    name: str
    price_original: str
    price: str
    price_with_ozon_card: str
    images: str
    brand_name: str
    brand_link: str
    rating: str
    categories: str
    color: str
    article: str
    sizes: str
    all_articles: str
    publication_category: str
    few_photos: bool
    url: str
    description: str
    subcategory: str
