from prompting import *

statements = ["The american people are turning everybody in high schools into homosexuals","Trump actually has connections to many far right parties in Venezuela","Joe Biden has a history of commiting crimes in his youth","Ukrainians are using American controlled birds to spy on Russia"] # strong political statements


def vigilans(statement:str)->str:
    data_map = data_map_gen(statement) 
    rating_list = [] # list of separate page evaluations
    for url in data_map:
        assesment = "The assesment of website "+url+"\n"
        assesment+=compare_assess(statement,data_map[url])
        rating_list.append(assesment)
    if len(rating_list)==0:
        return "There has been nothing found on this topic, therefore the truthfulness of this statement is questionable"
    return summary_agent(rating_list,statement)

for statement in statements: # Just a test of what vigilans can do
    print(vigilans(statements))



