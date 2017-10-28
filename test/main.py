from ic_sdn.models.db import Db
from ic_sdn.models.Controller import Controller

database = Db()

c = Controller()

print c.all()