from .DataParsers.CountryDataParsers import CanadaTimelineDataParser, USTimelineDataParser, AustraliaTimelineDataParser, FranceTimelineDataParser, ItalyTimelineDataParser, ChinaTimelineDataParser
from .DateFormatter import DateFormatter

import datetime as dt

CanadaTimelineDataParser = CanadaTimelineDataParser()
USTimelineDataParser = USTimelineDataParser()
AustraliaTimelineDataParser = AustraliaTimelineDataParser()
FranceTimelineDataParser = FranceTimelineDataParser()
ChinaTimelineDataParser = ChinaTimelineDataParser()
ItalyTimelineDataParser = ItalyTimelineDataParser()


class CovidClient():
	def __init__(self):
		pass

	def getCanadaPerDayData(self):
		data =  CanadaTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def formatDate(self, data):
		for day in data:
			date = day.getDate()
			reformatted_date = DateFormatter().reformat(date, '%m/%d/%Y')
			day.setDate(reformatted_date)
		return data

	def getTodaysCanadaData(self):
		perDayData = self.getCanadaPerDayData()
		todaysData = perDayData[-1]
		return todaysData

	def getUSPerDayData(self):
		data =  USTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def getAustraliaPerDayData(self):
		data =  AustraliaTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def getFrancePerDayData(self):
		data =  FranceTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def getItalyPerDayData(self):
		data =  ItalyTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def getChinaPerDayData(self):
		data =  ChinaTimelineDataParser.read()
		data = self.formatDate(data)
		return data

	def getAllPerDayData(self):
		data = []
		data.append(["Canada", self.getCanadaPerDayData()])
		data.append(["US", self.getUSPerDayData()])
		data.append(["Australia", self.getAustraliaPerDayData()])
		data.append(["Italy", self.getItalyPerDayData()])
		data.append(["France", self.getFrancePerDayData()])
		data.append(["China", self.getChinaPerDayData()])
		return data