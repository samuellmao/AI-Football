# Choose names for your players and team
    # Choose a funny name for each player and your team
    # Use names written only in cyrillic
    # Make sure that the name is less than 11 characters
    # Don't use profanity!!!
import math
import random
def gtb(ball,our_team):
    yt=ball['y']-our_team['y']
    xt=ball['x']-our_team['x']
    alpha=math.atan2(yt, xt)
    return alpha
def gtp(our_team, their_team, your_side):
    if your_side=='left':
        a=max(their_team[0]['x'], their_team[1]['x'], their_team[2]['x'])
        for i in range (3):
            if(a==their_team[i]['x']):
                b=i
            else: b=1
        yt = their_team[b]['y'] - our_team['y']
        xt = their_team[b]['x'] - our_team['x']
        alpha = math.atan2(yt, xt)
    elif your_side=='right':
        a=min(their_team[0]['x'], their_team[1]['x'], their_team[2]['x'])
        for i in range (3):
            if(a==their_team[i]['x']):
                b=i
            else: b=1
        yt = their_team[b]['y'] - our_team['y']
        xt = their_team[b]['x'] - our_team['x']
        alpha = math.atan2(yt, xt)
    return alpha
def dribble(ball, their_team, our_team, num):
    for i in range (3):
        if(distot(ball, their_team[i])<=100):
            alpha=random.choice([math.pi/4, 7*(math.pi)/4])
        else:
            alpha=gtb(ball, our_team[num])
    return alpha
def check_shot(ball, their_team, our_team, your_side):
    if your_side=='left':
        sl=line_equationslope(our_team['alpha'])
        co=line_equationc(our_team['alpha'], our_team['x'], our_team['y'])
        f=sl*1316+co
        print(f)
        if(f>343 and f<578):
            print("vlaga")
            return True
        else:
            return False
    if your_side=='right':
        sl=line_equationslope(our_team['alpha'])
        co=line_equationc(our_team['alpha'],our_team['x'], our_team['y'])
        f=sl*50+co
        if(f>=343 and f<=578):
            return True
        else:
            return False
def distnt(ball, our_team):
    d=math.sqrt((ball['y']-our_team['y'])**2+(ball['x']-our_team['x'])**2)
    return d
def distot(ball, their_team):
    d = math.sqrt((ball['y'] - their_team['y']) ** 2 + (ball['x'] - their_team['x']) ** 2)
    return d
def najblizok(ball, their_team, our_team):
    a=min(distnt(ball, our_team, 0), distnt(ball, our_team, 1), distnt(ball, our_team, 2))
    b=min(distot(ball, their_team, 0), distnt(ball, their_team, 1), distnt(ball, their_team, 2) )
    for i in range (3):
        if(a<=b and distnt(ball, our_team, i)==a):
            return i
        else:
            return -1
def checkvodi(ball, our_team):
     i=-1
     for j in range(3):
         if (distnt(ball, our_team[j]) - ball['radius'] - our_team[j]['radius'] <= 10):
            i=j
     return i


def line_equationslope(angle):
    slope = math.tan(angle)
    return slope
def line_equationc(angle, x, y):
    slope = math.tan(angle)

    # Calculate the y-intercept (c) using the point-slope form
    c = y - slope * x

    # Return the slope and y-intercept
    return c

def line_equation2pts(x1,x2, y1, y2):

    # Calculate slope
    slope = (y2 - y1) / (x2 - x1)

    # Calculate the y-intercept (c)
    intercept = y1 - slope * x1

    # Return the slope and y-intercept
    return slope, intercept


def distance_to_line(x, y, line):
    A, B, C = line

    # Calculate the numerator of the distance formula
    numerator = abs(A * x + B * y + C)

    # Calculate the denominator of the distance formula
    denominator = math.sqrt(A ** 2 + B ** 2)

    # Calculate the distance
    distance = numerator / denominator

    return distance


def team_properties():
    properties = dict()
    player_names = ["ШУИ", "Фримпо", "Џаби"]
    properties['team_name'] = "НЕВЕРЛУЗЕН"
    properties['player_names'] = player_names
    properties['image_name'] = 'B04.png'  # use image resolution 153x153
    properties['weight_points'] = (9, 10, 15)
    properties['radius_points'] = (5, 10, 20)
    properties['max_acceleration_points'] = (40, 10, 15)
    properties['max_speed_points'] = (40, 10, 5)
    properties['shot_power_points'] = (18, 20, 13)
    return properties
