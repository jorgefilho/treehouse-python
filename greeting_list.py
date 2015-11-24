full_name = "Jorge Filho"
name_list = full_name.split()

greeting_list = "Hi, I'm Treehouse".split()

temporary = list()
for item in greeting_list:
  if item == 'Treehouse':
    temporary.append(name_list[0])
  else:
    temporary.append(item)
  greeting_list = temporary

greeting = ' '.join(greeting_list)