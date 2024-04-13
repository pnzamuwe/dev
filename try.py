# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# zipped = zip(number, months)
# print(type(zipped))
# for x in zipped:
#     print(x)

# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)

bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)