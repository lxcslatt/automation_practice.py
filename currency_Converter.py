#Gives access to the request libary 
import requests
#This is the url of the api we going to use to give us currency rates and also converting
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_KPVoAYZo154auYBFB1Bt7QzUzY9rMFc29KSOI2UF"


#These are the currencies that our currency is going to be compared with
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]
#Function to input which currency we want to compare 
def convert_currency(base):
	#Our CURRENCIES list but now in a string format seperated by ,
	currencies = ",".join(CURRENCIES)
	#Our formatted url that we want to send to the BASE_URL
	url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
	try:
		#this variable holds the response from the api
		response = requests.get(url)
		#This variable holds the data but now viewable in terminal in a dictonary 
		data = response.json()
		#Prints data 
		print(data)
		return data
	#if request doesnt work store whatever data came back in the variable |e|
	except Exception as e:
		# We can see what the error is
		print(e)
		return None
#We call the function and specify what currency we want to be compared.
convert_currency("GBP")		
