print("How many bars should be charged?")
bars_to_charge = int(input())


bars_charged = 0

print()

while (bars_charged < bars_to_charge):
    bars_charged = bars_charged + 1
    print("Charging:", "II" * bars_charged)
    
print("The battery is fully charged.")        