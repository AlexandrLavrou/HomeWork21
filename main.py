from extender import storage_list
from request import Request


user_text = "Со storage_1 в shop_1 перенести 2 Телефон"
req = Request(storage_list, user_text)
req.move()
print(f"storage_1:{storage_list[0]}")
print(f"storage_2:{storage_list[1]}")
print(f"shop_1:{storage_list[2]}")

# while True:
# 	print("Текущие площади:")
# 	print(f"storage_1:{storage_1}")
# 	print(f"storage_2:{storage_2}")
# 	print(f"shop_1:{shop_1}")
#
# 	user_text = input("Введите команду:\n")
# 	if user_text == "стоп":
# 		break
# 	else:
# 		try:
# 			req = Request(user_text)
# 			req.move()
# 		except Exception as e:
# 			print(f"error {e}")

