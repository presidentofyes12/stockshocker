import yfinance as yf
import datetime

today = datetime.date.today()
datesplit = str(today).split("-")
datesplit[0] = str(int(datesplit[0])-1)
start_date = ""
for i in datesplit:
  if i != datesplit[-1]:
    start_date += (i + "-")
  else:
    start_date += i

print(start_date)

def evaluateInvestment():
  stocksymbol = input("Stock Symbol: ")
  data = yf.download(stocksymbol, start_date, today)
  beginning = data['Close'].tolist()[0]
  midpoint = data['Close'].tolist()[round(len(data['Close'].tolist())/2)]
  end = data['Close'].tolist()[-1]
  
  print("\nOne year ago, " + stocksymbol + "'s markets numbered at around " + str(beginning))
  print("Six months ago, " + stocksymbol + "'s markets numbered at " + str(midpoint))
  print("Currently, " + stocksymbol + "'s markets are at " + str(end))
  print("\n")
  
  if (beginning * 0.9) > midpoint: # > 10% decrease from beginning to midpoint (done)
    print("The " + stocksymbol + " market declined between 1 year ago and half a year ago. The decline was a " + str(round(100-((midpoint/beginning)*100), 2)) + "% decline.")
    if (midpoint * 0.9) > end:
      print("The " + stocksymbol + " market declined between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
      if round(100-((midpoint/beginning)*100), 2) < round(100-((end/midpoint)*100), 2):
        print("This means that " + stocksymbol + " is undergoing an accelerating decrease in prices. Investing in the stock at the moment is not recommended.")
      else:
        print(stocksymbol + " is undergoing a slight decrease in prices, that may alleviate soon. Keep an eye out.")
    elif (midpoint * 1.1) < end:
      print("The " + stocksymbol + " market increased between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
      if round(100-((midpoint/beginning)*100), 2) > round(100-((midpoint/end)*100), 2):
        print(stocksymbol + " has rebounded slightly after a decrease, but you could wait some time to see how the stock progresses before investing.")
      else:
        print(stocksymbol + " has rebounded after a decrease, and it'd make sense to invest now.")
    else:
      if midpoint > end:
        print("The " + stocksymbol + " market declined slightly between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
        print(stocksymbol + " is undergoing a slight decrease in prices, that may alleviate soon. Keep an eye out.")
      else:
        print("The " + stocksymbol + " market increased slightly between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
        print(stocksymbol + " has rebounded slightly after a decrease, but you could wait some time to see how the stock progresses before investing.")
        
        
  elif (beginning * 1.1) < midpoint: # > 10% increase from beginning to midpoint
    print("The " + stocksymbol + " market increased between 1 year ago and half a year ago. The increase was a " + str(round(100-((beginning/midpoint)*100), 2)) + "% increase.")
    if (midpoint * 0.9) > end:
      print("The " + stocksymbol + " market declined between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
      if round(100-((beginning/midpoint)*100), 2) > round(100-((end/midpoint)*100), 2):
        print(stocksymbol + " has recently begun a slight decrease in prices- the time to invest is not now, but perhaps soon.")
      elif round(100-((beginning/midpoint)*100), 2) < (round(100-((end/midpoint)*100), 2))/2:
        print(stocksymbol + " has recently begun a major decrease in prices. You should not invest now.")
      else:
        print(stocksymbol + " is experiencing a moderate decrease in prices. You should watch the stock to see how it progresses.")
    elif (midpoint * 1.1) < end:
      print("The " + stocksymbol + " market increased between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
      if round(100-((beginning/midpoint)*100), 2) > round(100-((midpoint/end)*100), 2):
        print(stocksymbol + " is increasing in price, but the rate of increase has fallen. You could invest.")
      else:
        print(stocksymbol + " is currently experiencing a decent growth in prices. It would be a good time to invest.")
    else:
      if midpoint > end:
        print("The " + stocksymbol + " market declined slightly between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
        print(stocksymbol + "'s prices could be stagnating or beginning a downturn. It's best to wait.")
      else:
        print("The " + stocksymbol + " market increased slightly between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
        print(stocksymbol + "'s rate of price increase is decreasing, but you could still invest.") 
        
        
  else:
    if beginning > midpoint: # < 10% decrease from beginning to midpoint
      print("The " + stocksymbol + " market declined slightly between 1 year ago and half a year ago. The decline was a " + str(round(100-((midpoint/beginning)*100), 2)) + "% decline.")
      if (midpoint * 0.9) > end:
        print("The " + stocksymbol + " market declined between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
        print(stocksymbol + " is beginning a period of decline. It is not advised to invest.")
      elif (midpoint * 1.1) < end:
        print("The " + stocksymbol + " market increased between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
        print(stocksymbol + " is beginning to rise again, so investment could make sense now.")
      else:
        if midpoint > end:
          print("The " + stocksymbol + " market declined slightly between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
          print(stocksymbol + "'s decline in prices remained minor and steady.")
        else:
          print("The " + stocksymbol + " market increased slightly between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
          print(stocksymbol + " experienced some increase in prices after a slight decline.")
    else: # < 10% increase from beginning to midpoint
      print("The " + stocksymbol + " market increased slightly between 1 year ago and half a year ago. The increase was a " + str(round(100-((midpoint/beginning)*100), 2)) + "% increase.")
      if (midpoint * 0.9) > end:
        print("The " + stocksymbol + " market declined between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
        print(stocksymbol + " experienced a decline in prices after a slight increase. It is not advised to invest.")
      elif (midpoint * 1.1) < end:
        print("The " + stocksymbol + " market increased between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
        print(stocksymbol + " is now experiencing larger rates of increasing prices.")
      else:
        if midpoint > end:
          print("The " + stocksymbol + " market declined slightly between half a year ago and the current moment. The decline was a " + str(round(100-((end/midpoint)*100), 2)) + "% decline.")
          print(stocksymbol + " has declined a bit after an increase.")
        else:
          print("The " + stocksymbol + " market increased slightly between half a year ago and the current moment. The increase was a " + str(round(100-((midpoint/end)*100), 2)) + "% increase.")
          print(stocksymbol + "is continuing an increase in prices now.")
  
  
while True:
  evaluateInvestment()
  if input("Go again? (Y/N) ").lower() == "n":
    break
