def reverse_(lst):
    if len(lst) < 1:
        return ""
    return reverse_(lst[1:]) + lst[0]

name = "Fudji"

a = [[96], [69]]
print(''.join(list(map(str, a))))
print(reverse_(name))
z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)

def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)

def aa(some, 5):
   return

aa(a)

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)