#The bottle shipping problem
bottles = int(input("Enter the number of bottles:"))
carton_sizes = {'XL': 48,
    'Large': 24,
    'Medium': 12,
    'Small': 6
}
cartons_used = {}
for carton, capacity in carton_sizes.items():
    num_cartons = bottles // capacity
    if num_cartons > 0:
        cartons_used[carton] = num_cartons
    bottles %= capacity
for carton, count in cartons_used.items():
    print(count,carton,end=", ")
