from TournamentGame import TournamentGame
import pickle
# from sklearn.externals import joblib

file = open('model.pkl', 'rb')
model = pickle.load(file)
file.close()

# model = joblib.load('model.pkl')

## First Four
FiFo_RUT_ND = TournamentGame(team_1 = "Rutgers", team_2 = "Notre Dame", round_str = "First Four")
FiFo_Wright_Bryant = TournamentGame(team_1 = "Wright St", team_2 = "Bryant", round_str = "First Four")
FiFo_Txamcc_Texso = TournamentGame(team_1 = "TAM C. Christi", team_2 = "Texas St", round_str = "First Four")
FiFo_WYOM_IND = TournamentGame(team_1 = "Wyoming", team_2 = "Indiana", round_str = "First Four")

## Rest of Bracket


West_Teams = [ # in order of schedule (upper Left)
    "Gonzaga",
    "Georgia St",
    "Boise St",
    "Memphis",
    "Connecticut",
    "New Mexico St",
    "Arkansas",
    "Vermont",
    "Alabama",
    FiFo_RUT_ND,
    "Texas Tech",
    "Montana St",
    "Michigan St",
    "Davidson",
    "Duke",
    "CS Fullerton",
]

South_Teams = [ # in order of schedule (upper right)
    "Arizona",
    FiFo_Wright_Bryant,
    "Seton Hall",
    "TCU",
    "Houston",
    "UAB",
    "Illinois",
    "Chattanooga",
    "Colorado St",
    "Michigan",
    "Tennessee",
    "Longwood",
    "Ohio St",
    "Loyola-Chicago",
    "Villanova",
    "Delaware",
]

East_Teams = [ # in order of schedule (lower left)
    "Baylor",
    "Norfolk St",
    "North Carolina",
    "Marquette",
    "St Mary's CA",
    FiFo_WYOM_IND,
    "UCLA",
    "Akron",
    "Texas",
    "Virginia Tech",
    "Purdue",
    "Yale",
    "Murray St",
    "San Francisco",
    "Kentucky",
    "St Peter's",
]

MidWest_Teams = [ # in order of schedule (lower right)
    "Kansas",
    FiFo_Txamcc_Texso,
    "San Diego St",
    "Creighton",
    "Iowa",
    "Richmond",
    "Providence",
    "South Dakota",
    "LSU",
    "Iowa St",
    "Wisconsin",
    "Colgate",
    "USC",
    "Miami FL",
    "Auburn",
    "Jacksonville St",
]

def setup_quadrant(list_of_teams):

    # round 1
    round_1_games = [
        TournamentGame(
            team_1 = list_of_teams[idx],
            team_2 = list_of_teams[idx+1],
            round_str = "Round 1",
        ) for idx in range(0, len(list_of_teams), 2)
    ]

    # round 2
    round_2_games = [
        TournamentGame(
            team_1 = round_1_games[idx],
            team_2 = round_1_games[idx+1],
        ) for idx in range(0, len(round_1_games), 2)
    ]

    # round 3
    round_3_games = [
        TournamentGame(
            team_1 = round_2_games[idx],
            team_2 = round_2_games[idx+1],
        ) for idx in range(0, len(round_2_games), 2)
    ]
    
    return TournamentGame(
        team_1 = round_3_games[0],
        team_2 = round_3_games[1],
    )

West_Final_Four = setup_quadrant(West_Teams)
East_Final_Four = setup_quadrant(East_Teams)
South_Final_Four = setup_quadrant(South_Teams)
MidWest_Final_Four = setup_quadrant(MidWest_Teams)

EastWestSemiFinal = TournamentGame(
    team_1 = West_Final_Four,
    team_2 = East_Final_Four,
)

SouthMidWestSemiFinal = TournamentGame(
    team_1 = South_Final_Four,
    team_2 = MidWest_Final_Four,
)

Final = TournamentGame(
    team_1 = EastWestSemiFinal,
    team_2 = SouthMidWestSemiFinal,
)

Final.predict_result(model)

# # Set up bracket
# ## First Quadrant
# round_1_game_A = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# round_1_game_B = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# round_2_game_AB = TournamentGame(child_1 = round_1_game_A, child_2 = round_1_game_B)

# round_1_game_C = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# round_1_game_D = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# round_2_game_CD = TournamentGame(child_1 = round_1_game_C, child_2 = round_1_game_D)

# round_3_game_ABCD = TournamentGame(child_1 = round_2_game_AB, child_2 = round_2_game_CD)

# round_1_game_E = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# round_1_game_F = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# round_2_game_EF = TournamentGame(child_1 = round_1_game_E, child_2 = round_1_game_F)

# round_1_game_G = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# round_1_game_H = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# round_2_game_GH = TournamentGame(child_1 = round_1_game_G, child_2 = round_1_game_H)

# round_3_game_EFGH = TournamentGame(child_1 = round_2_game_EF, child_2 = round_2_game_GH)

# round_4_game_ABCDEFGH = TournamentGame(child_1 = round_3_game_ABCD, child_2 = round_3_game_EFGH)
# round_4_game_ABCDEFGH.predict_result(0)
# # round_1_game_I = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_J = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# # round_1_game_I = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_J = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# # round_1_game_K = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_L = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# # round_1_game_M = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_N = TournamentGame(team_1 = "Bear", team_2 = "Jamie")




# # round_1_game_O = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_P = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# # round_1_game_Q = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_R = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# # round_1_game_Q = TournamentGame(team_1 = "Gonzaga", team_2 = "Max")
# # round_1_game_R = TournamentGame(team_1 = "Bear", team_2 = "Jamie")

# ## Round 2
# round_2_game_AB = TournamentGame(child_1 = round_1_game_A, child_2 = round_1_game_B)

# # round_2_game_1.predict_result(0)