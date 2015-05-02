import csv
import pprint
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['nfl-db']
schedule_collection = db['schedules']

# map the abbreviations to actual names
name_mapping = {
	'ARI': 'Arizona Cardinals',
	'ATL': 'Atlanta Falcons',
	'BAL': 'Baltimore Ravens',
	'BUF': 'Buffalo Bills',
	'CAR': 'Carolina Panthers',
	'CHI': 'Chicago Bears',
	'CIN': 'Cincinnati Bengals',
	'CLE': 'Cleveland Browns',
	'DAL': 'Dallas Cowboys',
	'DEN': 'Denver Broncos',
	'DET': 'Detroit Lions',
	'GB': 'Green Bay Packers',
	'HOU': 'Houston Texans',
	'IND': 'Indianapolis Colts',
	'JAX': 'Jacksonville Jaguars',
	'KC': 'Kansas City Chiefs',
	'MIA': 'Miami Dolphins',
	'MIN': 'Minnesota Vikings',
	'NE': 'New England Patriots',
	'NO': 'New Orleans Saints',
	'NYG': 'New York Giants',
	'NYJ': 'New York Jets',
	'OAK': 'Oakland Raiders',
	'PHI': 'Philadelphia Eagles',
	'PIT': 'Pittsburgh Steelers',
	'SD': 'San Diego Chargers',
	'SF': 'San Francisco 49ers',
	'SEA': 'Seattle Seahawks',
	'STL': 'St. Louis Rams',
	'TB': 'Tampa Bay Buccaneers',
	'TEN': 'Tennessee Titans',
	'WSH': 'Washington Redskins'
}

team_dict = []
nfl_dict = {}

def main():
	with open('nfl_schedule_data.csv') as csvfile:
		file_reader = csv.reader(csvfile, delimiter=',')
		
		# Get to the rows with the actual
		# schedule data
		file_reader.next()
		file_reader.next()

		for row in file_reader:
			nfl_dict = {}
			nfl_dict['team_code'] = row[0]
			nfl_dict['team_name'] = name_mapping[row[0]]
			for x in range(1,len(row)):
				key = 'Week ' + str(x)
				nfl_dict[key] = row[x]
				# print row[0], name_mapping[row[0]]

			schedule_collection.insert_one(nfl_dict)
			# for testing
			team_dict.append(nfl_dict)

	# for testing
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(team_dict)

if __name__ == '__main__':
    status = main()
