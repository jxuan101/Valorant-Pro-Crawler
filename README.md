# Valorant Pro Match Scraper
Retrieves Valorant pro match data from [VLR](https://www.vlr.gg/).  
The purpose of this project is solely educational and nonprofit.  
Data is retrieved in a embedded List structure.  
The structure is returned containing:  

<ul>
    <li>Match
    <ul>
        <li>Date, Time, Patch Info
        <li>Team Names, Match Scores
        <li>Map Name, Agents
    </ul>
</ul>

**Example**: [This match](https://www.vlr.gg/28331/soniqs-vs-ghost-gaming-champions-tour-north-america-stage-3-challengers-2-qualifier-ro16) translates to [['Friday,', 'July', '23rd', '7:15', 'PM', 'EDT', 'Patch', '3.01'], ['Soniqs', '[1865]', 'final', '0', ':', '2', 'vs.', 'Bo3', 'Ghost', 'Gaming', '[1795]'], ['Breeze', 'jett', 'sova', 'viper', 'cypher', 'skye', 'jett', 'viper', 'cypher', 'sova', 'skye'], ['Split', 'cypher', 'jett', 'sage', 'kayo', 'omen', 'omen', 'sage', 'cypher', 'raze', 'kayo']]

# Requirements
[selenium](https://pypi.org/project/selenium/)==3.141.0  
[bs4](https://pypi.org/project/beautifulsoup4/)==0.0.1  
Make sure to install requirements.txt with pip before trying to run the script.
