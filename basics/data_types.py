a_int = 1  # integers, no upper/lower limit
a_int2 = -1

a_float = 1.1  # float
a_float2 = 1.0  # float assignment

print(1 / 2)  # result 0.5
print(1 // 2)  # result in int -> 0

a_str = "'test"  # string
a_str2 = '\'test'  # no difference between " and ', to print special characters use \
print(a_str2)
print(a_str2[0])  # print first letter from string
print(a_str2[1])

a_list = [1, 2, 3, "test"]
print(a_list[1])
print(a_list[-1])  # last element of list

a_list[0] = 10
print(a_list)

a_list.remove(2)  # remove value
a_list.pop(2)  # remove index
print(a_list)

a_list.append("value")  # add element
print(a_list)

b_list = [1, 2]
c_list = b_list  # reference assignment
c_list[0] = 3

print(b_list, c_list)

a_tuple = (1, 2, 3)  # tuple, not mutable, e.g. a_tuple[0] = 10 not possible
print(a_tuple[1])

a_set = {1, 2, 3, 3}  # not subscriptiable# /order, e.g. a_set[1]
print(a_set)

a_dict = {  # key -> value
 "color": "blue",
 "1": {
  "2": [1, 2, 3]
 }
}
print(a_dict["1"])

a_bool = True  # boolean (True or False)
a_bool2 = bool(1)
print(a_bool2)
a_bool3 = bool(0)
print(a_bool3)
a_bool4 = bool(-1)
print(a_bool4)
a_bool5 = bool([0])  # False if 0, [], (), {}, None
print(a_bool5)


python = {
 "colour": "mixed",
 "age": 3,
 "weight": 4.5,
 "food": ["water", "birds", "butterflies"],
 "toys": ("ball", "mouse")
}

print(python)

food1 = "pancakes"
food2 = "potatos"

text = "I like {} & {}".format(food1, food2)
print(text)

text2 = f"I like {food1} & {food2}"
print(text2)
