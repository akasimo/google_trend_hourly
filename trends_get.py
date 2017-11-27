from pytrends.request import TrendReq
import pandas as pd
import time
from random import randint

pytrend = TrendReq()

# neyi arıyoruz
kw_list=['bitcoin']

# tarih gir, o tarihten sonra kaç saat istiyorsan periods kısmını değiştir

stamps = pd.date_range('2017-10-10', periods=24, freq='H')
times = stamps.strftime("%Y-%m-%dT%H")
timeframe1=str(times[0])+" "+str(times[1])

pytrend.build_payload(kw_list=kw_list,timeframe=timeframe1)
df = pytrend.interest_over_time()

for i in range(1,len(times)-1):
    wait=randint(1,5)
    print("Periyot {}, {} saniye bekle".format(i,wait))
    time.sleep(wait)

    timeframe=str(times[i])+" "+str(times[i+1])
    pytrend.build_payload(kw_list=kw_list,timeframe=timeframe)
    _ = pytrend.interest_over_time()
    df = df.append(_)

df.to_csv("trends.csv")
