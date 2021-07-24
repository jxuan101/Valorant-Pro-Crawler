from selenium import webdriver
from bs4 import BeautifulSoup
import sys

# Retrieves the href for all matches on the page
def get_matches(card):
    results = []
    for tag in card:
        links = tag.find_all('a')
        for link in links:
            results.append(link.get("href"))
    return results

# Retrieves the agents for the map
def get_agents(map):
    results = []
    agents = map.find_all(lambda tag: tag.name == "td" and tag.get("class") == ["mod-agents"])
    for agent in agents:
        agent_name = agent.find("img")
        results.append(agent_name.get("title"))
    return results


def main():

    driver = webdriver.Chrome("./chromedriver")

    ## Getting all the match links -- Finished 

    match_links = []

    # 50 matches per page amounts to 200 matches total
    pages = ["","?page=2", "?page=3", "?page=4"]

    for page in pages:
        link = "https://www.vlr.gg/matches/results/" + page
        driver.get(link)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        page_results = soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ["wf-card"])
        match_links += get_matches(page_results)

    ## Getting all the agents in each map played during the match -- Finished
    for match in match_links:
        link = "https://www.vlr.gg" + match
        driver.get(link)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        all_maps = []

        # Get the date and time of the match -- Finished
        page_results = soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ["match-header-date"])
        match_date = page_results[0].text.split()
        all_maps.append(match_date)

        # Get team names and final scores -- Finished
        page_results = soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ["match-header-vs"])
        match_stats = page_results[0].text.split()
        all_maps.append(match_stats)

        # Get data for each map [[map1, agents...], [map2, agents...]] -- Finished
        maps = soup.find_all(lambda tag: tag.name == "div" and tag.get("class") == ["vm-stats-game"])
        for map in maps:
            map_name = map.find(lambda tag: tag.name == "div" and tag.get("class") == ["map"])
            if map_name == None:
                map_name = soup.find(lambda tag: tag.name == "div" and tag.get("class") == ["vm-stats-game-header"])
                map_name_text = map_name.find(lambda tag: tag.name == "div" and tag.get("class") == ["map"]).text.split()[0]
            else:
                map_name_text = map_name.text.split()[0]
            data = []
            agents = []
            agents = get_agents(map)
            data.append(map_name_text)
            data += agents
            all_maps.append(data)

        print (all_maps)

    ## Exit
    driver.close()
    sys.exit()

if __name__ == '__main__':
    main()