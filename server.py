import socket 
import threading
# from . import dbcon as db
import mysql.connector
#Connecting to DataBase
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "gui12345",
    database="SearchTabletest",
)
mycursor = db.cursor(buffered=True)
cur_for_check_book  = db.cursor(buffered=True)
port = 9879
FORMAT = 'utf-8'
DISCONNECT_request = "Disconnect"
#Selects automatically the ipv4 address of the computer 
host = socket.gethostbyname(socket.gethostname())    

req_binding = (host, port) # used to bind with the server in the future

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Bind the socket to the port
sock.bind(req_binding)


#Function when the client buys from the server 
def check_buy(ls_buy_req, user_addr):
    #Making empty list to save answer in future
    ans_buy = ""
    #Making variable for back_order
    back_order = None
    #Filtering userdata from list to add respective variable.
    CustomerName = ls_buy_req[1]
    BookNum = int(ls_buy_req[2])
    BookQuantity = int(ls_buy_req[3])
    # print(CustomerName, BookNum, BookQuantity)
    Buying_book = BookQuantity
    #Adding username to anser
    ans_buy = ans_buy + CustomerName + ", "
    mycursor.execute("SELECT * FROM buy WHERE Book_Number=%s", (BookNum,))
    #getting data from User table.
    cur_for_check_book.execute("SELECT * FROM Users")
    mycur_book_res = cur_for_check_book.fetchall()
    user_books_indb = 0
    check_getin_db = False
    Spent_money_buy = 0
    back_order = 0
    Current_run_cost = 0
    #searching in database
    for i in mycur_book_res:
        #Cheking if Customer Name is exist in databe or not. If exists get the required data
        if(i[0] == CustomerName) :
            user_books_indb = i[2]
            Spent_money_buy = i[3]
            back_order = i[4]
            Current_run_cost = i[5]
            check_getin_db = True
    #checking condition if customer name exist if not then adding that data to Users Table.
    if check_getin_db:
        BookQuantity += user_books_indb
        #Updating data in users table.
        cur_for_check_book.execute("UPDATE Users SET books_buy=%s WHERE UserName= %s", (BookQuantity, CustomerName, ))
        db.commit()
    else:
        # print("Inserting... ")
        #insert Data to Users table.
        cur_for_check_book.execute("INSERT INTO Users (UserName, portofuser, books_buy, Total_Cost, Back_order, Totalprice) VALUES (%s, %s, %s, %s, %s, %s)",(CustomerName,user_addr[1], BookQuantity, Spent_money_buy, back_order, Current_run_cost,) )
        db.commit()
        # print("Data added to users")

    #condition to check if the user has bought more than 8 books or not 
    if BookQuantity >8:
        # print("You are in 8")
        ans_buy += "You are not allowed to Buy more than 8 Number of books... "
        
    else:
        #running a loop for all required data.
        for x in mycursor:
            #checking required book quantity is exist in database or not.
            if Buying_book <= x[3]:
                #if the user buys the book how much is left 
                Left_books = x[3] - Buying_book
                #Taking single book price from database
                Single_book_price = x[2]
                
                #calculates the total price 
                Total_price = Buying_book*Single_book_price
                Spent_money_buy += Total_price
                #updates the database
                Current_run_cost += Total_price
                cur_for_check_book.execute("UPDATE Users SET Total_Cost=%s WHERE UserName= %s",(Spent_money_buy, CustomerName, ))
                db.commit()
                #Checking the cost and set Discount
                if(Current_run_cost>= 75):
                    # Apply 10% discount to the order if above 75 
                    if Current_run_cost==0:
                        Total_price = Total_price*0.9
                    else:
                        Total_price = Current_run_cost*0.9
                    ans_buy += "Discount of 10% was applied."
                else:
                    Total_price = Current_run_cost
                #Add total price to the output to show the client 
                ans_buy += " Total Cost of Books " + str(round(Total_price,2)) +". \n"
                cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(Current_run_cost, CustomerName, ))
                db.commit()
                
            else:
                #Taking Back_order
                back_order += Buying_book - x[3]
                available_books = x[3]
                #Taking single book price from database
                Single_book_price = x[2]
                #calculating Total Price
                #updating total price
                Total_price = Buying_book*Single_book_price
                Current_run_cost += Total_price
                #getting total money spend by user.
                Spent_money_buy += Total_price
                #Updating Total money spend by user to Users table.
                cur_for_check_book.execute("UPDATE Users SET Total_Cost=%s WHERE UserName= %s",(Spent_money_buy, CustomerName, ))
                db.commit()
                #Updating back order of user to Users Table.
                cur_for_check_book.execute("UPDATE Users SET Back_order=%s WHERE UserName= %s",(back_order, CustomerName, ))
                db.commit()
                Left_books = 0
                #Checking the cost and set Discount
                if(Current_run_cost>= 75):
                    #Discount of 10% if above 75%
                    #adding discount to last price
                    if Current_run_cost==0:
                        Total_price = Total_price*0.9
                    else:
                        Total_price = Current_run_cost*0.9
                    # Total_price = Spent_money_buy*0.9

                    ans_buy += "Discount of 10% was applied."
                else:
                    Total_price = Current_run_cost
                #Creating Required Answer
                ans_buy += " Total Cost of Books " + str(round(Total_price,2)) +". "
                cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(Current_run_cost, CustomerName, ))
                db.commit()
                
        #Updates the database
        mycursor.execute("UPDATE buy SET Book_Quantity=%s WHERE Book_Number= %s", (Left_books,BookNum,))
        db.commit()

        #Checks if there is anything in back order or not 
        if back_order!=0:
            ans_buy += " Books in back order = "+str(back_order) +". \n"

    return ans_buy


