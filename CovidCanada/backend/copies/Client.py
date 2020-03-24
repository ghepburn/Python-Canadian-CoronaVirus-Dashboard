from .DataParsers.VirusTrackerParser import VirusTrackerParser, CanadianVirusTrackerParser
import json

CanadianParser = CanadianVirusTrackerParser()
CanadianHistoricalParser = None
GlobalParser = None
GlobalHistoricParser = None

class CovidClient():
	def __init__(self):
		self.data_parser = VirusTrackerParser()

	def getData(self):
		data = self.data_parser.getData()
		return data
	
class CovidCanadaClient(CovidClient):
	def __init__(self):
		self.data_parser = CanadianParser	

class CovidCanadaClient(CovidClient):
	def __init__(self):
		self.data_parser = CanadianParser	

