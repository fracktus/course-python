numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_new = [i for i in numbers if i]

numbers_print = [(sum(numbers_new)/len(numbers) if x is None else x) for x in numbers]

print("Измененный список:", numbers_print)

