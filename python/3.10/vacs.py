x = float(input("Vacances actuelles: \n"))
m = int(input("Mois restant avant la date de vacances: \n"))
for i in range(1, m+1):
    x = x + 2.08
    print("m + " + str(i) + " = " + str(round(x, 2)) + "j de vacances")

x = float(input("RTT actuels: \n"))
m = int(input("Mois restant avant la date de RTT: \n"))
for i in range(1, m+1):
    x = x + 0.38
    print("m + " + str(i) + " = " + str(round(x, 2)) + "j de RTT")

dq = input("press enter a key to quit or close window: \n")

# 0.7 1.08 1.46