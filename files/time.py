import csv
def time():
    with open('resources/time.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict2 = {rows[0]:rows[1] for rows in reader}
        ut1,ut2 = input("Enter the conversion to be done : ").split()
        it1 = float(input("Enter the numeric value : "))
        try:
            if ut1 == "sec":
                it2 = ut1 + " to " + ut2
                cft = float(mydict2[it2])
                print(it1*cft, ut2)
            elif ut2 == "sec":
                it2 = "sec to " + ut1
                cft = float(mydict2[it2])
                print(it1*(1/cft), ut2)
            else:
                it2 = "sec to " + ut1
                cft1 = float(mydict2[it2])
                tvt = it1*(1/cft1)
                it3 = "sec to " + ut2
                cft2 = float(mydict2[it3])
                print(tvt*cft2, ut2)
        except:
            print("Conversion not Possible")
