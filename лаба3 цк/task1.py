items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def func(i_list, f_item):
    index_item = i_list.index(f_item) if f_item in i_list else None
    return index_item

for find_item in ['банан', 'груша', 'персик']:
    index_item = func(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
