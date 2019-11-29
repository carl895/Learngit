import copy
spam = [0,1,2,3]
cheese = copy.deepcopy(spam)
cheese[1] = "A"
print(spam)
print(cheese)