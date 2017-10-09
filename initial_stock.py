import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
%matplotlib inline
%pylab inline


start = datetime.datetime(2016,6,1)
end = datetime.datetime.today()
uwt = web.DataReader('UWT', "google", start, end)

print type(uwt)


pylab.rcParams['figure.figsize'] = (15,9)

uwt["Adj Close"].plot(grid = True)

#candlestick plots
