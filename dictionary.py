# belajar Tipe Data Dictionary

customer = {"Name": "Eko", "Age": 30, "Address": "Subang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Address"]

customer["Company"] = "X"
customer["Name"] = "Kurniawan"

del customer["Address"] # menghapus data

for key, value in customer.items():
    print(f"{key}:{value}")