# This function gathers game information and controls each one of your three players
def decision(our_team, their_team, ball, your_side, half, time_left, our_score, their_score):
    manager_decision = [dict(), dict(), dict()]
    for i in range(3):

        if (your_side == 'left'):
             # if (i == 1):  # golman
             #    player = our_team[i]
             #    if (player['x'] > 90):
             #        manager_decision[i]['alpha'] = math.pi
             #    elif (player['x'] <= 90 and player['x'] > 80):
             #        pom=player["alpha"]
             #        if (player['y'] <= 380):
             #            manager_decision[i]['alpha'] = (math.pi) / 2
             #        elif (player['y'] >= 550):
             #            manager_decision[i]['alpha'] = 3 * (math.pi) / 2
             #        elif(player['alpha'] == math.pi):
             #            manager_decision[i]['alpha'] = math.pi / 2
             #        else:
             #           manager_decision[i]['alpha'] = pom
             if (i == 1):  # golman
                player = our_team[i]
                if (player['x'] > 90):
                    manager_decision[i]['alpha'] = math.pi
                elif (player['x'] <= 90 and player['x'] > 80):
                    pom=player["alpha"]
                    if (player['y'] <= 380):
                        manager_decision[i]['alpha'] = (math.pi) / 2
                    elif (player['y'] >= 550):
                        manager_decision[i]['alpha'] = 3 * (math.pi) / 2
                    elif (ball['y']<578 and ball['y']>343):
                        if(player['y']>ball['y']):
                            manager_decision[i]['alpha']=3*math.pi /2
                        else:
                            manager_decision[i]['alpha']=math.pi/2
                    elif(player['alpha'] == math.pi):
                        manager_decision[i]['alpha'] = math.pi / 2
                    else:
                       manager_decision[i]['alpha'] = pom
                else:
                    manager_decision[i]['alpha'] = 0
                manager_decision[i]['force'] = 1000000000000
                manager_decision[i]['shot_request'] = True
                manager_decision[i]['shot_power'] = 100
             if (i == 0):
                if (checkvodi(ball, our_team) == i):
                        if (check_shot(ball, their_team, our_team[i], 'left')):
                            print("vlaga2")
                            manager_decision[i]['shot_request'] = True
                            manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                        else:
                            manager_decision[i]['shot_request'] = False
                            manager_decision[i]['alpha'] = dribble(ball, their_team, our_team, i)
                else:
                    manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                    manager_decision[i]['shot_request'] = True
                manager_decision[i]['force'] = 1000
                manager_decision[i]['shot_power'] = 1000000000000000000000000000000000000
             if(i==2):
                if (checkvodi(ball, our_team) == -1):
                    manager_decision[i]['alpha']=gtb(ball, our_team[i])
                    manager_decision[i]['shot_request'] = False
                elif (checkvodi(ball, our_team) == i):
                    manager_decision[i]['shot_request'] = True
                    manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                else:
                    manager_decision[i]['alpha']=gtp(our_team[i], their_team, 'left')
                    manager_decision[i]['shot_request'] = False
                manager_decision[i]['force'] = 10000
                manager_decision[i]['shot_power'] = 100
        if (your_side == 'right'):
                if (i == 1):  # golman
                    player = our_team[i]
                    if (player['x'] < 1276):
                        manager_decision[i]['alpha'] = 0
                    elif (player['x'] > 1276 and player['x'] < 1316):
                        pom = player["alpha"]
                        if (player['y'] <= 380):
                            manager_decision[i]['alpha'] = (math.pi) / 2
                        elif (player['y'] >= 550):
                            manager_decision[i]['alpha'] = 3 * (math.pi) / 2
                        elif (ball['y'] < 578 and ball['y'] > 343):
                            if (player['y'] > ball['y']):
                                manager_decision[i]['alpha'] = 3 * math.pi / 2
                            else:
                                manager_decision[i]['alpha'] = math.pi / 2
                        elif (player['alpha'] == 0):
                            manager_decision[i]['alpha'] = math.pi / 2
                        else:
                            manager_decision[i]['alpha'] = pom
                    else:
                        manager_decision[i]['alpha'] = 0
                    manager_decision[i]['force'] = 1000000000000
                    manager_decision[i]['shot_request'] = True
                    manager_decision[i]['shot_power'] = 100
                else:
                    manager_decision[i]['alpha'] = math.pi/2
                    manager_decision[i]['force'] = 1000000000000
                    manager_decision[i]['shot_request'] = True
                    manager_decision[i]['shot_power'] = 100
                if (i == 0):
                    if (checkvodi(ball, our_team) == i):
                        if (check_shot(ball, their_team,our_team[i], 'right') == 1):
                            manager_decision[i]['shot_request'] = True
                            manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                        else:
                            manager_decision[i]['shot_request'] = False
                            manager_decision[i]['alpha']=dribble(ball, their_team, our_team, i)
                    else:
                        manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                        manager_decision[i]['shot_request'] = False
                    manager_decision[i]['force'] = 1000000000000
                    manager_decision[i]['shot_power'] = 100
                if (i == 2):
                    if (checkvodi(ball, our_team) == -1):
                        manager_decision[i]['alpha']=gtb(ball, our_team[i])
                    elif (checkvodi(ball, their_team) == i):
                        manager_decision[i]['shot_request'] = True
                        manager_decision[i]['alpha'] = gtb(ball, our_team[i])
                    else:
                        manager_decision[i]['alpha'] = gtp(our_team[i], their_team, 'right')
                        manager_decision[i]['shot_request'] = False
                    manager_decision[i]['force'] = 10000
                    manager_decision[i]['shot_power'] = 100
    return manager_decision