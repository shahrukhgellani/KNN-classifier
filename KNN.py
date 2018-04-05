import csv
import math
with open('iris.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar = '|')
    list = []
    for row in spamreader:
         list.append(row)
def spliter(dataset , ratio):
     Training = []
     Testing = []
     length = int(len(dataset)*ratio)
     for i in dataset:
          if(dataset.index(i) < length):
               Training.append(i)
          else:
               Testing.append(i)
     return Training,Testing
Training , Testing = spliter(list,0.8)
pair = []
touplelist = []
list2 = []
final_list = []
distance = 0
for j in Testing:
     for i in Training:
          for k in range(len(i)-1):
               distance += (float(j[k]) - float(i[k]))**2   # finding distance
          distance = math.sqrt(distance)                    # finding distance
          pair.append((distance,i[k+1]))                    # list of touples having distanc and city name
          distance = 0
     touplelist.append(pair)                                #list of touple having distance and city name
     pair = []

n = input("Enter number for minimum distances = ")
for i in range(len(touplelist)):
     list2 = touplelist[i]                   #list according to city
     list2.sort()                            #sorted distance of every city
     #print(list2)
     list3 = list2[:int(n)]                 #First n nearest distances
     print(list3)
     list4 = [x[1] for x in list3]
     print(list4)
     dict1 = {}
     for city in list4:
          if not city in dict1:
               dict1[city] = 1
          else:
               dict1[city] += 1
     num = 0
     print(dict1)
     for key in dict1:
          print(dict1[key])
          if (dict1[key] > num):
               num = dict1[key]
     print(num)
     for key in dict1:
          if (dict1[key] == num):
               final_list.append(key)
print(final_list)
print(Testing)
print(len(Testing))
print(len(final_list))
print(len(touplelist))
testing_list = [x[4] for x in Testing]
print(testing_list)
number = 0
for i in range(len(final_list)):
     if(testing_list[i] == final_list[i]):
          number += 1
     
accuracy = (number/len(Testing))* 100
print(accuracy)
     
          


