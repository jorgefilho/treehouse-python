

def add_list(any_list):
  total = 0
  for i in any_list:
    total = total + i
  return total

def summarize(any_list):
  total = str(add_list(any_list))  

  temporary = list()
  for i in any_list:
  	temporary.append(str(i))

  value = "[" + ', '.join(temporary) + "]"
  result = "The sum of {} is {}.".format(value, total)
  return result

add_list([1, 2, 3])

summarize([5, 1, 2])