from apicontrol import askGpt
from searching import gather_info
GLOBAL_MODEL = "gpt-4-0314"
def data_map_gen(statement:str) -> dict: # Uses gpt to create a search query and then proceeds to gather data into a hash map using the gather_info function
    query = askGpt(prompt=f"Based on this statement: {statement}\nReturn below a few keywords that would best search for information regarding its truthfulness:",model=GLOBAL_MODEL)
    query = query.rstrip('"') # Format string for search engine reasons
    return gather_info(query) 
def compare_assess(statement:str,gathered:str) -> str: # Uses gpt to compare site info with given statement
    return askGpt(prompt=f"In what ways does this statement:\n{statement}\nDiffer from the information here:\n{gathered}\n",model=GLOBAL_MODEL)
def summary_agent(researched_list:list,statement:str)->str: # uses gpt to output a final summary of statement's truthfulness
    readable_text = ""
    for rating in researched_list:
        readable_text+=rating+"\n"
    return askGpt(prompt=f"Why is this statement:{statement}\ntrue or not? Summarize and explain why based on these articles you have found (If nothing much is found, its probably not correct): \n{readable_text}. Then list sources you base your opinion upon",model=GLOBAL_MODEL)



