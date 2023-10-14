pages = 100
lines = 50
symbols = 25
for_save_symbol = 4
volume_in_mb = 1.44
volume_in_b = volume_in_mb * 1024 * 1024
volume_one_book = pages * lines * symbols * for_save_symbol
result = int(volume_in_b // volume_one_book)

print("Количество книг, помещающихся на дискету:", result)
