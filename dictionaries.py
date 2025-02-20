# Dictionaries:
dic = {
    1: [12,"A","AHMED","DATASCIENCE"],
    2: ("ALI",'p',1122),
    3: "Pakistan"
}
dic[1][0] = 11 #overwrighting a value
dic[0] = [1,2,3] #saving a new key value
print(dic[0])

# nested dictionaries:
dictionary = {
    "Name" : "Ahmed",
    "Subjects" : {
        "PF" : 100,
        "AICT" : 100,
        "DM" : 90,
        "Calculus" : 92,
    "Roll no." : 25
    }
}
print(dict["Subjects"]["Calculus"])

#Methods:
print(dict.keys())

#Typecasting:
print(tuple(dictionary))
list1 = [[1,"AJ"],[2,"ALI"],[3,"TAAHA"]]
print(dict(list1))

#adding a new key value pairs(it can also be used to update the old key values):
#creating new:
new_dic = {"city":"Gujranwala"}
dictionary.update(new_dic)
print(dictionary["city"])
#or
dictionary.update({"city":"Gujranwala"})
print(dictionary["city"])

#updating previous one:
dictionary.update({"name":"AJ"})
print(dictionary['name'])