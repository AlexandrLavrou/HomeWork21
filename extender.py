from shop import Shop
from store import Store

storage_1 = Store(items={"Телефон": 10, "Компьютер": 10, "Телевизор": 20})
storage_2 = Store(items={"Телефон": 10, "Компьютер": 10, "Приставка": 10})
shop_1 = Shop(items={"Телефон": 3, "Компьютер": 4, "Телевизор": 2})

storage_list = [storage_1, storage_2, shop_1]