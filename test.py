import utils.transactions as transaction
import utils.database as database
from datetime import datetime

date = datetime.now().timestamp()



data = database.load()

UID = "543806339785162764"
MID = "845699992806050847"

marriage_data = data[UID]['marriage'] 

print(marriage_data)


if MID in marriage_data:
    print(True)