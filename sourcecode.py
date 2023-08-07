import csv

def main():
    # load data
    aI = []
    aF = []
    f = open("AllergenIndex.csv", encoding="utf8")
    r = csv.reader(f)
    for row in r:
        aI.append(row)
    f.close
    f = open("AllergenFamilies.csv", encoding="utf8")
    r = csv.reader(f)
    for row in r:
        aF.append(row)
    f.close
    
# main window
    lst = []
    x = 0
    b = False
    
    # textBox
    print ("Please enter your allergies one at a time. Click remove to remove your last answer. Click done when finished.")
    while x != "done":
    
    # inputBox    
        x = input()w
        if len(x) > 2:
            if len(lst) > 0 and x == "remove":
                print("Removed " + lst[-1][1].title())
                lst = lst[:-1]
            elif len(lst) < 1 and x == "remove":
                print("There is nothing to remove")
            else:
                for i in aI:
                    if (x[0].upper() + x[1:]) in i[1]:
                        if not(i in lst):
                            lst.append(i)
                            b = True
                        else:
                            print("Repeated allergy identified")
                            b = True
                if not b and x != "done":
                    print("Allergy not recognized")
                b = False
        else:
            print("Invalid answer")
    
    # resultBox 
        print(lst)
    
    uA = lst
    
# second window
    y = ""
    uRelated = []
    uBreakdown = []
    for i in uA:
        for j in aF:
            if i[0] == j[0]:
                y = y + "the " + j[1] + " which includes "
                for k in j[2:-1]:
                    y = y + k.title() + ", "
                    uRelated.append(k.title())
                y = y[:-1] + j[-1].title()
                uRelated.append(j[-1].title())
        uBreakdown.append("Your allergy to " + i[1] + " suggests you could be allergic to " + y)
        y = ""
    # textBox
    print()
    print("Confirmed Allergies")
    print("-------------------")
    for m in uA:
        print(m[1])
    print()
    print("Possible Allergies")
    print("------------------")
    for n in uRelated:
        print(n)
    print()
    
    # inputBox
    if len(uA) > 1:
        o = input("Type yes to show report breakdown")
        if o.lower() == "yes":
    
    # resultBox
            for p in uBreakdown:
                print()
                print(p)

main()