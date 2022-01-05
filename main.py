print("Menu:\n1 = Process Data\n2 = Visualise Data\n3 = Export Data\n4 = Exit ")
    opt = int(input("Choose an option: "))
    if opt == 1:
        print("\n1 = Record by Serial Number\n2 = Records by Observation Date\n3 = Group Records by Country/Region\n4 = Summarise Records")
    elif opt == 2:
        print("\n1 = Country/Region Pie Chart\n2 = Observations Chart\n3 = Animated Summary")
    elif opt == 3:
        print("\n1 = All Data\n2 = Data for Specific Country/Region")
    elif opt == 4:
        break
    else:
        print("Invalid Option. Choose number from 1 to 4")
        return opt