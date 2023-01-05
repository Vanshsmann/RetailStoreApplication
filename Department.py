import csv
import os.path
#from colorama import Fore, Style

def search(upc, department):
    notfound = 1
    f = open("NewPricebook.csv", "a")  # Create new Pricebook
    with open('pricebook29174.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:

            currentstring = f'{",".join(row)}'  # Turn Current Row into string
            upcstring = currentstring.split(',', 1)[0]  # Gets first Attribute which is UPC

            if upcstring == upc:  # IF UPC IS MATCH
                # SPLIT STRING TILL DEPARTMENT IS REACHED
                commastring = ','
                # This Function splits UPC away
                rowarray = currentstring.split(commastring, -1) #Turn Row into Array
                rowarray[1] = department #Change department
                updatedstring = rowarray[0] + "," + rowarray[1] + "," + rowarray[2] + "," + rowarray[3] + "," + \
                                rowarray[4] + "," + rowarray[5] + "," + rowarray[6] + "," + rowarray[7] + "," + \
                                rowarray[8] + "," + rowarray[9] + "," + rowarray[10] + "," + rowarray[11] + "," + \
                                rowarray[12] + "," + rowarray[13]
                f.write(updatedstring + "\n")
                #print("FOUND AND CHANGED")
                notfound = 0
            line_count += 1

    if notfound == 1:
        print("NOT FOUND")
        #print(Fore.RED +"NOT FOUND")
        #print(Style.RESET_ALL)
    f.close()


# Begin Code Here


# Ask user if we should delete previous book
deletePriceBook = input("Would you like to delete the updated pricebook? Y|N? ")
if deletePriceBook == 'Y':
    if os.path.exists('NewPricebook.csv'):  # if file exist then remove
        os.remove("NewPricebook.csv")
    c = open("NewPricebook.csv", "a")  # Create new Pricebook
    c.write(
        "upc,Department,qty,cents,incltaxes,inclfees,Name,size,ebt,byweight,Fee Multiplier,Stock,cost_cents,cost_qty\n")
    print("New Pricebook Created\n")
    c.close()

# Ask department name
newDepartment = input("Department Name:")
scannedupc = ''  # Create UPC Entity Initialize as NULL string
while scannedupc != 'Q':  # If user types in Q then quit
    scannedupc = str(input("Scan UPC, or type 'Q': "))
    if scannedupc != 'Q':
        search(scannedupc, newDepartment)
