import requests as rq
import pandas as pd
stocks = pd.read_csv('stock.csv')
stocklist= stocks.to_dict(orient='records')

for i in stocklist:
    cUrl = 'https://api.coinbase.com/v2/exchange-rates'
    cHeader = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
    }
    currency=i['currency']
    cParams={
         "currency" :currency 
        }
    cResp = rq.get(url=cUrl, headers=cHeader,params=cParams)
    cData = cResp.json()
    INRrates= cData['data']['rates']['INR']
    i['INRValue'] = i['price'] * float(INRrates)
print(stocklist)
A=pd.DataFrame(stocklist)
A.to_csv('StockinINR')
