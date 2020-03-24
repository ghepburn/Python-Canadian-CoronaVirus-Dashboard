class DaileyStatEntry():
	def __init__(self, date, cases, deaths, total_cases, total_recoveries, total_deaths):
		self.date = date
		self.cases = cases
		self.deaths = deaths
		self.total_cases = total_cases
		self.total_recoveries = total_recoveries
		self.total_deaths = total_deaths

	def getDate(self):
		return self.date

	def setDate(self, new_date):
		self.date = new_date

	def getCases(self):
		return self.cases

	def getDeaths(self):
		return self.deaths

	def getTotalCases(self):
		return self.total_cases

	def getTotalRecoveries(self):
		return self.total_recoveries

	def getTotalDeaths(self):
		return self.total_deaths