# Lists are mutable, we needed something immutable as well, here comes tuple

tea_types = ("Black", "Green", "Oolong")
print(tea_types)

print(tea_types[0])
# tea_types[0] = "Else" # won't work
print(tea_types[0])

more_tea = ("Earl Grey", "Herbal")

all_tea = tea_types + more_tea
print(all_tea)

if "Green" in all_tea:
    print("I have green tea!")

more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea.count("Herbal"))

(bl, gr, ool) = tea_types # number of params received should be known, so that left hand side vars can be used for assigning, tuples can be used for unwrapping, as such.
print(bl)

print(type(tea_types))

