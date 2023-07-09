import random

toss = ["Heads", "Tails"]
choose_to = ["Bat", "Bowl"]


class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batsmen = []
        self.bowlers = []

    def select_captain(self, captain):
        self.captain = captain

    def choose_batsmen(self, count):
        self.batsmen = random.sample(self.players, count)

    def choose_bowler(self):
        self.bowlers = random.choice(self.players)


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def simulate_ball(self, batsman, bowler):
        
        pass


class Commentator:
    def __init__(self):
        pass
    def provide_commentary(self, comment):
        print(comment)


class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.commentator = Commentator()

    def toss_coin(self):
        self.commentator.provide_commentary(
            "What a beautiful day today! It's a "+field.size+" & "+field.pitch_conditions+" field. Both captains walking into the field for the toss.")
        call = random.choice(toss)
        self.commentator.provide_commentary(
            call+" is the call by "+team1.captain.name)
        coin_outcome = random.choice(toss)
        self.commentator.provide_commentary("And it's "+coin_outcome)
        choose = random.choice(choose_to)
        if call == coin_outcome:
            self.commentator.provide_commentary(
                team1.captain.name+" chooses to "+choose)
        else:
            self.commentator.provide_commentary(
                team2.captain.name+" chooses to "+choose)

    def start_match(self):
        # Perform toss, choose batting/bowling order, etc.
        # Start the match and simulate ball-by-ball actions
        pass

    def change_innings(self):
        # Change the batting and bowling teams for the second innings
        pass

    def end_match(self):
        # Display final score, result, and any other relevant information
        pass
    
    # Team India
player1 = Player("Rohit Sharma", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Rishab Pant", 0.8, 0.2, 0.99, 0.8, 0.9)
player3 = Player("Virat Kohli", 0.8, 0.2, 0.99, 0.8, 0.9)
player4 = Player("Ishan Kisan", 0.8, 0.2, 0.99, 0.8, 0.9)
player5 = Player("Hardik Pandya", 0.8, 0.2, 0.99, 0.8, 0.9)
player6 = Player("Shubman Gill", 0.8, 0.2, 0.99, 0.8, 0.9)
player7 = Player("Shreyas Iyer", 0.8, 0.2, 0.99, 0.8, 0.9)
player8 = Player("Axar Patel", 0.8, 0.2, 0.99, 0.8, 0.9)
player9 = Player("Kuldeep Yadav", 0.8, 0.2, 0.99, 0.8, 0.9)
player10 = Player("Bhuvaneshwar Kumar", 0.8, 0.2, 0.99, 0.8, 0.9)
player11 = Player("Yuzvendra Chahal", 0.8, 0.2, 0.99, 0.8, 0.9)

# Team England
player12 = Player("Zak Craley ", 0.8, 0.2, 0.99, 0.8, 0.9)
player13 = Player("Ben Duckett", 0.8, 0.2, 0.99, 0.8, 0.9)
player14 = Player("Harry Brook", 0.8, 0.2, 0.99, 0.8, 0.9)
player15 = Player("Joe Root", 0.8, 0.2, 0.99, 0.8, 0.9)
player16 = Player("Jonny Bairstow", 0.8, 0.2, 0.99, 0.8, 0.9)
player17 = Player("Ben stokes", 0.8, 0.2, 0.99, 0.8, 0.9)
player18 = Player("Moen Ali", 0.8, 0.2, 0.99, 0.8, 0.9)
player19 = Player("Chris Woakes", 0.8, 0.2, 0.99, 0.8, 0.9)
player20 = Player("Mark Wood", 0.8, 0.2, 0.99, 0.8, 0.9)
player21 = Player("Stuart Broad", 0.8, 0.2, 0.99, 0.8, 0.9)
player22 = Player("Ollie Robinson", 0.8, 0.2, 0.99, 0.8, 0.9)
team1 = Team("India", [player1, player2, player3, player4, player5,
             player6, player7, player8, player9, player10, player11])
team1.select_captain(player6)

team2 = Team("England", [player12, player13, player14, player15, player16,
             player17, player18, player19, player20, player21, player22])
team2.select_captain(player13)

field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
match.toss_coin()