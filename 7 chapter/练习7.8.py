sandwich_orders = ['san1','san2','san3']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\n i made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
for san in finished_sandwiches:
    print(san)
