from datetime import date
from typing import Any

class Product:
    def __init__(self, name: str, expires: date) -> None:
        self.name, self.expires = name, expires
    
    @property
    def expires(self) -> date:
        return self._expires
    
    @expires.setter
    def expires(self, new_date: date) -> None:
        if not isinstance(new_date, date):
            raise TypeError(f'{new_date} must be date, not {type(new_date).__name__}')
        self._expires = new_date

class Warehouse:
    def __init__(self, products: list[Product]) -> None:
        self.products = products
    
    @property
    def products(self) -> list[Product]:
        return self._products
    
    @staticmethod
    def check_is_product(value: Any) -> None:
        if not isinstance(value, Product):
            raise TypeError('Your product is not product')

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        if not isinstance(new_products, list):
            raise TypeError(f'Products must be list, not {type(new_products).__name__}')
        for product in new_products:
            self.check_is_product(product)
        self._products = new_products
    
    def add(self, new_product: Product) -> None:
        if new_product in self.products:
            raise ValueError(f'This product already exists')
        self.check_is_product(new_product)
        self.products.append(new_product)
    
    def remove(self, old_product: Product) -> None:
        if old_product not in self.products:
            raise ValueError(f'{old_product.__name__} not in products')
        self.products.remove(old_product)
    
    def clean(self) -> None:
        self.products = list(filter(lambda product: product.expires >= date.today(), self.products))

karbonara_vega = Product('karbonara by Novikov', date(2023, 12, 6))
bedro = Product('Chicken bedro KFC', date(2023, 12, 7))

siriusuniversity = Warehouse([karbonara_vega])
siriusuniversity.add(bedro)
siriusuniversity.clean()
siriusuniversity.remove(bedro)
print(len(siriusuniversity.products))