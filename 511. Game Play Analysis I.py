import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # mydict = {}
    # for i in range(len(activity)):
    #     player_id = activity['player_id'][i]
    #     e_date = activity['event_date'][i]
    #     if player_id in mydict:
    #         if e_date <  mydict[player_id]:
    #             mydict[player_id] = e_date
    #     else:
    #         mydict[player_id] = e_date
    # result = []
    # for key,value in mydict.items():
    #     result.append([key,value])
    # return pd.DataFrame(result,columns=['player_id','first_login'])
    # mydict = {}
    # for i in range(len(activity)):
    #     player_id = activity['player_id'][i]
    #     e_date = activity['event_date'][i]
    #     if player_id not in mydict:
    #         mydict[player_id] = []
    #     mydict[player_id].append(e_date)
    # result = []
    # for key,value in mydict.items():
    #     value.sort()
    #     result.append([key,value[0]])
    # return pd.DataFrame(result,columns=['player_id','first_login'])
    df = activity.groupby(['player_id'])['event_date'].min().reset_index()
    return df.rename(columns={'event_date':'first_login'})

 

            
        
    