import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # mydict  = {}
    # Max = 0
    # for i in range(len(orders)):
    #     cus_num = orders['customer_number'][i]
    #     if cus_num not in mydict:
    #         mydict[cus_num] = 0
    #     mydict[cus_num] += 1
    #     if mydict[cus_num]>Max:
    #         Max = mydict[cus_num]
    # result = []
    # for key,value in mydict.items():
    #     if value == Max:
    #         result.append([key])
    # return pd.DataFrame(result,columns = ['customer_number'])
    group = orders.groupby(['customer_number']).size().reset_index(name = 'count')
    group.sort_values(by=['count'],ascending =False, inplace =True)
    if len(group) == 0:
        return pd.DataFrame([], columns = ['customer_number'])
    # return pd.DataFrame([group.iloc[0]['customer_number']]).rename(columns = {0:'customer_number'})
    return group[['customer_number']][0:1]