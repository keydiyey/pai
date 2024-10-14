import utils.transactions as transaction
import utils.database as database
from datetime import datetime

date = datetime.now().timestamp()


print(date)

data = database.load()

UID = "543806339785162764"
marriage_data = data[UID]['marriage'] 

marriage_data |=  {"x" : "07 - 31 - 1999"} 


database.update(data)
