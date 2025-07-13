sandwich_orders = ['pastrami','san1','pastrami','san2','san3','pastrami']
print('sorry,the pastrami has been sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for value in sandwich_orders:
    print(value)