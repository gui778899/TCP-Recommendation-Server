import socket
import random
# data_payload = 2048
port = 9879
FORMAT = 'utf-8'
DISCONNECT_request = "Disconnect"

#server which we are connecting
SERVER = socket.gethostbyname(socket.gethostname()) 
ADDR = (SERVER, port)

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Client.connect(ADDR)

#This function is for sending and receiving data from server.
def send_buy(msg, noOfBooks=1, address_user = None):
    #avoid errors form the server 
    if msg == "Get_OuTPut_From_Server":
        res_ser = Client.recv(2048).decode(FORMAT)
        if res_ser:
            check_book_ = res_ser.split(", ")
            for i in check_book_:
                if(i == "You are not allowed to Buy more than 8 Number of books... "):
                    print()
                    print(i)
                    return
            res_ser = res_ser.split('\n')

            len_res_ser = len(res_ser)
            if len_res_ser == 3:
                print()
                print(res_ser[len_res_ser-2])
                print()
            else:
                print()
                print(res_ser[len_res_ser-3],res_ser[len_res_ser-2])
                print()
        
        if(address_user == "Get Address From user"):
            order_number = random.randint(1, 1000000)
            print(f"Thanks for ordering.\nYour Order id is {order_number}. \nWe will Deliver these Books to your Respective Address...\n")
    #encode in byte format 
    message = msg.encode(FORMAT)
    Client.send(message)
    print()



def send(msg, noOfBooks=1, address_user = None):
    #if condition to avoid errors from the server 
    if msg == "Get_OuTPut_From_Server":
        #conditions if the data is transfered more than 2 times or less than 2 times between server and client  
        
        if(noOfBooks<=2):
            for i in range(0,noOfBooks):
                res_ser = Client.recv(2048).decode(FORMAT)
                if res_ser :
                    if(res_ser == "['Book is Not available which you want... ']"):
                        res_ser = res_ser.replace("[","")
                        res_ser = res_ser.replace("]","")
                        res_ser = res_ser.replace("'","")
                        print(res_ser)
                        print()
                    else:
                        try_ans = []
                        for x in res_ser.split(", "):
                            try_ans.append(x)
                        for y in try_ans:
                            y = y.replace("[", "")
                            y = y.replace("]", "")
                            y = y.replace("'", "")
                            y = y.replace(",", "")
                            print(y)
                        print()

        else:
            for i in range(0,2):
                res_ser = Client.recv(2048).decode(FORMAT)
                if res_ser :
                    print(res_ser)
                
            
    #encode in byte format
    message = msg.encode(FORMAT)
    Client.send(message)
    print()


#Check if user wants to buy or search and retrieve the input from the user 
cond = True
Check_lst_SB = ["Search", "Buy"]
NumberOfBooks = None
while cond:
    Opt_byclient = input("Hey Do you want to search book Or Buy a Book? \n For Searching book write \"Search\" \n For Searching book write \"Buy\" \n ")
    if Opt_byclient in Check_lst_SB:
        if Opt_byclient == Check_lst_SB[1]:
            NumberOfBooks = int(input(f"How many different books do you want to {Opt_byclient} = "))
        else:
            NumberOfBooks = int(input(f"How many books do you want to {Opt_byclient} = "))
        break
    else:
        print("There is some mistake in which you have written. Please write the exact same word... ")


#Correct spelling mistakes
SpellMis_Search_difi_easy = ["Eay", "Esy", "asy", "Eas", "easy"]
SpellMis_Search_difi_medi = ["Medim", "Medum", "Mdium", "Meium", "medium"]
SpellMis_Search_difi_hard = ["Hrd", "Had", "ard", "hard"]
orignal_Search_spell = ["Easy", "Hard", "Medium"]
orignal_area_spell = ["peakdistrict","lincoinshire", "york", "peakdistrict", "northwales", "warwickshire", "cheshire"]
#Checking user want to search or buy and taking inputs regarding that       
if Opt_byclient == Check_lst_SB[0]:
    #Dynamic lop to buy and search 
    for i in range (0, NumberOfBooks):
        Area =  input("Area Where Want to Walk = ") or "Client not write it."
        Min_length = (input("Minimum Length in Miles = ") or str(0))
        Max_length = (input("Maximum Length in Miles = ") or str(0))
        Level_dificulty = input("Level of Difficult = ")
        send(Opt_byclient)
        Area = Area.lower()
        if Area in orignal_area_spell:
            send(Area)
        else:
            Area = input("Please write correct area name : ")
            send(Area.lower())
        send(Min_length)
        send(Max_length)
        #conditions for some spelling mistakes 
        if Level_dificulty in orignal_Search_spell:
            send(Level_dificulty)
        else:
            if Level_dificulty in SpellMis_Search_difi_easy:
                correct_Word = input("Do you mean \'Easy\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Easy")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
                    
            elif Level_dificulty in SpellMis_Search_difi_medi:
                correct_Word = input("Do you mean \'Medium\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Medium")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
            elif Level_dificulty in SpellMis_Search_difi_hard:
                correct_Word = input("Do you mean \'Hard\'? write Yes/No or y/n for confirmation. ")
                if correct_Word == "Yes" or correct_Word == "y" or correct_Word == "Y":
                    send("Hard")
                else:
                    print("Please write spelling carefully. Make sure it's perfect. ")
                    Level_dificulty = input("Level of Difficult = ")
                    send(Level_dificulty)
    send("Get_OuTPut_From_Server", NumberOfBooks)

#Taking inputs for Buy 
if Opt_byclient == Check_lst_SB[1]:
    Customer_Name = input("Write Your Name : ")
    for i in range (0, NumberOfBooks):
        Book_Number = input("Book Number which you want to buy : ")
        Book_Quanity = input("Book Quantity which you want for above book : ")
        send_buy(Opt_byclient)
        send_buy(Customer_Name)
        send_buy(Book_Number)
        send_buy(Book_Quanity)
    Your_address = input("Please Write your Full Address for Delivery.")
    send_buy("Get_OuTPut_From_Server", NumberOfBooks, "Get Address From user")
    




DISCONNECT_request = DISCONNECT_request.encode(FORMAT)
Client.send(DISCONNECT_request)
