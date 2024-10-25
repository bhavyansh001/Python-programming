print("Hello Bhavyansh!")

def chai(n):
    print(n)

chai("name")

one = "Hello"
two = "world!"

num_list = '0123456789'
num_list[:]     # 0123456789
num_list[3:]    # 3456789
num_list[:7]    # 0123456
num_list[0:7:2] # 0246
num_list[0:7:3] # 036

# Methods:
# lower
# upper
# split (to list)
# find
# strip
# replace
# len

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {}"
print(order.format(quantity, chai_type))

# List to string: join
chai_variety = ["Lemon", "Masala", "Ginger"]
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))

chai = "Masala Chai"
for letter in chai:
    print(letter)

chai = "Masala\nChai"

raw_string = r"Masala\nChai" # now print won't print new line

chai = "Masala Chai"
print("Masala" in chai) # returns true false based on presence of "Masala"