import csv
def hel():
    with open('resources/help.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
        print("Symbol", "Unit")
        for i in mydict.keys():
            print("---------------------------------------------------------------------")
            print(i, "\t\t\t", mydict[i])
        print("---------------------------------------------------------------------")
        print("For Area put sq after length unit")
        print("Example:- \nFor converting m to cm \nEnter the type of conversion : length\nEnter the conversion to be done : m cm ")
