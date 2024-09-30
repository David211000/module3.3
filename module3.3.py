def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params(b=25,c=[1,2,3])
values_list=[4,'str',False]
values_dict={'a':3,'b':3.12,'c':'string'}
print_params(*values_list)
print_params(**values_dict)
values_list_2=[24,'привет']
print_params(*values_list_2,42)