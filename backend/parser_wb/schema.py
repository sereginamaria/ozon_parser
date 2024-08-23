from dataclasses import dataclass

@dataclass(frozen=False)
class Product:
    id: int
    name: str
    price_original: str
    price: str
    images: str
    brand_name: str
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
