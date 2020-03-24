import datetime as dt

class DateFormatter():
	def reformat(self, date, currentFormat):
		dt_date = dt.datetime.strptime(date, currentFormat)
		new_date = str(dt_date)[:10]
		return new_date

