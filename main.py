import random
from collections import deque

toss = ["Heads", "Tails"]
choose_to = ["Bat", "Bowl"]
dismissals = ["Bowled", "Out by LBW", "Run-out", "Caught", "Stumped-out"]
run = [-1, 0, 1, 2, 3, 4, 6]


class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience
        self.runs_scored = 0
        self.runs_given = 0
        self.wickets_taken = 0
        self.dismissal = ""


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batsmen = players
        self.bowlers = players[5:]
    def select_captain(self, captain):
        self.captain = captain
    def next_batsman(self, pos):
        pos = pos % len(self.batsmen)
        return self.batsmen[pos]
    
    def next_bowler(self, pos):
        pos = pos % len(self.bowlers)
        return self.bowlers[pos]

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage





class Umpire:
    def __init__(self, overs):    
        self.score = 0
        self.wickets = 0
        self.overs = overs

    def simulate_ball(self, bat, bowl):
        batting_rating = bat.batting
        bowling_rating = bowl.bowling
        fielding_rating = bat.fielding
        running_rating = bat.running

        total_rating = batting_rating + bowling_rating + fielding_rating + running_rating

        boundary_prob = batting_rating / total_rating
        six_prob = boundary_prob / 6
        four_prob = (boundary_prob - six_prob) / 4
        three_prob = (1 - boundary_prob) / 3
        two_prob = three_prob / 2
        one_prob = two_prob / 2
        zero_prob = 1 - (boundary_prob + three_prob + two_prob + one_prob)

        outcome = random.random()

        if outcome < boundary_prob:
            outcome = random.choices([4, 6], weights=[four_prob, six_prob])[0]
        elif outcome < boundary_prob + three_prob:
            outcome = 3
        elif outcome < boundary_prob + three_prob + two_prob:
            outcome = 2
        elif outcome < boundary_prob + three_prob + two_prob + one_prob:
            outcome = 1
        else:
            outcome = -1
            
        if outcome > -1:
            bat.runs_scored += outcome
            bowl.runs_given += outcome
            self.score += outcome
        else:
            bowl.wickets_taken += 1
            self.wickets += 1
        return outcome


class Commentator:
    def __init__(self):
        pass
    def provide_commentary(self, comment):
        print("")
        print(comment)



class Match:
    def __init__(self, team1, team2, field, total_overs):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(total_overs)        
        self.commentator = Commentator()
        self.stricker = None
        self.non_stricker = None
        self.bowler = None
        

    def toss_coin(self):
        self.commentator.provide_commentary(
            "What a beautiful day today! It's a "+field.size+" & "+field.pitch_conditions+" field. Both captains walking into the field for the toss.")
        call = random.choice(toss)
        self.commentator.provide_commentary(
            call+" is the call by "+team1.captain.name)
        coin_outcome = random.choice(toss)
        self.commentator.provide_commentary("And it's "+coin_outcome)
        choose = random.choice(choose_to)
        toss_res = {}
        if call == coin_outcome:
            self.commentator.provide_commentary(
                team1.name+" wins the toss. " + team1.captain.name+" chooses to "+choose)
            if choose == "Bat":
                toss_res["Bat"] = team1
                toss_res["Bowl"] = team2
            else:
                toss_res["Bat"] = team2
                toss_res["Bowl"] = team1
        else:
            self.commentator.provide_commentary(team2.name+" wins the toss. " + team2.captain.name+" chooses to "+choose)
            if choose == "Bat":
                toss_res["Bat"] = team2
                toss_res["Bowl"] = team1
            else:
                toss_res["Bat"] = team1
                toss_res["Bowl"] = team2
        return toss_res

    def start_match(self, res, target):
        self.stricker = res['Bat'].next_batsman(0)
        self.non_stricker = res['Bat'].next_batsman(1)
        self.umpire.score = 0
        self.umpire.wickets = 0
        over = 0
        end = False

        self.bowler = res['Bowl'].next_bowler(over)
        for i in range(self.umpire.overs):
            for j in range(6):
                if self.umpire.wickets == 10:
                    end = True
                    break
                outcome = self.umpire.simulate_ball(self.stricker, self.bowler)
                if outcome == -1:
                    dismissal_type = random.choice(dismissals)
                    self.stricker.dismissal = dismissal_type
                    self.commentator.provide_commentary(
                        self.stricker.name+" is "+dismissal_type)
                    self.stricker = res['Bat'].next_batsman(
                        self.umpire.wickets+1)
                else:
                    self.commentator.provide_commentary(
                        self.stricker.name + " scores "+str(outcome)+" runs")
                    if self.umpire.score >= target:
                        end = True
                        break
                    if outcome % 2 != 0:
                        temp = self.stricker
                        self.stricker = self.non_stricker
                        self.non_stricker = temp
            over += 1
            self.bowler = res['Bowl'].next_bowler(over)
            if end | over == self.umpire.overs:
                self.commentator.provide_commentary("Innings over")
                break
            temp = self.stricker
            self.stricker = self.non_stricker
            self.non_stricker = temp
            self.commentator.provide_commentary("Over change")
        self.commentator.provide_commentary(
            "Total runs scored: "+str(self.umpire.score))
            
        return self.umpire.score

    def change_innings(self, res, target):
        self.commentator.provide_commentary("Next innings")
        temp = res['Bowl']
        res['Bowl'] = res['Bat']
        res['Bat'] = temp
        return self.start_match(res, target)

    def end_match(self, res, target, chase):
        self.commentator.provide_commentary(
            "What an extra ordinary match. Let's take a look at the Scoreboard")
        self.commentator.provide_commentary(team1.name+" Batting")
        for i in team1.batsmen:
            self.commentator.provide_commentary(
                i.name+" "+str(i.runs_scored)+" "+i.dismissal)
        print("**********************")
        self.commentator.provide_commentary(team1.name+" Bowling")
        for i in team1.bowlers:
            self.commentator.provide_commentary(
                i.name+" "+str(i.runs_given)+" "+str(i.wickets_taken))
        print("**********************")
        self.commentator.provide_commentary(team2.name+" Batting")
        for i in team2.batsmen:
            self.commentator.provide_commentary(
                i.name+" "+str(i.runs_scored)+" "+i.dismissal)
        print("**********************")
        self.commentator.provide_commentary(team2.name+" Bowling")
        for i in team2.bowlers:
            self.commentator.provide_commentary(
                i.name+" "+str(i.runs_given)+" "+str(i.wickets_taken))
        if chase >= target:
            self.commentator.provide_commentary(res['Bat'].name+" wins")
        else:
            self.commentator.provide_commentary(res['Bowl'].name+" wins")
    
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
team2.select_captain(player17)

field = Field("Large", 0.8, "Dry", 0.1)

match = Match(team1, team2, field)
toss_res = match.toss_coin()
target = match.start_match(toss_res, 99999)
chase = match.change_innings(toss_res, target+1)
match.end_match(toss_res, target, chase)