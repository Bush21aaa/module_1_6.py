#2
my_dict= {'mama':1952, 'papa':1953,'brother':1976,'ya':1983 }
print(my_dict)
print(my_dict.get('ya'))
print(my_dict.get('sister'))
my_dict.update({'son':2014, 'daughter':2015})
print(my_dict.pop('papa'))
print(my_dict)

#3
my_set={1,2,3,4,5,0,2,3,'Tree',2.28, 'boy',5,4}
print(my_set)
my_set.update([9,7])
print(my_set)
my_set.remove(0)
print(my_set)