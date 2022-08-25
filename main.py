from extender import storage_dict
from request import Request

# user_text = "С склад1 в магазин перенести 8 Телефон"
# req = Request(storage_dict, user_text)
# req.move()
# print(f"storage_1:{storage_dict['склад1']}")
# print(f"storage_2:{storage_dict['склад2']}")
# print(f"shop_1:{storage_dict['магазин']}")

while True:
    print("Формула пеерноса: Из <area№1> в <area№2> переместить <кол-во> <Товар>")
    print(f"склад1:{storage_dict['склад1']}")
    print(f"склад2:{storage_dict['склад2']}")
    print(f"магазин:{storage_dict['магазин']}")

    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
            req = Request(storage_dict, user_text)
            req.move()
        except Exception as e:
            print(f"error {e}")
