# 1
name = input("Enter your name: ")
year = int(input("Enter your birth year: "))
age = 2025 - year
print(name, "is", age, "years old")

# 2
txt = 'LMaasleitbtui'
car1 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] + txt[10] + txt[12] # lacetti
car2 = txt[1] + txt[3] + txt[5] + txt[7] + txt[9] + txt[11] # malibu
print(car1, car2)

# 3
txt = 'MsaatmiazD'
car1 = txt[0] + txt[2] + txt[4] + txt[6] + txt[8] # matiz
car2 = txt[9] + txt[2] + txt[5] + txt[7] + txt[1] # damas
print(car1, car2)

# 4
txt = "I'am John. I am from London"
print(txt.split("from ")[1])

# 5
s = input("Enter text: ")
print(s[::-1])

# 6
s = input("Enter text: ")
count = 0
for i in s.lower():
    if i in 'aeiou':
        count += 1
print("Vowels:", count)

# 7
nums = list(map(int, input("Enter numbers: ").split()))
print("Max:", max(nums))

# 8
w = input("Enter word: ")
if w == w[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# 9
email = input("Enter email: ")
print("Domain:", email.split('@')[1])

# 10
import random, string
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.sample(chars, 10))
print("Password:", password)