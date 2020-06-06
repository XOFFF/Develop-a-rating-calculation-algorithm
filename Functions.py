import datetime
import json
# roomId, listOfUsers, i, difference, Person, currentUserId
# def saveTime(listOfUsers, currentUserId, Person):
def findDifference(firstTime, lastTime):
    first_time = datetime.datetime.strptime(firstTime, '%Y-%m-%d %H:%M:%S.%f')
    later_time = datetime.datetime.strptime(lastTime, '%Y-%m-%d %H:%M:%S.%f')
    return  later_time - first_time

def saveIntoOutputFile(listOfUsers):
    data = []
    for userInfo in listOfUsers:
        data.append({
            'User id': userInfo['User id'],
            'Time spent on work': userInfo['Time']['On work'],
            'Time spent on rest': userInfo['Time']['On rest']
        })
        print(userInfo)

# def saveIntoOutputFile2(listOfUsers):
#     data = []
#     for s in listOfUsers:
#         data.append({
#             'User id': s.persId,
#             'Time spent on work': str(s.workRoomTime),
#             'Time spent on rest': str(s.restRoomTime)
#         })
#         s.printPersInfo()

    with open('C:\\Users\\marke\\Desktop\\cache files\\cache output\\cache_output.json', 'w') as outfile:
        json.dump(data, outfile, indent=3)