#Function for searching data in database and return require output
def check_Search(ls_search_req):
    #Declare Variable to not write same thing multiple time in future.
    Book_is_not = "Book is Not available which you want... "
    ans_sear = []
    #Filtering userdata from list to add respective variable.
    Area = ls_search_req[1] 
    Min_len = float(ls_search_req[2])
    Max_len = float(ls_search_req[3])
    LevelOfDifficulty = ls_search_req[4]
    if Area == "Client not write it.":
        #checking if user werite AREA NAME OR NOT
        ans_sear.clear()
        ans_sear.append("Invalid Area Name Where Want to Walk.")
        return ans_sear
    # print(Area, Min_len, Max_len, LevelOfDifficulty)
    mycursor.execute("SELECT * FROM search WHERE Area= %s", (Area,))
    
    # print("what happended")
    #Get data using Querry now we are filterting that data one-by-one and use it as we require.
    for x in mycursor:
        # print("In loop")
        if(x[4]>= Min_len and x[4]<= Max_len):
            if(x[5] == LevelOfDifficulty):
                ans_sear.clear()  #Before Adding data clearing old data if list have.
                ans_sear.append(x[2])  # Appending data into List
                ans_sear.append(x[3])  # Appending data into List
                ans_sear.append(str(x[6]))  # Appending data into List
                print("[Data Passed to user...]")
                return ans_sear
            else:
                #cheking if anser "Book is Not available which you want... " is already added into ans_sear or not if not added then we are adding it.
                if Book_is_not in ans_sear:
                    continue
                ans_sear.append(Book_is_not) # Appending data into List
        else:
            #cheking if anser "Book is Not available which you want... " is already added into ans_sear or not if not added then we are adding it.
            if Book_is_not in ans_sear:
                    continue
            ans_sear.append(Book_is_not)# Appending data into List
    #returing required answer        
    return ans_sear


#Below function is for handle the connection between the client and server
#conn = connection with client,  addr = address  
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")
    #Create below boolean variable for run while loop and whenever time comes we can break the loop by changing the below variable value. 
    connected = True
    #Count variable to count how many times the loop runs 
    count = 0
    #Creation of empty lists to then do future operations(Buy and Search)
    temp_ls = []
    ans_sear = []
    ans_buy = []
    while connected:
        #Receiving data from client.
        msg = conn.recv(2048).decode(FORMAT)
        #if condition when client connects first time 
        if msg:
            count += 1
            #Condition to close from the server 
            if msg == "Get_OuTPut_From_Server":
                print("Got Connection closing")
                msg = DISCONNECT_request
            if msg == DISCONNECT_request:
                connected = False
                
            #Appending data into the list
            temp_ls.append(msg)
            #After getting all the parameters defined by the user count reaches 4, performs Buy
            if count == 4:
                #Here we are comparing the first value and finding which operation user wants
                if temp_ls[0] == "Buy":
                    ans_buy = check_buy(temp_ls, addr)
                    if ans_buy:
                        #loop to check if the user can process with the buy or already reached the limit of books
                        for x in ans_buy:
                            if x == "You are not allowed to Buy more than 8 Number of books... ":
                                ans_buy.clear()
                                ans_buy.append(x)
                        #sending required data to the client
                        conn.send(str(ans_buy).encode(FORMAT))
                        ans_buy= "" #Clearing a List
                        #reseting the count 
                        count = 0
                

            ##After getting all the parameters defined by the user count reaches 5, performs Search     
            if count == 5:
                if temp_ls[0] == "Search":
                    ans_sear = check_Search(temp_ls)
                    temp_ls.clear()
                    #checking if anser is empty or not
                    if ans_sear:
                        #checking answer length for perform some operations
                        if(len(ans_sear)>1):
                            #getting required data in required variable from list
                            Recommanded_book = "The Reccomended Book is : " + ans_sear[0]
                            Walk_name_out = "The Walk name is : "+ ans_sear[1]
                            Pages_book = "The page is : "+ ans_sear[2]
                            ans_sear.clear()
                            ans_sear.append(Recommanded_book)
                            ans_sear.append(Walk_name_out)
                            ans_sear.append(Pages_book)
                            conn.send(str(ans_sear).encode(FORMAT)) #Sending data to client
                            ans_sear.clear()  #Clearing a list
                        else:
                            conn.send(str(ans_sear).encode(FORMAT)) #Sending data to client.
                            ans_sear.clear()  #Clearing a list
                        count = 0

    CustomerName = temp_ls[1]
    cur_for_check_book.execute("UPDATE Users SET Totalprice=%s WHERE UserName= %s",(0, CustomerName, ))    #Removing Total session prices from database. So when user login again it's can get new.
    cur_for_check_book.execute("UPDATE Users SET Back_order=%s WHERE UserName= %s",(0, CustomerName, ))
    db.commit()         #Removing back_order from older database
    temp_ls.clear() #Clearing list
    print("You are Closing the client...")
    conn.close()
    print("Connection is closed...")
        

def start():
    sock.listen()
    print(f"[LISTENING] Server is listening on {host}\n")
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}\n")


print("[STARTING] server is starting...")
start()
