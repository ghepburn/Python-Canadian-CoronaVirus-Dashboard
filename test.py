from CovidCanada.backend.SerializerSchemas.DailyStatEntrySchema import DailyStatEntrySchema
from CovidCanada.backend.DataObjects.DaileyStatEntry import DaileyStatEntry
from CovidCanada.backend.Serializer import Serializer

from marshmallow import Schema, fields

data = DaileyStatEntry("01/01/2020", 1, 2, 3, 4, 5)

class DailyStatEntrySchema(Schema):
	date = fields.Str()
	cases = fields.Integer()
	deaths = fields.Integer()
	total_cases = fields.Integer()
	total_recoveries = fields.Integer()
	total_deaths = fields.Integer()

schema = DailyStatEntrySchema()
y = schema.dump(data)
print(y)

class MyData():
	def __init__(self, a, b, c):
		self.a = a
		self._b = b
		self.c = c

class MySchema(Schema):
	a = fields.Integer()
	b = fields.Integer()
	c = fields.Str()

# data = MyData(1, 2, "Threeeeee")

# schema = MySchema()
# x = schema.dump(data)

# print(x)