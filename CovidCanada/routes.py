from flask import Flask, render_template
import requests
from CovidCanada import app
from .backend.Client import CovidClient
from.backend.Serializer import Serializer

@app.route('/', methods=['GET'])
def dashboard():
	client = CovidClient()
	TodaysCanadaData = client.getTodaysCanadaData()
	CanadaPerDayData = client.getCanadaPerDayData()
	

	return render_template('dashboard.html', TodaysCanadaData=TodaysCanadaData, CanadaPerDayData=CanadaPerDayData)


# @app.route('/api/canadadailydata', methods=['GET'])
# def apiCall():
# 	client = CovidClient()
# 	CanadaPerDayData = client.getCanadaPerDayData()
# 	serializedData = {}
# 	for entry in CanadaPerDayData:
# 		serializedEntry = Serializer().serializePerDateData(entry)
# 		serializedData[entry.getDate()] = serializedEntry
# 	return serializedData

@app.route('/api/coviddailydata', methods=['GET'])
def apiCall():
	client = CovidClient()
	CovidPerDayData = client.getAllPerDayData()
	serializedData = {}
	for countrydata in CovidPerDayData:
		country = countrydata[0]
		data = countrydata[1]
		countrySerializedData = {}
		for entry in data:
			serializedEntry = Serializer().serializePerDateData(entry)
			countrySerializedData[entry.getDate()] = serializedEntry
		serializedData[country] = countrySerializedData
	return serializedData

