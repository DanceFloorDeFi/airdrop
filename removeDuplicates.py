import csv
# open file in read mode
with open('TheList.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
    # Iterate over each row in the csv using reader object

    data = {}

    counter = 0

    for row in csv_reader:
        # row variable is a list that represents a row in csv
        #print(row.upper())
        if row[0].lower() in data:
            data[row[0].lower()] = data[row[0].lower()] + float(row[1])
        else:
            data[row[0].lower()] = float(row[1])

        counter = counter + 1
        if(counter % 1000 == 0):
            print("checked " + str(counter))

print("==== done ====")
#print(data)

with open('FinalList.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    for key, value in data.items():
       write.writerow([key, value])
