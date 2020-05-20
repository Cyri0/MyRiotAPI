import requests
import json

def requestSummonerData(summonerName, APIKey):
 
    URL = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+summonerName+"?api_key=" + APIKey
    response = requests.get(URL)
    responseJSON = str(response.json())

    responseJSON = responseJSON.replace("'", "\"")    
    responseDict = json.loads(responseJSON)
    return responseDict

def requestHero(summID, APIKey):
    URL = "https://eun1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/"+summID+"?api_key=" + APIKey
    response = requests.get(URL)
    responseJSON = str(response.json())

    responseJSON = responseJSON.replace("'", "\"")
    responseJSON = responseJSON.replace("True", "1") 
    responseJSON = responseJSON.replace("False", "0")    
    responseDict = json.loads(responseJSON)
    
    return responseDict
    
def getHeroNameById(id):
    URL = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"
    response = requests.get(URL)
    responseJSON = response.json()
    champDict = responseJSON["data"]
    for champ in champDict:
        champKey = int(champDict[champ]["key"])
        if champKey == id:
            champName = champDict[champ]["id"]
            champTitle = champDict[champ]["title"]
            tags = champDict[champ]["tags"]
            tagString = ""
            for tag in tags:
                tagString = tagString + tag + " "

            return champName + " - " + champTitle + " ( " + tagString + ")"

    return "Nincs ilyen hos! (id: " +str(id)+ ")" 

def main():

    summonerName = input('Add meg az idéző nevét! \n')
    APIKey = input('Add meg az API key-t! (https://developer.riotgames.com/ )\n')

    responseSummoner  = requestSummonerData(summonerName, APIKey)
    
    print("Idéző neve: " + responseSummoner["name"])
    summID = responseSummoner["id"]
    print("Idéző szintje: " + str(responseSummoner["summonerLevel"]))

    heroDict = requestHero(summID, APIKey)
    print("Kedvenc hosok:\n")
    counter = 0
    for hero in heroDict:
        print(getHeroNameById(int(hero["championId"])))
        counter += 1
        if counter == 5:
            break


#This starts my program!
if __name__ == "__main__":
    main()

