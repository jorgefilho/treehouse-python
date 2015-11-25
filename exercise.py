the_list = ["a", 2, 3, 1, False, [1, 2, 3]]


the_list.insert(0, the_list.pop(3))
the_list.remove("a")
the_list.remove(False)
the_list.remove([1, 2, 3])
items =  list(range(4,21))
the_list.extend(items)