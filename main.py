# Loop Buffer Scholarship database - Team Switch
# Participants - Abha Barge, Aditi Mahadik, Mitali Badamikar



class Node:
    def __init__(self, data):
        self.data = data
        self.nexref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print("Nothing added in wishlist!")

        else:
            n = self.head
            while n.nexref is not None:
                print(n.data)
                n = n.nexref
            print(n.data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.nexref is not None:
                n = n.nexref
            n.nexref = new_node

    def delnode(self):
        print("Enter the number of element you want to delete")
        c1 = int(input())
        bfrc1 = c1 - 1
        delete = 1
        nod = self.head

        if c1 != delete:
            while bfrc1 != delete:
                delete = delete + 1
                nod = nod.nexref

            if bfrc1 == delete:
                nod.nexref = nod.nexref.nexref

        if c1 == delete:
            newhd = nod.nexref
            self.head = newhd




def filters(crit, lst):
    if crit in lst:
        return True
    else:
        return False


ll = LinkedList()
queue = []
accs = [[]]


def enqueue(ele):
    queue.append(ele)


def dequeueall():
    while queue:
        queue.pop(0)


def adw(qu):
    if qu:
        print("Do you want to add any scholarship to wishlist? 1-Yes 0-No")
        wshlst = int(input())
        if wshlst == 1:
            print("Enter the number of the  scholarship you wish to add: ")
            num = int(input())
            ind = num-1
            ll.append(qu[ind][0])
            adw(qu)

    else:
        print("No scholarships for this filter!")


sclist = [
        [["Santoor Women's Scholarship", "   -Scholarship of INR 24,000 to talented underprivileged girl students",
          "   -16 years of age, enrolled in high-school", "   -Apply before 1/10/2023"], [2, "nb", "girl", "sci"]],

        [["L&T Build India Scholarship", "   -Scholarship of INR 13,400 per month",
          "   -For students pursuing B.E./ B.Tech. in core Civil Engineering & core Electrical Engineering(21-23 yrs)",
          "   -Apply before 28th February 2023"], [3, "tb", " ", "sci"]],

        [["Begum Hazrat Mahal National Scholarship",
          "   -Scholarship worth INR 10,000 to INR 12,000 annually for girl students belonging to minority communities ",
          "   -For Girl students studying from Class 9 to 12(14-18 yrs)", "   -Apply before 30 September 2022 "],
         [2, "nb", "girl ", "sci "]],

        [["SOF Scholarship of Excellence in English (S.E.E.)",
          "   -Scholarship to recognize the student's excellence in the English Language with variable rewards",
          "   -For students studying from Class 1 to 10(6-16 yrs)", "   -Apply before 28th February 2023"],
         [1, 2, "tb", " ", "arts"]],

        [["AAI Sports Scholarship Scheme",
          "   -Scholarship worth INR 16000 per month with the aim to enhance sporting standards",
          "   -For Applicants aged 14 to 24 years", "   -Apply before 15th March 2023"], [2, 3, "tb", " ", "sports"]],

        [["INSPIRE Scholarship For Higher Education (SHE) ",
          "   -Scholarship of INR 80000 per annum to provide financial help to students who have passed Class 12",
          "   -For students aged 17-22 yrs and have passed Class 12 examination from any Central/State board in "
          "India with aggregate marks within the top 1% of Class",
          "   -Apply before 31st October 2022"], [2, 3, "tb", " ", "sci"]],

        [["National Scholarship Exam (NSE)",
          "   -Scholarship up to INR 25000 with the aim to identify and nurture talented students ",
          "   -For students studying from Class 5 to 12(11-18 yrs)", "   -Apply before 20th October 2022"],
         [1, 2, "tb", " ", "sci"]],

        [["Abhilasha Scholarship 2023", "   -Scholarship for girl students worth INR 5000",
          "   -For Girl students studying from Class 9 to 12(14-18 yrs)", "   -Apply before 20th April 2023"],
         [2, "nb", "girl ", "sci"]],

        [["Kishore Vaigyanik Protsahan Yojana (KVPY)",
          "   - scholarship of up to INR 7,000 per month and a contingency grant ",
          "   -For students aged 17-20 yrs pursuing bachelor's and master's degrees in the science stream",
          "   -Apply before 6th September 2023"], [2, 3, "tb", " ", "sci"]],

        [["NISD National Sports Scholarship",
          "   -Scholarship up to INR 9000 for all talented and proved achievers in sports ",
          "   -For Applicants aged 8 to 21 yrs ", "   -Apply before 15th January 2023"],
         [1, 2, 3, "tb", " ", "sports"]],

        [["Abdul Kalam Technology Innovation National Fellowship ", "   -Monthly Fellowship monthly worth INR 25,000",
          "   -Applicants must hold at least a bachelor’s degree(aged above 22 yrs)",
          "   -Apply before 30th June 2023"], [3, "tb", " ", "sci"]],

        [["D.K Bhave scholarship by Savitribai Phule Pune university",
        "    -Upto INR 5 lakhs", "    -For pursuing masters degree in engineering and technology in foreign accredited "
            "universities", "    -Application dates vary"],[3, "sci", "tb"]],

        [["Rolls royce Unnati Scholarship Programme for women in engineering",
         "    -Provides financial aid for 1st,2nd,3rd year engineering students ","    -Women in Engineering",
          "    -last date 15/5/23"],[3, "sci", "girl", "nb"]],

        [["HDFC Bank Parivartan’s ECS Scholarship", "     -INR 15-18k aims to support meritorious" 
        "and needy students belonging to underprivileged sections of the society ","    -Financial need demonstrated",
          "    -Application dates – check website"],[1,2, "tb"]],

        [["LIC HFL Vidyadhan Scholarship", "    -INR 20,000", "    -Initiative of LIC Housing Finance Limited (LIC HFL)"
            " to support the education of underprivileged students in India.", "   -Students enrolled in the first "
            "year of post-graduation programme at any recognised college/university/institution "
            "(in the academic year 2022-23) in India can apply."],[3,"tb", "sci"]],

        [["L’Oréal India For Young Women in Science Scholarship","    -Objective to help financially deprived young "
            "women to pursue scientific studies","    -Scholarship worth INR 2.5lakhs", "    -Apply by 31st October"],
         [2, "sci","nb", "girl"]],

        [["Indian Oil Sports Scholarship", "    -Scholarship of Rs. 180000 to Rs. 360000 per annum", "    -The age of "
            "the applicant should be in between 13 to 19 years","    -Apply before 30th June"], [2, "sports", "tb"]],

        [["Shoolini University Admission Scholarship", "    -A financial aid worth Rs.10k-1lakh offered by Shoolini "
            "University to students taking admission in undergraduate and postgraduate programs in fields.",
            "    -Fields like Management, Applied "
            "Sciences, Basic Sciences, Arts, Hotel Management, etc.", "    -Apply by15-May-2023"], [3, "sci", "tb"]],

        [["Saryu Doshi Graduate Fellowships in Liberal Arts & Sciences", "    -UG students from recognized Indian "
            "Universities are eligible. Candidates must have secured admission in a foreign University in liberal "
            "arts course", "    -A merit based grant of INR 3 lakhs", "    -Apply by 30th May "], ["arts", "tb", 3]],

        [["Scheme for Scholarships to Young Artistes in Different Cultural Fields", "    -Candidates must have a degree"
           " in the chosen field along with proof of interest and Age should be between 18 and 25 years",
          "    -INR 60,000", "    -Visit website for Application dates(varied)"], [3, "tb", "arts"]]

    ]


dict_ = {"harshal.sharma@gmail.com": "123$Harsh", "anjalithakur@yahoo.com": "thankurAnjali@7543",
         "abha@gmail.com": "hello123"}

flag = 1
while flag == 1:
    print("\n1.Log Into an existing account\n2.SignUp to create a new account\n3.Exit ")

    choice = int(input("\nEnter your preferred choice(1/2/3) "))
    if choice == 1:
        user = input("\nPlease enter your email-id ")

        if user in dict_.keys():
            _pass = input("Please enter your password ")

            if dict_[user] == _pass:
                print("\nLogIn Successful ")
                flag = 0
            else:
                print("\nInvalid Password ")
        else:
            print("\nInvalid Username ")

    elif choice == 2:
        userName = input("\nPlease enter your email-id ")

        if userName in dict_.keys():
            print("\nUsername already exists. Please enter a valid username. ")
        else:
            pass_ = input("Please create a password ")
            dict_[userName] = pass_
            flag = 0
            print("\nAccount Created ")

    elif choice == 3:
        print("\nThankyou for Visiting ")
        break

    else:
        print("\nInvalid Choice ")

while flag == 0:

    print("\n\n\nWelcome! \nYou can browse scholarships by applying the following filters :-")
    print("1)No filters\n2)Age criteria\n3)Need based/Talent based\n4)Gender\n5)Field(Science/Arts/Sports)")
    print("6)View Wishlist\n7)Remove from wishlist\n8)End Program")
    print("Please Enter desired option")

    choice = int(input())

    if choice == 1:
        for i in range(20):
            enqueue(sclist[i][0])
        for i in range(20):
            print(str(i+1)+") ")
            for j in range(4):
                print(queue[i][j])
            print("\n")
        adw(queue)
        dequeueall()

    elif choice == 2:
        print("Select the required age group:")
        print("    1)Below 16 years\n    2)16 - 20 years\n    3)Above 20 years")
        choice2 = int(input("Enter your option i.e 1/2/3"))
        if choice2 == 1:
            for i in range(20):
                if filters(1, sclist[i][1]):
                    enqueue(sclist[i][0])
            count = 1
            for sc in queue:
                print( str(count)+ ") ")
                for i in range(4):
                    print(sc[i])
                count = count + 1

        elif choice2 == 2:
            for i in range(20):
                if filters(2, sclist[i][1]):
                    enqueue(sclist[i][0])
            count = 1
            for sc in queue:
                print(str(count) + ") ")
                for i in range(4):
                    print(sc[i])
                count = count + 1

        elif choice2 == 3:
            for i in range(20):
                if filters(3, sclist[i][1]):
                    enqueue(sclist[i][0])
            count = 1
            for sc in queue:
                print(str(count) + ") ")
                for i in range(4):
                    print(sc[i])
                count = count + 1
        adw(queue)
        if queue:
            dequeueall()

    elif choice == 3:
        print("Select the basis:\n     1)Need Based\n     2)Talent Based")
        basis = int(input("Enter option number"))
        if basis == 1:
            for i in range(20):
                if filters("nb", sclist[i][1]):
                    enqueue(sclist[i][0])
            count = 1
            for sc in queue:
                print(str(count) + ") ")
                for i in range(4):
                    print(sc[i])
                count = count + 1

        elif basis == 2:
            for i in range(20):
                if filters("tb", sclist[i][1]):
                    enqueue(sclist[i][0])
            count = 1
            for sc in queue:
                print(str(count) + ") ")
                for i in range(4):
                    print(sc[i])
                count = count + 1
        adw(queue)
        if queue:
            dequeueall()

    elif choice == 4:
        print("Select gender:\n    1)Girl\n    2)Boy")
        gen = int(input("Select your option"))
        if gen == 1:
            gen = "girl"
        elif gen == 2:
            gen = "boy"
        for i in range(20):
            if filters(gen, sclist[i][1]):
                enqueue(sclist[i][0])
        count = 1
        for sc in queue:
            print(str(count) + ") ")
            for i in range(4):
                print(sc[i])
            count = count + 1
        adw(queue)

        if queue:
            dequeueall()

    elif choice == 5:
        print("Select field: 1)Science and Technology 2)Arts 3)Sports")
        fld = int(input())
        if fld == 1:
            fld = "sci"

        if fld == 2:
            fld = "arts"

        if fld == 3:
            fld = "sports"
        for i in range(20):
            if filters(fld, sclist[i][1]):
                enqueue(sclist[i][0])
        count = 1
        for sc in queue:
            print(str(count) + ") ")
            for i in range(4):
                print(sc[i])
            count = count + 1
        adw(queue)
        if queue:
            dequeueall()

    elif choice == 6:
        ll.printll()

    elif choice == 7:
        ll.printll()
        ll.delnode()

    elif choice == 8:
        break

    else:
        print("Enter valid choice -> 1/2/3/4/5/6/7")


