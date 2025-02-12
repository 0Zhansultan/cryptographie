# %%
with open(r'C:\Users\Etudiant\Desktop\gitub48\cryptographie\message1.txt', 'r', encoding="utf-8") as file:
    message = file.read()

def split_list(lst, x):
    L = len(lst)
    split_size = (L + x - 1) // x
    result = []
    start = 0

    for i in range(x):
        end = start + split_size
        if end > L:
            end = L
        result.append(lst[start:end])
        start = end

    return result

def read_columns(lists):
    if not lists:
        return []

    max_length = max(len(lst) for lst in lists)
    columns = []

    for col in range(max_length):
        for row in lists:
            if col < len(row):
                columns.append(row[col])

    return columns

def filtre_list(lists, sequence):
    def contains_sequence(lst, sequence):
        for i in range(len(lst) - len(sequence) + 1):
            if lst[i:i+len(sequence)] == sequence:
                return True
        return False

    filtered_lists = [lst for lst in lists if contains_sequence(lst, sequence)]
    return filtered_lists


def split_read_and_filter_columns(lst, x):
    split_lists = split_list(lst, x)
    columns = read_columns(split_lists)
    filtered_columns = filtre_list([columns], [' ', 'e', 's', 't', ' '])
    return filtered_columns, x

# %%
# Convert the message to a list of characters
lists = [list(message)]

result = []
divisions = []
for i in range(1, len(lists[0]) + 1):
    filtered_columns, division = split_read_and_filter_columns(lists[0], i)
    if filtered_columns:
        result.extend(filtered_columns)
        divisions.append(division)

print("Liste finale filtrée contenant la séquence 'e', 's', 't':")
print(result)
print("Divisions correspondantes:")
print(divisions)
true_result = ''.join(result[-8])
print(true_result)