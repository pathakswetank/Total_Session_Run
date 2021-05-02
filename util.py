import pickle
import json
import numpy as np

__PLAYER = None
__data_columns = None
__model = None

def estimated_run(PLAYER,Mat, Inns, NO, Avg, HS, BF, SR, HUNDREDS, FIFTY,Fours, Six):
    try:
        loc_index = __data_columns.index(PLAYER.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Mat
    x[1] = Inns
    x[2] = NO
    x[3] = Avg
    x[4] = HS
    x[5] = BF
    x[6] = SR
    x[7] = HUNDREDS
    x[8] = FIFTY
    x[9] = Fours
    x[10] = Six
    if loc_index >= 0:
        x[loc_index] = 1

    return round (__model.predict([x])[0])


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __PLAYER = __data_columns[12:]  

    global __model
    if __model is None:
        with open('IPL_SESSION_2020_TOTAL_RUN.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def player_names():
    return __PLAYER

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(player_names())
    print(estimated_run("KL_Rahul", 14, 12, 5, 10.0, 88, 300,89,0,2,7,2))
    