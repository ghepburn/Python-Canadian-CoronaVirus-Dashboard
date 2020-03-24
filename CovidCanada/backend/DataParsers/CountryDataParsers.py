from .DataParser import CountryTimelineDataParser

class CanadaTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=CA"


class USTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=US"


class AustraliaTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=AU"


class FranceTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=FR"


class ItalyTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=IT"


class ChinaTimelineDataParser(CountryTimelineDataParser):
	def __init__(self):
		super().__init__()
		self.source = "https://thevirustracker.com/free-api?countryTimeline=CN"