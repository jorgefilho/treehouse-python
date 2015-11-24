import random

def random_member(any_list):
  items = 0
  for i in any_list:
    items = items + 1
  result = 0
  if items>0:
    result = random.randint(0, items-1)
  return  any_list[result]

random_member([1, 2])