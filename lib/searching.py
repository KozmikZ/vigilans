import bs4,requests
from lib.utils import rndhead
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
VERBOSE = True
def prv(out):
    if VERBOSE:
        print(out)
# ok, i think we have our solution, a headless browser instance literally does the work for us. No need for googlesearch or rate limitting libraries
# implement full scraping capabilities in a model.
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--incognito")
try:
    geckodriver_path = "/snap/bin/geckodriver"  # specify the path to your geckodriver -> unfortunately have to do that since it cannot find it otherwise (firefox is installed with snap, selenium is not used to that)
    driver_service = Service(executable_path=geckodriver_path)
    driver = webdriver.Firefox(options=firefox_options,service=driver_service) 
except:
    driver = webdriver.Firefox(options=firefox_options) 


def search(query: str) -> list: # returns a list of urls with titles froma duckduckgo search
    driver.get(f"https://duckduckgo.com/?t=ffab&q={query}") # first run browser with search query
    search_soup = bs4.BeautifulSoup(driver.page_source,"html.parser")
    result_list = []
    for link in search_soup.find_all('li',attrs={"class":"wLL07_0Xnd1QZpzpfR4W"}):
        data_map = {}
        data_map["url"] = link.find("a",attrs = {"data-testid":"result-extras-url-link"})["href"] # catch the title and the url
        data_map["title"] = link.find("a",attrs= {"data-testid":"result-title-a"}).text
        result_list.append(data_map)
    return result_list



def read_url(url:str) -> bs4.BeautifulSoup: # reads a site, then returns its soup
    prv(f"Reading page: {url}")
    try:
        raw_data = requests.get(url,headers=rndhead())
        raw_data.encoding = "utf-8"
        raw_html = raw_data.text
    except:
        return f"Technical Issues"
    site_soup = bs4.BeautifulSoup(raw_html,"html.parser")
    return site_soup

def gather_info(query:str)->dict: # packages the information from a single searches websites into a hashmap
    reslt_list = search(query)
    site_list = []
    for x in reslt_list:
        site_list.append((read_url(x["url"]),x["title"],x["url"]))
    data_map = {}
    for site in site_list:
        soup = site[0]
        if soup=="Technical Issues":
            continue
        info_text = ""
        info_text+=f"{site[1]}\n"
        for cont in soup.find_all("p"):
            info_text+=cont.text+'\n'
            if len(info_text)>6000: # to prevent our models from crashing
                break
        data_map[site[2]]=info_text # set key value pair -> url:site text
    return data_map
