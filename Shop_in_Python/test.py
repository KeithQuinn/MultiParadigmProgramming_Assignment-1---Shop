import csv

with open('../live.csv', 'w', newline="") as file:
    myFile = csv.writer(file)
    myFile.writerow(["Customer", 100.0])
    while True:
        try:
            Item = str(input("Enter Item (or x to quit): "))
            if Item == "x":
                break
            How_many = float(input("Enter quantity (or 0 to quit): "))
            if How_many == "0":
                break
            else:
                myFile.writerow([Item, How_many])
        except:
            print("")
        
