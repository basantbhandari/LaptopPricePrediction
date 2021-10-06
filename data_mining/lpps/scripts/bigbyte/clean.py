import csv

csvData = []
csvData1 = []
csvRow = []
csvFile = "../../cleaned-data/bigbyte.csv"
filePath = "../../extracted-data/bigbyte.txt"
headerRow = ['brandname','model','cpucore','clock','gpu','ram','ssd','hdd','display','displayquality','price','battery']

# function to get data from file
def getData(filepath):
    with open(filepath,'r') as file:
        data = file.readlines()
    return data

# function to write data to csv
def writeToCSV(csvfile):
    with open(csvfile,'w') as file:
        writer = csv.writer(file)
        # writing header row
        writer.writerow(headerRow)
        # writing data
        writer.writerows(csvData1)

# cleaning data
data = getData(filePath)
for row in data:
    # print(type(row))
    if(row == '\n'):
        continue
    else:
        csvRow.append(row)
        csvData.append(csvRow)
    csvRow = []

toAppend = []
for row in csvData:
    # print(row[0])
    content = row[0].split(',')
    # print(content)
    for i,element in enumerate(content):
        # print(element)
        if(len(toAppend) != 0):
            temp = content[i]
            # print(toAppend[0])
            content[i] = str(toAppend[0]) + temp 
            # print(content[i])
            toAppend = []
            if('\n' in content[i]):
                el = content[i].split('\n')
                # print(el)
                content[i] = el[0]
                # print(content[i])
                # print(element)

        if('NPR\xa0' in element):
            el = element.split('NPR\xa0')
            content[i] = el[0]
            toAppend.append(el[1])
    csvData1.append(content)
print(csvData1)
writeToCSV(csvFile)

