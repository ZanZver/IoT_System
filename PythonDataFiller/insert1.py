import pymongo
import names
import random, string
from random_address import real_random_address

from random import randrange
from datetime import timedelta
from datetime import datetime
import json
from scipy import rand

#connectToDB
myclient = pymongo.MongoClient("mongodb://localhost:27019")
mydb = myclient["initialDB"]
colUsers = mydb["Users"]
colIoT_Customer_Device = mydb["IoT_Customer_Device"]
colIoT_Device_Info = mydb["IoT_Device_Info"]
colIoT_Device_History = mydb["IoT_Device_History"]

startDate = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
year2022 = datetime.strptime('1/1/2022 1:30 PM', '%m/%d/%Y %I:%M %p')

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

emailProviders = [ "@gmail.com", "@yahoo.com", "@apple.com", "@proton.com", "@customemail.com"]

lights_model_list = {
    "Philips": {
        "S-Li-1":{
            "Past_Updates": ["V1", "V2"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zwave"],
            "Spare_parts": []
        },
        "S-Li-2":{
            "Past_Updates": ["V1", "V2"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zwave"],
            "Spare_parts": []
        },
        "S-Li-3":{
            "Past_Updates": ["V1", "V2", "V3"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-4":{
            "Past_Updates": ["V1", "V2", "V3"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-5":{
            "Past_Updates": ["V1", "V2", "V3"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-6":{
            "Past_Updates": ["V1", "V2", "V3"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-7":{
            "Past_Updates": ["V1", "V2", "V3", "V4"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-8":{
            "Past_Updates": ["V1", "V2", "V3", "V4"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-9":{
            "Past_Updates": ["V1", "V2"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-10":{
            "Past_Updates": ["V1", "V2","V3", "V4"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-11":{
            "Past_Updates": ["V1", "V2", "V3"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-12":{
            "Past_Updates": ["V1", "V2"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-13":{
            "Past_Updates": ["V1", "V2"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        },
        "S-Li-14":{
            "Past_Updates": ["V1"],
            "Serial_Numbers":[],
            "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"],
            "Spare_parts": ["Bridge"]
        }
    }
}
fridge_model_list ={
    "Bosh": {
    "FR-01" :{
        "Past_Updates": ["V1", "V2"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee"]
        },
    "FR-02" :{
        "Past_Updates": ["V1", "V2", "V3", "V4"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee",]
        },
    "FR-03" :{
        "Past_Updates": ["V1", "V2", "V3"],
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" : ["Zigbee", "Zwave"]
        },
    "FR-04" :{
        "Past_Updates": ["V1", "V2", "V3"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee","Zwave"]
        },
    "FR-05" :{
        "Past_Updates": ["V1", "V2", "V3", "V4"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee", "Google home", "Zwave"]
        },
    "FR-06" :{
        "Past_Updates": ["V1", "V2", "V3", "V4"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee", "Google home", "Zwave"]
        },
    "FR-07" :{
        "Past_Updates": ["V1", "V2", "V3", "V4", "V5"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Zigbee", "Google home", "Zwave"]
        },
    "FR-08" :{
        "Past_Updates": ["V1", "V2", "V3", "V4", "V5"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "FR-09" :{
        "Past_Updates": ["V1", "V2", "V3", "V4", "V5"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "FR-010" :{
        "Past_Updates": ["V1", "V2", "V3", "V4", "V5", "V6"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "FR-011" :{
        "Past_Updates": ["V1", "V2", "V3", "V4"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"] 
        },
    "FR-012" :{
        "Past_Updates": ["V1", "V2", "V3", "V4", "V5", "V6"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "FR-013" :{
        "Past_Updates": ["V1", "V2", "V3"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "FR-014" :{
        "Past_Updates": ["V1", "V2"],
        "Serial_Numbers" : [],
        "IoT_Standard_Support" : ["Apple home kit", "Zigbee", "Google home", "Zwave"]
    }}
}
vacuum_model_list = {
    "Dyson":{
    "VC01" : {
        "Past_Updates": ["V1", "V2"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Zigbee"]
        },
    "VC02" : {
        "Past_Updates": ["V1", "V2", "V3"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Zigbee","Zwave"]
        },
    "VC03" : {
        "Past_Updates": ["V1", "V2", "V3"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Zigbee", "Google home", "Zwave"]
        },
    "VC04" : {
        "Past_Updates": ["V1", "V2"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Zigbee", "Google home", "Zwave"]
        },
    "VC05" : {
        "Past_Updates": ["V1", "V2", "V3", "V4"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "VC06" : {
        "Past_Updates": ["V1", "V2", "V3"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "VC07" : {
        "Past_Updates": ["V1", "V2", "V3"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "VC08" : {
        "Past_Updates": ["V1", "V2", "V3", "V4"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "VC09" : {
        "Past_Updates": ["V1", "V2"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Google home", "Zwave"]
        },
    "VC10" : {
        "Past_Updates": ["V1"], 
        "Serial_Numbers" : [], 
        "IoT_Standard_Support" :  ["Apple home kit", "Zigbee", "Zwave"]
        }
    }
}



food = ["Abalone",
"Açaí berries",
"Açaí juice",
"Acorn squash",
"Adzuki bean paste",
"Adzuki beans",
"Aged Japanese kurozu",
"Albacore tuna",
"Alcohol",
"Ale",
"Alfalfa sprouts",
"Algae",
"Almond milk",
"Almond paste",
"Almonds",
"Ancho chili powder",
"Anchovies",
"Anchovy paste",
"Angus beef",
"Apple juice",
"Apples",
"Apricots",
"Apricots, Japanese",
"Arborio rice",
"Arctic char",
"Artichoke, Jerusalem",
"Artichokes",
"Arugula",
"Asian greens",
"Asparagus",
"Asparagus, Chinese",
"Autumn crocus",
"Avocado oil",
"Avocados",
"Bacon",
"Balsamic vinegar",
"Bananas",
"Barbecued meat",
"Basil",
"Bean curd",
"Beef",
"Beer",
"Beets",
"Bell peppers",
"Bitter almond oil",
"Bitter cucumber",
"Bitter melon",
"Black beans",
"Black cumin",
"Black currants",
"Black or purple rice",
"Black pepper",
"Black tea",
"Blackberries",
"Blueberries",
"Bok choy",
"Boysenberries",
"Brazil nuts",
"Bread",
"Broccoli",
"Broccoli sprouts",
"Brown mustard",
"Brown rice",
"Brown rice syrup",
"Brussels sprouts",
"Buckwheat",
"Butter",
"Butternut squash",
"Cabbage",
"Canola oil",
"Cantaloupe",
"Carrots",
"Cashews",
"Cauliflower",
"Caviar",
"Celeriac",
"Celery",
"Celery seed",
"Chamomile",
"Cheese",
"Cherries",
"Chicken",
"Chickpeas",
"Chilli peppers",
"Chives",
"Chocolate",
"Cilantro",
"Cinnamon",
"Clams",
"Coconut",
"Coconut oil",
"Coffee",
"Collard greens",
"Corn",
"Corn oil",
"Crab",
"Cranberries",
"Cream",
"Cucumbers",
"Cumin",
"Curcumin",
"Currants",
"Daidzein",
"Dal",
"Dill",
"Dried herring",
"Dried mackerel",
"Dry beans",
"Edamame",
"Eggs",
"Escargot",
"Fennel",
"Fennel seed",
"Fermented bean paste",
"Fermented milk",
"Flaxseed",
"Flaxseed oil",
"Fried potatoes",
"Garbanzo beans",
"Garden cress",
"Garlic",
"Genistein",
"Ghee",
"Ginger",
"Grape seed oil",
"Grapefruit",
"Grapes",
"Gravy",
"Green beans",
"Green onions",
"Green papaya",
"Green peas",
"Green tea",
"Greens",
"Guacamole",
"Halibut",
"Ham",
"Herring",
"Holy basil",
"Honey",
"Honeydew melon",
"Horseradish",
"Hot peppers",
"Hummus",
"Indian mustard",
"Kale",
"Kefir",
"Kelp",
"Kidney beans",
"King mackerel",
"Kiwifruit",
"Kohlrabi",
"Kumquats",
"Lake trout",
"Lamb",
"Lard",
"Lavender",
"Leeks",
"Lemons",
"Lentils",
"Lettuce",
"Lima beans",
"Limes",
"Lingonberries",
"Liquor",
"Liver",
"Lobster",
"Loganberries",
"Long pepper",
"Low-fat yogurt",
"Macadamia nut oil",
"Macadamia nuts",
"Mackerel",
"Maitake mushrooms",
"Mangoes",
"Mangosteen",
"Margarine",
"Marionberrries",
"Maté",
"Mayonnaise",
"Melons",
"Mexican oregano",
"Milk",
"Mint",
"Mint tea",
"Mung beans",
"Mushrooms",
"Muskmelon",
"Mussels",
"Mustard",
"Mustard greens",
"Mustard oil",
"Mutton",
"Navy beans",
"Oatmeal",
"Oats",
"Octopus",
"Ohyo",
"Olive oil",
"Olives",
"Onions",
"Oranges",
"Oregano",
"Oysters",
"Papaya",
"Papaya seeds",
"Paprika",
"Parsley",
"Parsnips",
"Partially-hydrogen. oil",
"Passion fruit",
"Pâtés",
"Paw paw",
"Peaches",
"Peanut oil",
"Peanuts",
"Pears",
"Peas",
"Pecans",
"Peppermint",
"Persipan",
"Pesto sauce",
"Pickled papaya",
"Pickled watermel. rind",
"Pickles",
"Pineapple",
"Pinto beans",
"Pistachio nuts",
"Plantago",
"Plantains",
"Plums",
"Pomegranate juice",
"Pomegranates",
"Pork",
"Portobello mushrooms",
"Potatoes",
"Prunes",
"Pumpkin seeds",
"Pumpkins",
"Radicchio",
"Radish",
"Raisins",
"Rapeseed oil",
"Rapini",
"Raspberries",
"Red bean paste",
"Red beans",
"Red cabbage",
"Red currants",
"Red onions",
"Red pepper flakes",
"Red pepper paste",
"Red rice",
"Red spinach",
"Red wine vinegar",
"Reishi mushrooms",
"Rhubarb",
"Ribs",
"Rice",
"Rice bran",
"Rice bran oil",
"Rice wine vinegar",
"Risotto",
"Roast beef",
"Roasted almonds",
"Roasted pork",
"Roe",
"Rolled oats",
"Romaine lettuce",
"Rosemary",
"Rutabagas",
"Rye",
"Safflower oil",
"Saffron",
"Sage",
"Sage tea",
"Salmon, wild",
"Salt",
"Sardines",
"Sauerkraut",
"Sausages",
"Scallions",
"Scallops",
"Seaweed",
"Sesame oil",
"Sesame seeds",
"Shallots",
"Shellfish",
"Shiitake mushrooms",
"Shrimp",
"Smoked mackerel",
"Snails",
"Snow peas",
"Soba noodles",
"Soy infant formula",
"Soy milk",
"Soy protein bars",
"Soy protein isolate",
"Soybean curd",
"Soybean oil",
"Soybean paste",
"Soybeans",
"Spaghetti squash",
"Spearmint",
"Spinach",
"Split peas",
"Squash",
"Steak",
"Strawberries",
"String beans",
"Subtropical ginger",
"Sugar",
"Sugar beets",
"Sugar snap peas",
"Summer squash",
"Sunflower oil",
"Sunflower seeds",
"Sweet peas",
"Sweet potatoes",
"Tabasco sauce",
"Tahini",
"Tallow",
"Tangerines",
"Tartary buckwheat",
"Tea",
"Thyme",
"Tofu",
"Tomato paste",
"Tomatoes",
"Tropical ginger",
"Turkey",
"Turkey bacon",
"Turmeric",
"Turnip greens",
"Turnips",
"Veal",
"Vinegar",
"Wakame",
"Walnut oil",
"Walnuts",
"Wasabi",
"Watercress",
"Watermelon",
"Watermelon seeds",
"Well-done meat",
"Wheat bran",
"Wheat germ",
"Wheat grass",
"White beans",
"White bread",
"White button mush.",
"White pepper",
"White tea",
"White vinegar",
"Whole wheat bread",
"Wild ginger",
"Wild rice",
"Wine",
"Winter squash",
"Yams",
"Yerba maté",
"Yogurt",
"Zucchini"]

def createUser(num):
    for i in range(num):
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        items = ["", str(random.randrange(1,999))]
        random_item = random.choice(items)
        random_email = random.choice(emailProviders)
        random_address = real_random_address()
        #print(random_item)
        mydict = {
                "Username": firstname + lastname,
                "Password": randomword(10),
                "email": firstname + "." + lastname + random_item + random_email,
                "Name": firstname,
                "Surname": lastname,
                "Location": {
                    "Address": [
                        random_address["address1"],
                        random_address["address2"]
                    ],
                    "Postcode": random_address["postalCode"],
                    "City": random_address["state"],
                    "Country": "United States"
                }
        }
        x = colUsers.insert_one(mydict)
        createItAll(x.inserted_id)
        createHistory(x.inserted_id)
        
def createTheSmartLight():
    randomDeviceManufacturer = str(random.choice(list(lights_model_list.keys())))
    randomModel = str(random.choice(list(lights_model_list[randomDeviceManufacturer].keys())))
    randomSerial_Number = str(str(random.randrange(1,999999)) + "-" + str(random.randrange(1,999999))) #create fake SN
    lights_model_list[randomDeviceManufacturer][randomModel]["Serial_Numbers"] += [randomSerial_Number] #fill in the SN to the fridge
    randomVersion = str(random.choice(list(lights_model_list[randomDeviceManufacturer][randomModel]["Past_Updates"])))
    randomListOfSetDevices = random.sample(lights_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"], random.randrange(0,len(list(lights_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"]))) +1)
    spareParts = lights_model_list[randomDeviceManufacturer][randomModel]["Spare_parts"]
    
    Light_ID = {
            "Device_Details":{
                    "Online_Status": str(random.choice([True, False])),
                    "DeviceManufacturer": randomDeviceManufacturer,
                    "Model": randomModel,
                    "Serial_Number": randomSerial_Number,
                    "Last_Update": {
                        "Date": str(random_date(startDate, datetime.now())), 
                        "Version": randomVersion, 
                        "Update_Pending": str(random.choice([True, False]))
                    },
                    "Communication_Protocol_Set":randomListOfSetDevices,
                    "Spare_Parts": spareParts
                },
            "Device_Status":{
                    "Colour": f"#{random.randrange(0x1000000):06x}"
                }
            }
    
    return Light_ID

def createTheFridge():
    randomDeviceManufacturer = str(random.choice(list(fridge_model_list.keys())))
    randomModel = str(random.choice(list(fridge_model_list[randomDeviceManufacturer].keys())))
    randomSerial_Number = str(str(random.randrange(1,999999)) + "-" + str(random.randrange(1,999999))) #create fake SN
    fridge_model_list[randomDeviceManufacturer][randomModel]["Serial_Numbers"] += [randomSerial_Number] #fill in the SN to the fridge
    randomVersion = str(random.choice(list(fridge_model_list[randomDeviceManufacturer][randomModel]["Past_Updates"]))) #get random version based on the random model selected
    randomListOfSetDevices = random.sample(fridge_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"], random.randrange(0,len(list(fridge_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"]))) +1)
    randomFridgeFood = random.sample(food, random.randrange(1,len(food)//2))
    randomFreezeerFood = random.sample(food, random.randrange(1,len(food)//3))
    Fridge_ID = {
                "Device_Details": {
                    "Online_Status": str(random.choice([True, False])), 
                    "DeviceManufacturer": randomDeviceManufacturer,
                    "Model": randomModel,
                    "Serial_Number": randomSerial_Number,
                    "Last_Update": {
                        "Date": str(random_date(startDate, datetime.now())),
                        "Version": randomVersion,
                        "Update_Pending": str(random.choice([True, False]))
                    },
                    "Communication_Protocol_Set": randomListOfSetDevices
                },
                "Device_Status": {
                    "FridgeTemerature": random.randrange(0,5),
                    "FreezerTemperature": random.randrange(-5,0),
                    "Food_In_Fridge": randomFridgeFood,
                    "Food_In_Freezeer": randomFreezeerFood
                }
    }
    
    return Fridge_ID

def createTheVauum():
    randomDeviceManufacturer = str(random.choice(list(vacuum_model_list.keys())))
    randomModel = str(random.choice(list(vacuum_model_list[randomDeviceManufacturer].keys())))
    randomSerial_Number = str(str(random.randrange(1,999999)) + "-" + str(random.randrange(1,999999)))
    vacuum_model_list[randomDeviceManufacturer][randomModel]["Serial_Numbers"] += [randomSerial_Number]
    randomVersion = str(random.choice(list(vacuum_model_list[randomDeviceManufacturer][randomModel]["Past_Updates"]))) #get random version based on the random model selected
    randomListOfSetDevices = random.sample(vacuum_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"], random.randrange(0,len(list(vacuum_model_list[randomDeviceManufacturer][randomModel]["IoT_Standard_Support"]))) +1)
    lastEmptied = str(random_date(year2022, datetime.now()))
    lastCleaning = ""
    nextCleaning = ""
    
    while True:
        try:
            lastCleaning = str(random_date(year2022, datetime.strptime(lastEmptied, "%Y-%m-%d %H:%M:%S")))
            break
        except Exception as e:
            print(e)
      
    while True:  
        try:
            nextCleaning = str(random_date(datetime.strptime(lastCleaning, "%Y-%m-%d %H:%M:%S"), datetime.now()))
            break
        except Exception as e:
            print(e)
            
    cleaningPlan = random.choice(["Every 3h", "Every 6h", "Every 12h", "Once a day", "Once a week"])
    cleaningTimeSchedule = []
    if(cleaningPlan == "Every 3h"):
        for i in range(24//3):
            cleaningTimeSchedule.append(str(datetime.strptime(nextCleaning, "%Y-%m-%d %H:%M:%S") + timedelta(hours=3*i)))
    elif(cleaningPlan == "Every 6h"):
        for i in range(24//6):
            cleaningTimeSchedule.append(str(datetime.strptime(nextCleaning, "%Y-%m-%d %H:%M:%S") + timedelta(hours=6*i)))
    elif(cleaningPlan == "Every 12h"):
        for i in range(24//12):
            cleaningTimeSchedule.append(str(datetime.strptime(nextCleaning, "%Y-%m-%d %H:%M:%S") + timedelta(hours=12*i)))
    elif(cleaningPlan == "Once a day"):
        cleaningTimeSchedule.append(str(datetime.strptime(nextCleaning, "%Y-%m-%d %H:%M:%S") + timedelta(hours=24*1)))
    elif(cleaningPlan == "Once a week"):
        cleaningTimeSchedule.append(str(datetime.strptime(nextCleaning, "%Y-%m-%d %H:%M:%S") + timedelta(hours=24*7)))
    
        
    vacDict = {
            "Device_Details": {
                "Online_Status": str(random.choice([True, False])),
                "DeviceManufacturer": randomDeviceManufacturer,
                "Model": randomModel,
                "Serial_Number": randomSerial_Number,
                "Last_Update": {
                    "Date": str(random_date(startDate, datetime.now())), 
                    "Version": randomVersion, 
                    "Update_Pending": str(random.choice([True, False]))
                },
                "Communication_Protocol_Set": randomListOfSetDevices
            },
            "Device_Status":{
                "Battery_Percentage": random.randrange(0,100),
                "Dust_Disposer": {
                    "Status": random.choice(["Full", "Empty"]),
                    "Last_Emptied": lastEmptied,
                },
                "Cleaning_Schedule": {
                    "Last_Cleaning": lastCleaning, 
                    "Next_Cleaning": nextCleaning, 
                    "Cleaning_Plan": cleaningPlan, 
                    "Cleaning_Time_Schedule": cleaningTimeSchedule
                }
            }
    }
    
    return vacDict

def createDevices():
    devDic ={"Smart light":{},
             "Smart fridge":{},
             "Smart vacuum":{}}
    numOfRandomLights = random.randrange(0,30)
    numOfRandomFridges = random.randrange(0,3)
    numOfRandomVacumms = random.randrange(0,10)
    for i in range(numOfRandomLights):
        devDic["Smart light"] = {**devDic["Smart light"],  **{str(i):createTheSmartLight()}}
        
    for i in range(numOfRandomFridges):
        devDic["Smart fridge"] = {**devDic["Smart fridge"],  **{str(i):createTheFridge()}}
        
    for i in range(numOfRandomVacumms):
        devDic["Smart vacuum"] = {**devDic["Smart vacuum"],  **{str(i):createTheVauum()}}
        
    return devDic

def createDeviceInfo():
    #print(str(lights_model_list).replace("""'""",'''"''' ))
    devInfoDic = {"Smart light":{},
                  "Smart fridge":{},
                  "Smart vacuum":{}}
    for i in list(lights_model_list.keys()):
        devInfoDic["Smart light"] = {**devInfoDic["Smart light"],  **{i:list(lights_model_list.values())}}
        
    for i in list(fridge_model_list.keys()):
        devInfoDic["Smart fridge"] = {**devInfoDic["Smart fridge"],  **{i:list(fridge_model_list.values())}}
        
    for i in list(vacuum_model_list.keys()):
        devInfoDic["Smart vacuum"] = {**devInfoDic["Smart vacuum"],  **{i:list(vacuum_model_list.values())}}
    
    return devInfoDic
    
def createItAll(UserID):
    colIoT_Customer_Device.insert_one({str(UserID):createDevices()})
    
    dict1 = createDeviceInfo()
    try:
        dict2 = colIoT_Device_Info.find_one()["Device_Info"]
        for deviceTypes in dict1.keys():
            for manufacturer in dict1[deviceTypes].keys():
                for modelName in list(dict1[deviceTypes][manufacturer])[0].keys():
                    for serialNumber in list(dict2[deviceTypes][manufacturer])[0][modelName]["Serial_Numbers"]:
                        list(dict1[deviceTypes][manufacturer])[0][modelName]["Serial_Numbers"].append(serialNumber)
                    
        oldquery = { "Device_Info": colIoT_Device_Info.find_one()["Device_Info"] }
        newquery = { "$set": { "Device_Info": dict1 } }

        colIoT_Device_Info.update_one(oldquery, newquery)
    except:
        colIoT_Device_Info.insert_one({"Device_Info":dict1})
        
def createHistory(userID):
    lightHistoryGenerator = random.randrange(1,30)
    fridgeHistoryGenerator = random.randrange(1,30)
    vacuumHistoryGenerator = random.randrange(1,30)
    for i in range(lightHistoryGenerator):
        colIoT_Device_History.insert_one({str(userID): {"1": createTheSmartLight()["Device_Status"]}})
    
    for i in range(fridgeHistoryGenerator):
        colIoT_Device_History.insert_one({str(userID): {"2": createTheFridge()["Device_Status"]}})
        
    for i in range(vacuumHistoryGenerator):
        colIoT_Device_History.insert_one({str(userID): {"3": createTheVauum()["Device_Status"]}})

createUser(10)