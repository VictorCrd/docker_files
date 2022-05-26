jr = int(input("Jours restant: \n"))
v = int(input("Vacances restantes: \n"))
rtt = int(input("rtt a poser: \n"))
da = int(input("jours potentiel de départ avant le 1 juillet: \n"))
jw = int(input("week-end restant : \n"))*2
jf = int(input("jours fériés avant le 1 juillet: \n"))
jt = jr - v - rtt - da - jw - jf

print("Il reste " + str(jr) + " jours avant le départ \n" +
      "Vacances: " + str(v) + "\n" +
      "jours week end: " + str(jw) + "\n" +
      "jours fériés: " + str(jf) + "\n" +
      "Il reste " + str(jt) + " jours de travail \n"
      )

dq = input("press enter a key to quit or close window: \n")
