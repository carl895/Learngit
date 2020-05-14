from random import randint,sample
lst = [randint(0,50) for _ in range(100)] # 从0到49中抽取100个
print(lst[0:5])

lst_sample = sample(lst,10) # 从100个中抽取10个
print(lst_sample)