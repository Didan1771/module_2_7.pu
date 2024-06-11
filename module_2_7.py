
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c = [1,2,3])

value_list = (10, 'text', False)
value_dict = {'a':5, 'b':'крыс', 'c':[4,5,6]}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [20, 'monkey']
print_params(*value_list_2, 66)

