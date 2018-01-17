from bs4 import BeautifulSoup
import requests
import time

def breaks(title):
    print('---------------------------')
    print('|^|'+title+'|^|')
    print('---------------------------')

# Get USD -> SGD Exchange Rate from Google Finance
breaks('USD to SGD Exchange Rate')

fin_google_r = requests.get('https://finance.google.com/finance/converter?a=1&from=USD&to=SGD&meta=ei%3D_OheWvmZFNDVuASSj5T4Ag')
fg_html_text = fin_google_r.text
fg_soup = BeautifulSoup(fg_html_text, 'html.parser')
usd_sgd_ex_rate = float((fg_soup.find('span', {'class':'bld'}).get_text()).replace(' SGD',''))
print('Current Exchange Rate from 1 USD to SGD is ' + str(usd_sgd_ex_rate) + ' SGD')


# Get Ethereum Price from cryptoprice.trade
breaks('Ethereum Price from CryptoPirce.trade')

cp_r = requests.get('https://marketools.plus500.com/Feeds/UpdateTable?instsIds=3407')
cp_json = cp_r.json()
cp_ether_price = float(cp_json['Feeds'][0]['S']) * usd_sgd_ex_rate
print("Timestamp : " + str(time.strftime('%d-%m-%Y %l:%M%p')))
print("")
print("1 Ethereum in SGD - {0:.2f} SGD".format(cp_ether_price))
print("1 SGD in Ethereum - {0:.8f} Ethereum".format(1/cp_ether_price))

# Get Ethereum Price from coinmarketcap.com
breaks('Ethereum Price from CoinMarketCap.com')

cm_r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
cm_json = cm_r.json()
cm_ether_price = float(cm_json[0]['price_usd']) * usd_sgd_ex_rate
print("Timestamp : " + str(time.strftime('%d-%m-%Y %l:%M%p')))
print("")
print("1 Ethereum in SGD - {0:.2f} SGD".format(cm_ether_price))
print("1 SGD in Ethereum - {0:.8f} Ethereum".format(1/cm_ether_price))

# Get Ethereum Price from crytoprice.co
breaks('Ethereum Price from CryptoPrice.co')

cpo_r = requests.get('https://cryptoprice.co/coin/ETH')
cpo_html_text = cpo_r.text
cpo_soup = BeautifulSoup(cpo_html_text, 'html.parser')
cpo_ether_price = float(cpo_soup.find('span',{'class': 'tooltip'}).get_text().replace(',','')) * usd_sgd_ex_rate
print("Timestamp : " + str(time.strftime('%d-%m-%Y %l:%M%p')))
print("")
print("1 Ethereum in SGD - {0:.2f} SGD".format(cpo_ether_price))
print("1 SGD in Ethereum - {0:.8f} Ethereum".format(1/cpo_ether_price))


breaks('Average ETH to SGD, SGD to ETH Price')

total = cp_ether_price + cm_ether_price + cpo_ether_price
print("Average Transcation Price")
print("1 Ethereum in SGD - {0:.2f} SGD".format(total/3))
print("1 SGD in Ethereum - {0:.8f} Ethereum".format(1/(total/3)))