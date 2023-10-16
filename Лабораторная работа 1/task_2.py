disk_capacity = 1.44 * 1024 * 1024

book_capacity = 100 * 50 * 25 * 4

count_of_books = int(disk_capacity // book_capacity)

print("Количество книг, помещающихся на дискету:", count_of_books)

