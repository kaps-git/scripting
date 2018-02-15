#!/usr/local/bin/python3
import sys, re, datetime
import requests
from bs4 import BeautifulSoup

## Define list of Stocks to get data
arrWatchList = ['FB', 'AAPL', 'TSLA']
urlYFinance = 'https://finance.yahoo.com/quote/'

out = open('../testdata_python/stockInfo.txt', 'a+')
now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')
pattern1 = re.compile("\d+\.\d+")                          ##Pattern to Extract only float number from string

#print("{:>10s},{:>10s},{:>10s},{:>10s},{:>10s},{:>10s}".format('Date', 'Stock','#Short', 'Short Ratio', 'Short %', '#Short PrevMonth'), file=out)
print("{:>s},{:>s},{:>s},{:>s},{:>s},{:>s}".format('Date', 'Stock','#Short', 'Short Ratio', 'Short %', '#Short PrevMonth'), file=out)

## For each stock, get Yahoo Finance Statistics page
for stock in arrWatchList:
   
    url = urlYFinance + stock + '/key-statistics'
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")

    ## From Statistics page, find values of Shares Short now ,  Shares Short (prior month), Short % of Float , Short Ratio,
    
    ## Count of shares short
    span1 = soup.find("span", string="Shares Short")
    tr1 = span1.find_parent("tr")
    sharesShort = pattern1.search(tr1.select_one("td.Fz(s)").string).group(0)                    ##Extract only float number from string
    
    ## Short Ratio 
    span2 = soup.find("span", string="Short Ratio")
    tr2 = span2.find_parent("tr")
    shortRatio = tr2.select_one("td.Fz(s)").string
    
    ##Short % of Float
    span3 = soup.find("span", string="Short % of Float")
    tr3 = span3.find_parent("tr")
    shortPercent = tr3.select_one("td.Fz(s)").string
     
    ##Shares Short (prior month) 
    span4 = soup.find("span", string="Shares Short (prior month)")
    tr4 = span4.find_parent("tr")
    shortPriorMonth = pattern1.search(tr4.select_one("td.Fz(s)").string).group(0)                ##Extract only float number from string
  
    #print("{:>10s},{:>10s},{:>10s},{:>10s},{:>10s},{:>10s}".format(today, stock ,sharesShort, shortRatio, shortPercent, shortPriorMonth), file=out)
    print("{:>s},{:>s},{:>s},{:>s},{:>s},{:>s}".format(today, stock ,sharesShort, shortRatio, shortPercent, shortPriorMonth), file=out)


## close ile.
out.close()