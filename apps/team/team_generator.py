import random
import math

from .models import Team, Player

def team_generate(num=50):
	available_cities =["New York City", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "Dallas", "Jacksonville", "San Francisco", "Seattle", "Denver", "Detroit", "DC", "Boston", "Baltimore", "Atlanta", "Miami", "Oakland", "Minneapolis", "New Orleans", "Cleveland", "St. Louis", "Pittsburgh", "Toronto", "Montreal", "Vancouver", "Mexico City", 'California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Ohio', 'Georgia', 'Michigan', 'Virginia', 'Washington', 'Arizona', 'Indiana', 'Colorado', "Ontario", "Quebec"]
	
	all_locations = ["New York City", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Seattle", "Denver", "El Paso", "Detroit", "DC", "Boston", "Memphis", "Nashville", "Portland", "Oklahoma City", "Las Vegas", "Baltimore", "Sacramento", "Kansas City", "Atlanta", "Raleigh", "Omaha", "Miami", "Oakland", "Minneapolis", "Tulsa", "Wichita", "New Orleans", "Cleveland", "St. Louis", "Pittsburgh", "Anchorage", "Cincinnati", "Buffalo", "Toronto", "Montreal", "Vancouver", "Ottawa", "Calgary", "Edmonton", "Quebec City", "Winnipeg", "Mexico City", "Havana", 'California', 'Texas', 'Florida', 'New York', 'Illinois', 'Pennsylvania', 'Ohio', 'Georgia', 'North Carolina', 'Michigan', 'New Jersey', 'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Indiana', 'Tennessee', 'Missouri', 'Maryland', 'Wisconsin', 'Minnesota', 'Colorado', 'South Carolina', 'Alabama', 'Louisiana', 'Kentucky', 'Oregon', 'Oklahoma', 'Connecticut', 'Puerto Rico', 'Iowa', 'Utah', 'Mississippi', 'Arkansas', 'Kansas', 'Nevada', 'New Mexico', 'Nebraska', 'West Virginia', 'Idaho', 'Hawaii', 'New Hampshire', 'Maine', 'Rhode Island', 'Montana', "Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba", "Saskatchewan", "New England", "Golden State"]

	places = available_cities * 2 + all_locations

	team_names = ["Orioles", "Red Sox", "Yankees", "Rays", "Blue Jays", "White Sox", "Tigers", "Royals", "Twins", "Astros", "Angels", "Athletics", "Mariners", "Rangers", "Marlins", "Mets", "Phillies", "Nationals", "Cubs", "Reds", "Brewers", "Pirates", "Cardinals", "Diamondbacks", "Rockies", "Dodgers", "Padres", "Giants", "Bills", "Dolphins", "Patriots", "Jets", "Ravens", "Bengals", "Browns", "Steelers", "Texans", "Colts", "Jaguars", "Titans", "Broncos", "Raiders", "Chargers", "Cowboys", "Eagles", "Bears", "Lions", "Packers", "Vikings", "Falcons", "Panthers", "Saints", "Buccaneers", "Rams", "49ers", "Seahawks", "Celtics", "Nets", "Knicks", "76ers", "Raptors", "Bulls", "Cavaliers", "Pistons", "Pacers", "Bucks", "Hawks", "Hornets", "Heat", "Magic", "Wizards", "Mavericks", "Rockets", "Grizzlies", "Pelicans", "Spurs", "Nuggets", "Timberwolves", "Thunder", "Trail Blazers", "Jazz", "Warriors", "Clippers", "Lakers", "Suns", "Kings", "Bruins", "Sabres", "Red Wings", "Canadiens", "Senators", "Lightning", "Maple Leafs", "Hurricanes", "Blue Jackets", "Devils", "Islanders", "Flyers", "Penguins", "Capitals", "Ducks", "Coyotes", "Flames", "Oilers", "Sharks", "Canucks", "Blackhawks", "Avalanche", "Stars", "Wild", "Predators", "Blues", "Stampeders", "Roughriders", "Rough Riders", "Blue Bombers", "Tiger-Cats", "Alouettes", "Redblacks", "Argonauts", "Hustlers", "Claws", "Squires", "Pipers", "Sails", "Outlaws", "Wranglers", "Stallions", "Breakers", "Blitz", "Gold", "Gamblers", "Express", "Showboats", "Generals", "Invaders", "Maulers", "Gunslingers", "Bandits", "Federals", "Renegades", "Black Sox", "Spiders", "Wolverines", "Colonels", "Bullets", "Robots", "Nightmare", "Americans", "Isotopes", "Gladiators"]

	teams = set()

	while Team.objects.count() < num:
		place = random.choice(places)
		team_name = random.choice(team_names)
		if not Team.objects.filter(location=place, team_name=team_name):
			Team.objects.create(location=place, team_name=team_name)

def player_generation(num=200):
	first_names = ['Noah', 'Liam', 'Mason', 'Jacob', 'William', 'Ethan', 'James', 'Alexander', 'Michael', 'Benjamin', 'Elijah', 'Daniel', 'Aiden', 'Logan', 'Matthew', 'Lucas', 'Jackson', 'David', 'Oliver', 'Jayden', 'Joseph', 'Gabriel', 'Samuel', 'Carter', 'Anthony', 'John', 'Dylan', 'Luke', 'Henry', 'Andrew', 'Isaac', 'Christopher', 'Joshua', 'Wyatt', 'Sebastian', 'Owen', 'Caleb', 'Nathan', 'Ryan', 'Jack', 'Hunter', 'Levi', 'Christian', 'Jaxon', 'Julian', 'Landon', 'Grayson', 'Jonathan', 'Isaiah', 'Charles', 'Emma', 'Olivia', 'Sophia', 'Ava', 'Isabella', 'Mia', 'Abigail', 'Emily', 'Charlotte', 'Harper']

	last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Rivera', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Griffin', 'Diaz', 'Hayes']

	while Player.objects.count() < num:
		first_name = random.choice(first_names)
		last_name = random.choice(last_names)
		team = random.choice(Team.objects.all())

		create_player = Player.objects.create(first_name=first_name, last_name=last_name, curr_team=team)

		create_player.all_teams.add(team)
	