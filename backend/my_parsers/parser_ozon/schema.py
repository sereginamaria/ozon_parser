from dataclasses import dataclass

@dataclass(frozen=False)
class Product:
    id: int
    name: str
    price_original: str
    price: str
    price_with_ozon_card: str
    images: str
    brand_name: str
    brand_link: str
    rating: str
    categories: str
    sizes: str
    color: str
    article: str
    all_articles: str
    url: str
    publication_category: str
    description: str
    sub_category: str
