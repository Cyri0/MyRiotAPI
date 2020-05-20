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
    switcher = {
        266: "Aatrox",
        412: "Thresh",
        23: "Tryndamere",
        79: "Gragas",
        69: "Cassiopeia",
        136: "AurelionSol",
        13: "Ryze",
        78: "Poppy",
        14: "Sion",
        1: "Annie",
        202: "Jhin",
        43: "Karma",
        111: "Nautilus",
        240: "Kled",
        99: "Lux",
        103: "Ahri",
        2: "Olaf",
        112: "Viktor",
        34: "Anivia",
        27: "Singed",
        86: "Garen",
        127: "Lissandra",
        57: "Maokai",
        25: "Morgana",
        28: "Evelynn",
        105: "Fizz",
        74: "Heimerdinger",
        238: "Zed",
        68: "Rumble",
        82: "Mordekaiser",
        37: "Sona",
        96: "Kog'Maw",
        55: "Katarina",
        117: "Lulu",
        22: "Ashe",
        30: "Karthus",
        12: "Alistar",
        122: "Darius",
        67: "Vayne",
        110: "Varus",
        77: "Udyr",
        89: "Leona",
        126: "Jayce",
        134: "Syndra",
        80: "Pantheon",
        92: "Riven",
        121: "Kha'Zix",
        42: "Corki",
        268: "Azir",
        51: "Caitlyn",
        76: "Nidalee",
        85: "Kennen",
        3: "Galio",
        45: "Veigar",
        432: "Bard",
        150: "Gnar",
        90: "Malzahar",
        104: "Graves",
        254: "Vi",
        10: "Kayle",
        39: "Irelia",
        64: "LeeSin",
        420: "Illaoi",
        60: "Elise",
        106: "Volibear",
        20: "Nunu",
        4: "TwistedFate",
        24: "Jax",
        102: "Shyvana",
        429: "Kalista",
        36: "Dr.Mundo",
        427: "Ivern",
        131: "Diana",
        223: "TahmKench",
        63: "Brand",
        113: "Sejuani",
        8: "Vladimir",
        154: "Zac",
        421: "Rek'Sai",
        133: "Quinn",
        84: "Akali",
        163: "Taliyah",
        18: "Tristana",
        120: "Hecarim",
        15: "Sivir",
        236: "Lucian",
        107: "Rengar",
        19: "Warwick",
        72: "Skarner",
        54: "Malphite",
        157: "Yasuo",
        101: "Xerath",
        17: "Teemo",
        75: "Nasus",
        58: "Renekton",
        119: "Draven",
        35: "Shaco",
        50: "Swain",
        91: "Talon",
        40: "Janna",
        115: "Ziggs",
        245: "Ekko",
        61: "Orianna",
        114: "Fiora",
        9: "Fiddlesticks",
        31: "Cho'Gath",
        33: "Rammus",
        7: "LeBlanc",
        16: "Soraka",
        26: "Zilean",
        56: "Nocturne",
        222: "Jinx",
        83: "Yorick",
        6: "Urgot",
        203: "Kindred",
        21: "MissFortune",
        62: "Wukong",
        53: "Blitzcrank",
        98: "Shen",
        201: "Braum",
        5: "XinZhao",
        29: "Twitch",
        11: "MasterYi",
        44: "Taric",
        32: "Amumu",
        41: "Gangplank",
        48: "Trundle",
        38: "Kassadin",
        161: "Vel'Koz",
        143: "Zyra",
        267: "Nami",
        59: "JarvanIV",
        81: "Ezreal"
    }
    return switcher.get(id, "Nincs ilyen hos! (Vagy nagyon uj...)")

def main():
    #I first ask the user for three things, their region, summoner name, and API Key.
    #These are the only three things I need from them in order to get create my URL and grab their ID.

    summonerName = input('Add meg az idéző nevét! \n')
    APIKey = input('Add meg az API key-t! (https://developer.riotgames.com/)\n')

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseSummoner  = requestSummonerData(summonerName, APIKey)
    
    print("Idéző neve: " + responseSummoner["name"])
    summID = responseSummoner["id"]
    #print("Idéző ID: " + summID)
    print("Idéző szintje: " + str(responseSummoner["summonerLevel"]))

    heroDict = requestHero(summID, APIKey)
    print("Kedvenc hosok:\n")
    for hero in heroDict:
        print("\t - " + getHeroNameById(hero["championId"]) +" (" + str(hero["championPoints"]) + ")")

#This starts my program!
if __name__ == "__main__":
    main()

