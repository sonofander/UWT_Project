import pandas as pd
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2016,6,1)
end = datetime.datetime.today()
uwt = web.DataReader('UWT', "google", start, end)

print type(uwt)
