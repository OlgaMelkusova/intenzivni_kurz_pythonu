sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
soucet = 0
for nazev, prodano in sales.items():
    soucet = soucet + prodano
print(f"Bylo prodáno {soucet} kusů knih. ")
