import csv

class CreateCsvFile:
	def __init__(self, results, csv_file):
		self.results = results
		self.csv_file = csv_file
		self.fields = ['rank', 'name', 'score', 'kills', 'deaths', 'assists', 'healing', 'damage']

	def exec(self):
		with open(self.csv_file, 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=self.fields)
			writer.writeheader()

			writer.writerows(self.results)

		return True