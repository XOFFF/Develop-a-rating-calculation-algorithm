import json
import datetime
from Person import Person
import Functions
from os import walk

listOfUsers = []
listOfUserId = []

folder_path = 'C:/Users/marke/Desktop/cache files/cache/'

f = []
for (dirpath, dirnames, filenames) in walk(folder_path):
    f.extend(filenames)
    print(f)

for eachFile in f:
    print('working ............................................................................................................................................')
    # text = f.read()
    # Opening JSON file
    file = open(folder_path + eachFile, )

    dataFromJSON = json.load(file)
    file.close()

    # Implementing variables
    listOfUsersCache = []
    typeOfRoom = 0
    currentUserId = 0
    firstTime = 0
    lastTime = 0

    # Code  to recognize the room in cache
    for item in dataFromJSON:
        listOfUsersCache.append((item['id'], item['Date time']))
        #     print(item)
        if item == dataFromJSON[0]:
            typeOfRoom = item['Room id']
            print(typeOfRoom)

    for eachItem in listOfUsersCache:
        print(eachItem)
        # if first item from file
        if currentUserId == 0:
            currentUserId = eachItem[0]
            if eachItem[0] not in listOfUserId:
                print('wow, new id!')
                listOfUserId.append(currentUserId)
            firstTime = eachItem[1]
            lastTime = eachItem[1]
        if len(listOfUsers) == 0:
            # object
            # listOfUsers.append(Person(currentUserId, 0, 0))
            # dictionary
            listOfUsers.append(dict({'User id': currentUserId, 'Time': {'On work': 0, 'On rest': 0}}))

        # Check if it is not first item from file  AND  if we got new user id in the item
        if eachItem[0] != currentUserId and eachItem != listOfUsersCache[-1] and len(listOfUsers) != 0:
            # Get the difference from first and last value with same user id from current item in file
            print('First time:', firstTime)
            print('Last time:', lastTime)
            difference = Functions.findDifference(firstTime, lastTime)
            print('Difference:', difference)
            difference = difference.total_seconds()
            print('Difference in seconds:', difference)
            # Check if got the same user id before
            if currentUserId not in listOfUserId:
                # Add new user to listOfUsers
                listOfUserId.append(currentUserId)
                listOfUsers.append(dict({'User id': currentUserId, 'Time': {'On work': 0, 'On rest': 0}}))
                print('wow, new id!')

            # Now we set the difference time to exactly right typeOfRoom to the user in listOfUsers

            if typeOfRoom == 1:
                for userInfo in listOfUsers:
                    if userInfo['User id'] == currentUserId: #and userInfo['Time']['On work'] == 0:
                        userInfo['Time']['On work'] += difference
            if typeOfRoom == 2:
                for userInfo in listOfUsers:
                    if userInfo['User id'] == currentUserId: #and userInfo['Time']['On work'] == 0:
                        userInfo['Time']['On rest'] += difference

            # last sets after we got new User id in the item
            currentUserId = eachItem[0]
            if eachItem != listOfUsersCache[-1]:
                    firstTime = eachItem[1]

        # if last item from file
        if eachItem == listOfUsersCache[-1]:
            print('last value')
            # set some variables for calculations for last item
            lastTime = eachItem[1]
            difference = Functions.findDifference(firstTime, lastTime).total_seconds()

            # Now we set the difference time to exactly right typeOfRoom to the user in listOfUsers

            if typeOfRoom == 1:
                for userInfo in listOfUsers:
                    if userInfo['User id'] == currentUserId: #and userInfo['Time']['On work'] == 0:
                        userInfo['Time']['On work'] += difference
            if typeOfRoom == 2:
                for userInfo in listOfUsers:
                    if userInfo['User id'] == currentUserId: #and userInfo['Time']['On work'] == 0:
                        userInfo['Time']['On rest'] += difference

        lastTime = eachItem[1]
    # Final step
    Functions.saveIntoOutputFile(listOfUsers)