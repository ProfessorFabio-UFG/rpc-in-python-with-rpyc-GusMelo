import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

  def exposed_CtoF(self, c):
    return (c * 9/5) + 32

  def exposed_FtoC(self, f):
    return (f - 32) * 5/9

  def exposed_KMtoMiles(self, km):
    return km * 0.621371

  def exposed_MilestoKM(self, miles):
    return miles / 0.621371

  def exposed_KGtoLB(self, kg):
    return kg * 2.20462

  def exposed_LBtoKG(self, lb):
    return lb / 2.20462

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()


