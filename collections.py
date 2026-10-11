
# =================================
# 1. LIST
# Ordered, mutable, allows duplicates
# =================================

my_list = [1, 2, 3, 'apple', 4.5]

print("----- LIST -----")
print("Original list:", my_list)

my_list.append("banana")
print("After append:", my_list)

my_list[0] = 100
print("After update:", my_list)

my_list.remove(2)
print("After remove:", my_list)

print("First item:", my_list[0])


# =================================
# 2. TUPLE
# Ordered, immutable, allows duplicates
# =================================

my_tuple = (1, 2, 3, 'banana', 4.5)

print("\n----- TUPLE -----")
print("Tuple:", my_tuple)

print("First item:", my_tuple[0])
print("Tuple length:", len(my_tuple))
print("Count of 2:", my_tuple.count(2))
print("Index of banana:", my_tuple.index("banana"))

# Tuples cannot be modified directly


# =================================
# 3. SET
# Unique items, mutable, unordered
# =================================

my_set = {1, 2, 3, 'orange'}

print("\n----- SET -----")
print("Original set:", my_set)

my_set.add("apple")
print("After add:", my_set)

my_set.discard(2)
print("After discard:", my_set)

my_set.update({4, 5})
print("After update:", my_set)

another_set = {3, 4, 5, 6}
print("Union:", my_set.union(another_set))
print("Intersection:", my_set.intersection(another_set))


# =================================
# 4. DICTIONARY
# Key-value pairs, mutable
# =================================

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

print("\n----- DICTIONARY -----")
print("Original dictionary:", my_dict)

print("Name:", my_dict['name'])

my_dict['age'] = 26
print("After update:", my_dict)

my_dict['country'] = 'USA'
print("After adding country:", my_dict)

my_dict.pop('city')
print("After removing city:", my_dict)

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())

# Loop through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")