AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
def menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter the following number below from the following menu:")
  print()
  print("1. PRINT all Authorized Vehicles")
  print("2. Exit")

menu()
menuchoice = input()

if menuchoice == "1" or menuchoice == "2":
  if menuchoice == "1":
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for c in range(len(AllowedVehiclesList)):
      print(AllowedVehiclesList[c])
  if menuchoice == "2":
    quit("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
else:
  print("\nInvalid choice")
  