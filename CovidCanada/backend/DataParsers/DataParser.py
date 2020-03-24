from ..DataObjects.DaileyStatEntry import DaileyStatEntry

import requests
import datetime as dt


class DataParser():
	def __init__(self):
		self.json_data = None
		self.source = None
		self.last_api_call = None

	def setData(self):
		data = requests.get(self.source, headers={"User-Agent": "XY"})
		print(data)
		self.json_data = data.json()

	def read(self):
		
		# get data from api
		if self.allowApiCall():
			print("Pulling From API")
			self.setData()
		
		# put into data object
		data = self.convertToDataObject(self.json_data)

		# return data object list
		return data

	def allowApiCall(self):
		currentDate = dt.datetime.today().date()
		if self.last_api_call == None:
			self.last_api_call = currentDate
			return True
		else:
			daysSinceLastCall = currentDate - self.last_api_call
			if daysSinceLastCall.days > 0:
				self.last_api_call = currentDate
				return True
			else:
				return False

	def convertToDataObject(self, raw_json_data):
		pass


class CountryTimelineDataParser(DataParser):

	def convertToDataObject(self, raw_json_data):
		dataObjectList = []
		dates = list(raw_json_data["timelineitems"][0])[:-1]
		for date in dates:
			date = date
			cases = raw_json_data["timelineitems"][0][date]["new_daily_cases"]
			deaths = raw_json_data["timelineitems"][0][date]["new_daily_deaths"]
			total_cases = raw_json_data["timelineitems"][0][date]["total_cases"]
			total_recoveries = raw_json_data["timelineitems"][0][date]["total_recoveries"]
			total_deaths = raw_json_data["timelineitems"][0][date]["total_deaths"]
			dataEntry = DaileyStatEntry(date, cases, deaths, total_cases, total_recoveries, total_deaths)
			dataObjectList.append(dataEntry)
		return dataObjectList