from marshmallow import Schema, fields

class DailyStatEntrySchema(Schema):
	date = fields.Str()
	cases = fields.Integer()
	deaths = fields.Integer()
	total_cases = fields.Integer()
	total_recoveries = fields.Integer()
	total_deaths = fields.Integer()