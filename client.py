import rpyc
from constRPYC import *

class Client:
  conn = rpyc.connect(SERVER, PORT)

  print("Lista atual:", conn.root.exposed_value())
  conn.root.exposed_append(5)
  conn.root.exposed_append(6)
  print("Lista atualizada:", conn.root.exposed_value())

  print("Conversões remotas:")
  print("CtoF(100) =", conn.root.exposed_CtoF(100))
  print("FtoC(212) =", conn.root.exposed_FtoC(212))
  print("KMtoMiles(10) =", conn.root.exposed_KMtoMiles(10))
  print("MilestoKM(6.2) =", conn.root.exposed_MilestoKM(6.2))
  print("KGtoLB(70) =", conn.root.exposed_KGtoLB(70))
  print("LBtoKG(154) =", conn.root.exposed_LBtoKG(154))

