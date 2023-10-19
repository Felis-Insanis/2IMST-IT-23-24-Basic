# Variables
# ->Input
temp1 = int(input("\nDen første temperaturen i celsius er:\n\t"))
temp2 = int(input("\nDen andre temperaturen i celsius er:\n\t"))
temp3 = int(input("\nDen tredje temperaturen i celsius er:\n\t"))

# Calculation
gjennomsnittTemp = (temp1 + temp2 + temp3) / 3

# Output
print("\nGjennomsnittet av de tre verdiene er:\n", str(gjennomsnittTemp) + "°C")