
var CanadaCases = []
var headers = ["Date", "Cases", "Deaths"]
CanadaCases.push(headers)

var GlobalCases = []
var headers = ["Date", "Australia", "Canada", "China", "France", "Italy", "US"]
GlobalCases.push(headers)

var request = new XMLHttpRequest()

request.open('GET', '/api/coviddailydata', true)

request.onload = function() {
	var countryData = JSON.parse(this.response)
	if (request.status >= 200 && request.status < 400) {
		for (key in countryData["Canada"]) {
			var thiscase = [key]
			thiscase.push(parseInt(countryData["Canada"][key]["cases"]))
			thiscase.push(parseInt(countryData["Canada"][key]["deaths"]))
			CanadaCases.push(thiscase)
		}
		for (date in countryData["Canada"]) {
			var dateData = [date]
			for (country in countryData) {
				dateData.push(parseInt(countryData[country][date]["cases"]))
			}
			GlobalCases.push(dateData)
		}

	}
}

request.send()

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
	var Canadadata = new google.visualization.arrayToDataTable(CanadaCases);
	var Canadaoptions = {
		title: 'Diagnosed Covid19 Cases & Deaths Per Day',
		hAxis: {title: 'Date'},
		vAxis: {title: 'Number Of People', minValue: 0, maxValue: 150},
		legend: 'top',
		height: 500, 
		width: 1200,
		lineWidth: 15
	};

	var Globaldata = new google.visualization.arrayToDataTable(GlobalCases);
	var Globaloptions = {
		title: 'Global Diagnosed Covid19 Cases & Deaths Per Day',
		hAxis: {title: 'Date'},
		vAxis: {title: 'Number Of People', minValue: 0, maxValue: 150},
		legend: 'top',
		height: 700, 
		width: 1400,
		lineWidth: 5
	};

	var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
	chart.draw(Canadadata, Canadaoptions);

	var second_chart = new google.visualization.LineChart(document.getElementById('second_chart_div'));
	second_chart.draw(Globaldata, Globaloptions);
  }

