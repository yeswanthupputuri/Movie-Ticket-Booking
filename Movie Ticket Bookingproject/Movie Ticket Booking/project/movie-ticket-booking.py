import mysql.connector
import getpass
from mysql.connector import Error

class bookTicket:
  print("Hi welcome to BookYourMovie.com ", "\n")
  print("**********************************************************************")

  @classmethod
  def insertScree_11(cls,r, c,name,gender,phoneNo,status):
          try:
              connection = mysql.connector.connect(host='localhost',
                                                   database='bookyourtickets',
                                                   user='root',
                                                   password='udaykiran',
                                                   port='3306')
              cursor = connection.cursor()
              mySql_insert_query = """INSERT INTO screen_11 (row_s11,Col,Name,Gender,PhoneNo,Status)
                                      VALUES (%s, %s, %s, %s, %s, %s) """

              recordTuple = (r, c, name, gender, phoneNo, status)
              cursor.execute(mySql_insert_query, recordTuple)
              connection.commit()
              print("Booked successfully ")

          except mysql.connector.Error as error:
              print("Failed to insert into MySQL table {}".format(error))

          finally:
              if (connection.is_connected()):
                  cursor.close()
                  connection.close()



  @classmethod
  def insertScree_12(cls,r, c,name,gender,phoneNo,status):
      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='bookyourtickets',
                                               user='root',
                                               password='udaykiran',
                                               port='3306')
          cursor = connection.cursor()
          mySql_insert_query = """INSERT INTO screen_12 (row_s12,Col,Name,Gender,PhoneNo,Status)
                                  VALUES (%s, %s, %s, %s, %s, %s) """

          recordTuple = (r, c,name,gender,phoneNo,status)
          cursor.execute(mySql_insert_query, recordTuple)
          connection.commit()
          print("Booked successfully ")

      except mysql.connector.Error as error:
          print("Failed to insert into MySQL table {}".format(error))

      finally:
          if (connection.is_connected()):
              cursor.close()
              connection.close()
  @classmethod
  def updateScreen1(cls):
      import mysql.connector
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='bookyourtickets',
                                               user='root',
                                               password='udaykiran',
                                               port='3306'
                                               )
          cursor = connection.cursor()

          sql_update_query = """Update statistics set  NoOfTickets = (select count(status) from screen_11),CurrentIncome=NoOfTickets * 10,Percentage=CurrentIncome / 500 * 100 where Screen = 'Screen1'"""
          cursor.execute(sql_update_query)
          connection.commit()
      except mysql.connector.Error as error:
          print("Failed to update table record: {}".format(error))
      finally:
          if (connection.is_connected()):
              connection.close()
      bookTicket.display()
  @classmethod
  def updateScreen2(cls):
      import mysql.connector
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='bookyourtickets',
                                               user='root',
                                               password='udaykiran',
                                               port='3306')
          cursor = connection.cursor()
          sql_update_query = """Update statistics set  NoOfTickets = (select count(status) from screen_12),CurrentIncome = NoOfTickets * 10,Percentage = CurrentIncome / 738 * 100 where Screen = 'Screen2'"""
          cursor.execute(sql_update_query)
          connection.commit()
      except mysql.connector.Error as error:
          print("Failed to update table record: {}".format(error))
      finally:
          if (connection.is_connected()):
              connection.close()
      bookTicket.display()
  @classmethod
  def screen1(cls,rows,cols):
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='bookyourtickets',
                                               user='root',
                                               password='udaykiran',
                                               port='3306')

          sql_select_Query = "select row_s11,Col from screen_11"
          cursor = connection.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          print("Cinema:\n")
          print("screen1:\n")
          for m in range(0, cols):
              if m == 0:
                  print(" ", end=" ")
              else:
                  print(m, end=" ")
          for i in range(0, rows):
              print()
              for j in range(0, cols):
                  if (i == 0 and j >= 0):
                      print(" ", end=' ')
                      break
                  if i > 0 and j == 0:
                      print(i, end=' ')
                  else:
                      if (i, j) in (records):

                          print('B', end=' ')
                      else:
                          print('S', end=" ")
          print("\n**********************************************************************\n")
      except Error as e:
          print("Error reading data from MySQL table", e)
      finally:
          if (connection.is_connected()):
              connection.close()
              cursor.close()
  @classmethod
  def screen2(cls,rows,cols):
      import mysql.connector
      from mysql.connector import Error

      try:
          connection = mysql.connector.connect(host='localhost',
                                               database='bookyourtickets',
                                               user='root',
                                               password='udaykiran',
                                               port='3306')

          sql_select_Query = "select row_s12,Col from screen_12"
          cursor = connection.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          print("Cinema:")
          print("screen2:\n")
          for m in range(0, cols):
              if m == 0:
                  print(" ", end=" ")
              else:
                  print(m, end=" ")
          for i in range(0, rows):
              print()
              for j in range(0, cols):
                  if (i == 0 and j >= 0):
                      print(" ", end=' ')
                      break
                  if i > 0 and j == 0:
                      print(i, end=' ')
                  else:
                      if (i, j) in (records):

                          print('B', end=' ')
                      else:
                          print('S', end=" ")
      except Error as e:
          print("Error reading data from MySQL table", e)
      finally:
          if (connection.is_connected()):
              connection.close()
              cursor.close()

  @classmethod
  def yourChoice(cls):
      print("1.  screen1 (less than 60 seats)\n")
      print("2. screen2 (More than 60 seats)\n")
  @classmethod
  def screenDisp(cls):
      select = int(input("Please select the screen\n"))
      if select == 1:
          bookTicket.screen1(8, 8)
          print()
          print("Want to Booked Ticket:\n")
          print("1. Yes")
          print("2. No")
          ch = int(input("select 1 or 2:\n"))
          if ch == 1:
              bookTicket.display()
          if ch == 2:
              bookTicket.display()
      if select == 2:
              bookTicket.screen2(10, 10)
              print()
              print("Want to Booked Ticket:\n")
              print("1. Yes")
              print("2. No")
              ch = int(input("select 1 or 2:\n"))
              if ch == 1:
                 bookTicket.display()
              if ch == 2:
                  bookTicket.display()
  @classmethod
  def statisticsDetail1(cls):
          try:
              mySQLConnection  = mysql.connector.connect(host='localhost',
                                                   database='bookyourtickets',
                                                   user='root',
                                                   password='udaykiran',
                                                   port='3306')

              cursor = mySQLConnection.cursor(buffered=True)

              sql_select_query = """select * from statistics """
              cursor.execute(sql_select_query)
              record = cursor.fetchall()

              for r in record:
                  print("Screen = ", r[1], )
                  print("NoOfTickets = ", r[2])
                  print("Percentage = ", r[3])
                  print("CurrentIncome = " ,r[4])
                  print("TotalIncome = ", r[5])
                  print()
              print("\n**********************************************************************\n")
          except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
              print("Something wrong")
          finally:
              if (mySQLConnection.is_connected()):
                  cursor.close()
                  mySQLConnection.close()
          bookTicket.display()
  @classmethod
  def getUserDetail1(cls,row,col):
      try:
          mySQLConnection = mysql.connector.connect(host='localhost',
                                                   database='bookyourtickets',
                                                   user='root',
                                                   password='udaykiran',
                                                   port='3306')

          cursor = mySQLConnection.cursor(buffered=True)
          sql_select_query = """select * from screen_11 where row_s11 = %s and col = %s"""
          cursor.execute(sql_select_query, (row,col))
          record = cursor.fetchall()
          print("audience details\n")
          for r in record:
              print("Name = ", r[2], )
              print("Gender = ", r[3])
              print("PhoneNo = ", r[4])
              print("Price = " ,"$10")
          print("\n**********************************************************************\n")
      except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
          print("Something wrong")
      finally:
          if (mySQLConnection.is_connected()):
              cursor.close()
              mySQLConnection.close()
  @classmethod
  def getUserDetail2(cls,row,col):
      try:
          mySQLConnection = mysql.connector.connect(host='localhost',
                                                   database='bookyourtickets',
                                                   user='root',
                                                   password='udaykiran',
                                                   port='3306')
          cursor = mySQLConnection.cursor(buffered=True)
          sql_select_query = """select * from screen_12 where row_s12 = %s and col = %s"""
          cursor.execute(sql_select_query, (row,col))
          record = cursor.fetchall()
          print("audience details:\n")
          for r in record:
              if r[0] <= 4:
                      print("Name = ", r[2])
                      print("Gender = ", r[3])
                      print("PhoneNo = ", r[4])
                      print("Price = " ,"$8")
              else:
                      print("Name = ", r[2], )
                      print("Gender = ", r[3])
                      print("PhoneNo = ", r[4])
                      print("Price = ", "$10")
          print("\n**********************************************************************\n")
      except mysql.connector.Error as error:
          # print("Failed to get record from MySQL table: {}".format(error))
          print("Something wrong")

      finally:
          if (mySQLConnection.is_connected()):
              cursor.close()
              mySQLConnection.close()
  @classmethod
  def display(cls):
    print("Please Enter your choice:")
    print("**********************************************************************")
    print("0. Exit")
    print("1. Show the Seats.")
    print("2. Buy the ticket.")
    print("3. Statitics.")
    print("4. Show booked ticket's user Info.")
    choice = int(input("Enter your choice:\n"))
    if choice == 0:
      exit()
    if choice == 1:
      bookTicket.yourChoice()
      bookTicket.screenDisp()

    if choice == 2:
      print("Book my ticket in:\n")
      print("1. screen1")
      print("2. Screen2")
      screenChoice = int(input("Select 1 or 2:\n"))
      if screenChoice == 1:
        r = int(input("Select the row\n"))
        range_r1 = range(1,8,1)
        if r not in range_r1:
            print("!! enter  between 1 and 7 !!\n")
            r = int(input("Select the row\n"))
        c = int(input("select the col\n"))
        range_c1 = range(1,8,1)
        if c not in range_c1:
            print("enter between 1 and 7\n")
            c = int(input("select the col\n"))
        name = input("enter your name\n")
        gender = input("enter the gender\n")
        phoneNo = input("Enter the mbl no\n")
        if (len(phoneNo) != 10):
            print("phone number must be of length 10 \n")
            print("please enter the number again\n")
            phoneNo = input("Enter the mbl no\n")
        bookTicket.insertScree_11(r, c, name, gender, phoneNo, "Booked")
        bookTicket.updateScreen1()
      if screenChoice == 2:
        r = int(input("Select the row\n"))
        range_r2 = range(1, 10, 1)
        if r not in range_r2:
            print("enter  between 1 and 9\n")
            r = int(input("Select the row\n"))
        c = int(input("select the col\n"))
        range_c2 = range(1, 10, 1)
        if c not in range_c2:
            print("enter between 1 and 9\n")
            c = int(input("select the col\n"))
        name = input("enter your name\n")
        gender = input("enter the gender\n")
        phoneNo = input("Enter the mbl no\n")
        if (len(phoneNo) != 10):
            print("phone number must be of length 10 \n")
            print("please enter the number again\n")
            phoneNo = input("Enter the mbl no\n")
        bookTicket.insertScree_12(r, c, name, gender, phoneNo, "Booked")
        bookTicket.updateScreen2()
    if choice == 4:
        password = input("Enter admin password:\n")
        if password == "udaykiran":
            print("1. Show data from screen1:\n")
            print("2. Show data from screen2:\n")
            datachoice = int(input("select1 or 2:\n"))
            if datachoice == 1:
                user1Row = int(input("Enter User's Row:\n"))
                range_r1 = range(1, 8, 1)
                if user1Row not in range_r1:
                    print("enter user's row between 1 and 7\n")
                    user1Row = int(input("Enter User's Row:\n"))
                user1Col = int(input("Enter User's Col:\n"))
                range_c1 = range(1, 8, 1)
                if user1Col not in range_c1:
                    print("enter user's column between 1 and 7\n")
                    user1Col = int(input("Enter User's Col:\n"))
                bookTicket.getUserDetail1(user1Row, user1Col)
            if datachoice == 2:
                user2Row = int(input("Enter User's Row:\n"))
                range_r2 = range(1, 10, 1)
                if user2Row not in range_r2:
                    print("enter user's row between 1 and 9\n")
                    user2Row = int(input("Enter User's Row:\n"))
                user2Col = int(input("Enter User's Col:\n"))
                range_c2 = range(1, 10, 1)
                if user2Col not in range_c2:
                    print("enter user's column between 1 and 9\n")
                    user2Col = int(input("Enter User's Col:\n"))
                bookTicket.getUserDetail2(user2Row, user2Col)
            else:
                print("Invalid password.\n")
                return

    if choice == 3:
        password = input("Enter admin password:\n")
        if password == "udaykiran":
            bookTicket.statisticsDetail1()
        else:
            print("Invalid password.\n")
            return


disp = bookTicket()
disp.display()