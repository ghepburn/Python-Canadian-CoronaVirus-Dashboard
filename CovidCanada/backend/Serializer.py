from .SerializerSchemas.DailyStatEntrySchema import DailyStatEntrySchema



class Serializer():
	def __init__(self):
		self.DailyStatEntrySchema = DailyStatEntrySchema()

	def serializePerDateData(self, DataObject):
		return self.DailyStatEntrySchema.dump(DataObject)
