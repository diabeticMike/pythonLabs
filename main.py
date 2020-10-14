# # 1
# firstName = 'Mykhailo'
# lastName = 'Tkachuk'
# group = 'PM-41'
# print(firstName, ' ', lastName, ' ', group)

# # 2
# print('Enter your firstname')
# firstName = input()
# print('Enter your lastname')
# lastName = input()
# print('Enter your group')
# group = input()
# print(firstName, ' ', lastName, ' ', group)

# # 3
# print('Enter size (width*height)')
# w = int(input())
# h = int(input())
# print('Carpet has area:', w*h)

# # 4
# print('Enter size (width*height)')
# w = int(input())
# h = int(input())
# print('Enter carpenter price')
# p = int(input())
# print('Carpet has area(in cm^2):', w*h)
# print('Carpet has area(in m^2):', w*h/10000)
# print('Carpet has price:', w*h/10000*p)

# # 5
# res = 1
# for i in range(2,20):
#     res*=i
# print(res)

# # 6
# for i in range(100):
#     print('A', end='')

# # 7
# for i in range(100):
#     print('Python', end='')

# # 8
# v = ''
# for i in range(50):
#     v += str(179)
# print(int(v)**2)

# # 9
# print('Enter your name')
# name = input()
# print('Hello, ', name,'!', sep='')

# # 10
# print(103,25,14, sep='\n')

# # 11
# print('%.2f'% 156.12459835)

# # 12
# print('%10.3f'%(7.240),'%9.3f'%-43.520)
# print('%10.3f'%(23.500),'%8.2f'%55.10)
# print(7)
# print('%10.3f'%(88.203),'%9.3f'%-769.800)

# # 13
# print('{:3d}\n'.format(103), '{:2d}\n'.format(24), '{:2d}'.format(14))
# print('{:.2f}'.format(156.12459835))
# print('{:10.3f}'.format(7.240),'{:9.3f}'.format(-43.520))
# print('{:10.3f}'.format(23.500),'{:8.2f}'.format(55.10))
# print('{:}'.format(7))
# print('{:10.3f}'.format(88.203),'{:9.3f}'.format(-769.800))

# # 14
# a = 2
# b = 4
# if a < b and a > 1:
#     print('true')
# else:
#     print('false')
# x = 'abc'
# y = 'a'
# if x < y or y == 'abc':
#     print('true')
# else:
#     print('false')
# # Строки мають лексикографічну властивість, тому ми відповідно можемо їх порівняти