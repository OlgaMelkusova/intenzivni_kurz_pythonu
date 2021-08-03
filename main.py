item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
item ["price"] = 929
print("Cena položky je ", item["price"], ".", sep="")
print("Cena položky je " + str (item ["price"])+".")
print (f"Cena položky je {item ['price']}.")
item["weight"] = 0.5
if "weight" in item:
    print(f"Hmotnost je {item['weight']} kg.")
else:
    print ("Hmotnost není zadaná.")
# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
# sausages.pop("Adam")
# print(len(sausages))
