numbers=[1,2,3,4,5,3,2,5,4,2,1,4,3,2]
print(numbers)
print(type(numbers))

#Set is nothing but unique objects.
sample_set = set(numbers)  
print(sample_set)
print(type(sample_set))

if 6 in sample_set:
    print("Number 6 Exists!")
else:
    print("Number 6 doesn't exist")

mySet = set([])
mySet.add(92)
mySet.add(67)
mySet.add(97)
mySet.add(39)
mySet.add(35)

print(mySet)

mySet.remove(35)
mySet.remove(92)

print(mySet)

#mySet.remove(100)- remove will throw error, if the element is not present in this set
#Discard will not throw error even if the number doesn't exist in this set:
mySet.discard(100)

print(mySet)

#Set Operations
#1) Union
#2) Intersection
#3) Difference
#4) Symmetric Difference

a = {1,2,3,4,5}
b = {4,5,6,7,8}

#Union is combining two sets together
print(a.union(b))
print(a|b)

#Intersection is the common number between two sets
print(a.intersection(b))
print(a & b)

#Difference of A and B is the elements that exist in A but not in B
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a)

#Symmetric difference is the (union of sets - intersection of sets) - removes the common terms
print(a.symmetric_difference(b))
print(a^b)