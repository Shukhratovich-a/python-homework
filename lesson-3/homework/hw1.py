# 1
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[2])

# 2
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# 3
nums = [10, 20, 30, 40, 50]
new_list = [nums[0], nums[len(nums)//2], nums[-1]]
print(new_list)

# 4
movies = ["The lord of the rings", "Back to the future", "La la land", "Catch me if you can", "Green mile"]
movies_tuple = tuple(movies)
print(movies_tuple)

# 5
cities = ["London", "Paris", "New York", "Tokyo"]
print("Paris" in cities)

# 6
nums = [1, 2, 3]
dup = nums * 2
print(dup)

# 7
nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

# 8
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(t[3:8])

# 9
colors = ["blue", "red", "blue", "green", "blue"]
print(colors.count("blue"))

# 10
animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))

# 11
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)

# 12
lst = [1, 2, 3, 4]
t = (5, 6, 7)
print(len(lst), len(t))

# 13
t = (10, 20, 30, 40, 50)
lst = list(t)
print(lst)

# 14
t = (8, 2, 9, 3, 7)
print(max(t), min(t))

# 15
words = ("hello", "world", "python", "rocks")
print(words[::-1])
