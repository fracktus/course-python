participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(p_first_group, p_second_group, sym = ","):
    first_group = p_first_group.split(sym)
    second_group = p_second_group.split(sym)
    common = list(set(first_group).intersection(second_group))
    return sorted(common)

print(find_common_participants(participants_first_group, participants_second_group, "|"))