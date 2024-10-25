# = Array
# Mutable

tea_varities = ["Black", "Green", "Oolong", "White"]

print(tea_varities)
print(tea_varities[1])
print(tea_varities[:2])
print(tea_varities[2:])

tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities[1:3] = ["Green", "Masala"] # notice passed array, as when using slicing syntax, var is treated as array

print(tea_varities)

tea_varities[1:1] = ["test", "test"]
# gets copied from index 1, others shift
print(tea_varities)

tea_varities[1:3] = [] # insert nothing aka delete operation
print(tea_varities)

for tea in tea_varities:
    print(tea + " Tea")

for tea in tea_varities:
    print(tea, end="-")  # default end is \n

if "Oolong" in tea_varities:
    print("I have Oolong Tea")
else:
    print("Nope I don't")

tea_varities.append("Oolong")

if "Oolong" in tea_varities:
    print("I have Oolong Tea")
else:
    print("Nope I don't")

tea_varities.pop()
tea_varities.remove("Herbal")
print(tea_varities)

tea_varities.insert(1, "Herbal")
print(tea_varities)

tea_varities_copy = tea_varities # this will have same reference, mutating one will mutate other, to copy:
tea_varities_copy = tea_varities.copy  # this is used to have different references, it is an actual copy


squared_nums = [x**2 for x in range(10)]
print(squared_nums)