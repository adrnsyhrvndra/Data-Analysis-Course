avenger = ['Iron Man','Captain America','Thor','Hulk','Black Widow','Hawkeye']
numbers = [1,2,3,4,5,6]

# Extends Untuk Menggabungkan List
avenger.extend(numbers)

print('=========================')

# Append Untuk Menambahkan List
avenger.append('Black Panther')

print('=========================')

# Insert Untuk Menganti Di Index Tertentu
avenger.insert(2,'Captain Marvel')

print('=========================')

# Remove Untuk menghapus Di Index Tertentu
avenger.remove('Hulk')

print('=========================')

# Pop Untuk menghapus Di List index terakhir
avenger.pop()

print('=========================')

# To Count
print(avenger.count('Iron Man'))

# To Sort And Make It Descending.
avenger.sort(reverse = True)

print(avenger)

# To make it copy
new_list = numbers.copy()
print(new_list)