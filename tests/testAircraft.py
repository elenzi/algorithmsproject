
from algorithmsproject.aircraft import Aircraft, Airplane, Helicopter

aircraft1=Aircraft('E1100')
airplane2=Airplane('E1199')
heli1=Helicopter('HH123')

print("Created 3 Objects")


unusedFuel=aircraft1.add_fuel(10000)
print("Fuel leftover for", aircraft1.flight_number, ": ", unusedFuel)
unusedFuel=airplane2.add_fuel(10000)
print("Fuel leftover for", airplane2.flight_number, ": ", unusedFuel)
unusedFuel=heli1.add_fuel(10000)
print("Fuel leftover for", heli1.flight_number, ": ", unusedFuel)


myJumbo= Airplane('747')
print("About to start preparing", myJumbo.flight_number, "for takeoff.")
myJumbo.add_fuel(30)
myJumbo.fuel_check()
myJumbo.take_off()

print("----")

myairbus= Airplane("A330")
print("About to start preparing", myairbus.flight_number, "for takeoff.")
myairbus.add_fuel(2000)
myairbus.fuel_check()
myairbus.take_off()


print("----")


myBoeing = Helicopter("HH2")
print("About to start preparing", myBoeing.flight_number, "for takeoff.")
fuelInTruck = 50000
fuelInTruck = myBoeing.add_fuel(fuelInTruck)
myBoeing.fuel_check()
myBoeing.take_off()
print("Fuel Truck still has", fuelInTruck)

