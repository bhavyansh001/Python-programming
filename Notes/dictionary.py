# order isn't important like list and strings, Mutable
chai_types = {"Masala":"Spicy",
              "Ginger":"Zesty",
              "Green":"Mild"}
print(chai_types)

print(chai_types["Ginger"])
print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai) # gives keys

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"

print(chai_types)

chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem() # last element

del chai_types["Green"] # remove memory reference as well

chai_types_copy = chai_types.copy()

squared_num = {x:x**2 for x in range(6)}
print(squared_num)

# construct dictionary
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)