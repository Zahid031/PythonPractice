nestDict={1:{'Name':"Zahid",'Age':'24','Sex':'M'},
          2:{'Name':'Faisa','Age':24}}
# print(nestDict)
# print(nestDict[2]['Name'])
# #addding elemnet to the dictionary
# nestDict[3]={}
# nestDict[3]['Name']='Sabbir'
# nestDict[3]['Age']=25
# print(nestDict)
# nestDict[4]={'Name':"Zahid",'Age':'24','Sex':'M'}
# print(nestDict)
# del nestDict[4]['Name']
# print(nestDict)
for p_id,p_info in nestDict.items():
    print("Person ID:",p_id)
    for key in p_info:
        print(key + ":", p_info[key])