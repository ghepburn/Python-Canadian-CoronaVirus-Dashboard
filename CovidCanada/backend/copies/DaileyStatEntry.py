class DaileyStatEntry():
	def __init__(self, date, cases, deaths):
		self._date = date
		self._cases = cases
		self._deaths = deaths

	def getDate(self):
		return self._date

	def getCases(self):
		return self._cases

	def getDeaths(self):
		return self._deaths

