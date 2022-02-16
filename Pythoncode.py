#Tell python to open the list we save in our repo from the url
with open("http_access_log.txt") as file_in:
    #Set array to look for specific data
    array = []
    for line in file_in:
        array.append(line)

 # Start the value at 0 so it can add up later to give us our numbers       
count = 0

#tell it to look for specific months and what year to get last 6 months and start counting for each entry
for i in array:
    if i.find("Apr") != -1 and i.find("1995") != -1 and i.find("[11") != -1:
        count += 1
    elif i.find("May") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jun") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jul") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Aug") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Sep") != -1 and i.find("1995") != -1:
        count += 1
        array[count] = i
    elif i.find("Oct") != -1 and i.find("1995") != -1:
        count += 1

#count all the entries by using the array (gives us boundaries) function inside a len (counts the length) function
countall = len(array)

#Print out the info they were asking and the results
print("Total Number of Requests in the past six months: ", count)
print("Total Number of Requests: ", countall)
