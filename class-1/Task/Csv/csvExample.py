from csv import reader,writer

#reading from text file
data,row = list(),True
with open("sample_text.txt",'r') as my_text_file:
    while row:
        row = my_text_file.readline().split()
        data.append(row)
for row in data:
    print row

print "\n\n\n\n"
#writing data into csv file
with open("sample_csv.csv",'w') as my_csv_file:
    write = writer(my_csv_file)
    for row in data:
        write.writerow(row)

#reading from csv file
with open("sample_csv.csv",'r') as my_csv_file:
    read = reader(my_csv_file)
    for row in read:
        print row


    
