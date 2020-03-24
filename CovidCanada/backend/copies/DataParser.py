import requests
import datetime as dt

class VirusTrackerParser():
	def __init__(self):
		self.source = None
		self.data = None
		self.last_api_call = None

	def getData(self):
		if self.allowApiCall():
			data = requests.get(self.source)
			self.data = data.json()
			print("called API")
		else:
			print("Did Not Call API")
		return self.data

	def allowApiCall(self):
		currentDate = dt.datetime.today().date()
		if self.last_api_call == None:
			self.last_api_call = currentDate
			return True
		else:
			print(self.last_api_call)
			daysSinceLastCall = currentDate - self.last_api_call
			if daysSinceLastCall.days > 0:
				self.last_api_call = currentDate
				return True
			else:
				return False


class CanadianVirusTrackerParser(VirusTrackerParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTotal=CA"
