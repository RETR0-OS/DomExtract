import imaplib, email
from email.parser import HeaderParser
import socket

##Define functions
def search(key, value, con):
    bolean=True
    while bolean==True:
      try:
          if key is not None:
              result, data = con.search(None, key, value)
              return data
              bolean=False
          elif key is None:
              result, data = con.search(None, value)
              return data
              bolean=False
      except socket.gaierror:
          print("Could not connect to host. Are you connected to the internet?")
          print("Please reconnect to the internet and try again.")
      except imaplib.IMAP4.error as error:
          if "SEARCH command error" in repr(error):
              print("Invalid search parameter! Please ensure you enter a valid search parameter!")
      except KeyboardInterrupt:
          print("Ctrl+C recived!")
          print("Terminating further operations!")
          print("Goodbye!")
          exit()

      except exception as error:
          print("The program encountered an unidentified error. Please contact the developers adn provide the following error: \n")
          print(repr(error))
def get_emails(result_bytes, connection_obj):
    msgs = []
    for num in result_bytes[0].split():
        type, data = connection_obj.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs
def get_filters():
    bolean=True
    while bolean==True:
      try:
          print("Choose a label to filter:")
          print(" 1) All \n 2) Inbox \n 3) Important \n 4) Spam")
          choice = int(input("Enter choice (1/2/3/4)>> "))
          if choice == 1:
              return '"[Gmail]/All Mail"'
              bolean=False
          elif choice == 2:
              return "INBOX"
              bolean=False
          elif choice == 3:
              return "[Gmail]/Important"
              bolean=False
          elif choice == 4:
              return "[Gmail]/Spam"
              bolean=False
          else:
              print("Invalid Choice!")
      except KeyboardInterrupt:
          print("Ctrl+C recived!")
          print("Terminating further operations!")
          print("Goodbye!")
          exit()
      except ValueError:
          print("Invalid choice! Please ensure you enter a valid integer choice!")
def streamline_messages():
    bolean=True
    while bolean==True:
      try:
          print("Enter the basis on which you wish to filter the messages whose domain name and sender you wish to find:")
          print(" 1) Subject \n 2) Sender's email address \n 3) Date")
          choice = int(input("Enter choice (1/2/3)>> "))
          if choice == 1:
              s = input("Enter subject to search by: ")
              return "SUBJECT", s
              bolean=False
          elif choice == 2:
              s = input("Enter sender's mail to search by: ")
              return "FROM", s
              bolean=False
          elif choice == 3:
              print("Select the option to search for: ")
              print(" 1) Before \n 2) Since \n 3) Before and since")
              choice2 =  int(input("Enter the required option (1/2)>> "))
              if choice2 == 1:
                  d = input("Enter the date to search by (Format: (dd-<first three letters of month>-yyyy))")
                  if validate_dates(d) == True:
                      return None, f"(BEFORE \"{d}\")"
                      bolean=False
                  else:
                      print("\nInvlid date format! Please ensure you enter a valid date format!\n")
              elif choice2 == 2:
                  d = input("Enter the date to search by (Format: (dd-<first three letters of month>-yyyy))")
                  if validate_dates(d) == True:
                      return None, f"(SINCE \"{d}\")"
                      bolean=False
                  else:
                      print("\nInvlid date format! Please ensure you enter a valid date format!\n")
              elif choice2 == 3:
                  s = input("Enter date to search since ((Format: (dd-<first three letters of month>-yyyy)): ")
                  b = input("Enter date to search before ((Format: (dd-<first three letters of month>-yyyy)): ")
                  if validate_dates(s) == True and validate_dates(b) == True:
                      return None, f"(Since \"{s}\" BEFORE \"{b}\")"
                      bolean=False
                  else:
                      print("\nInvlid date format! Please ensure you enter a valid date format!\n")
              else:
                  print("Invalid choice!")
          else:
              print("Invalid choice!")
      except ValueError:
          print("Invalid choice! Please ensure you enter a valid integer choice!")
      except KeyboardInterrupt:
          print("\nCtrl+C recived!")
          print("Terminating further operations!")
          print("Goodbye!")
          exit()
def validate_dates(date):
    d = date.split("-")
    month_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    if int(d[0])<=0 or int(d[0])>31:
        return False
    if d[1].title() not in month_list:
        return False
    if len(d[2]) != 4:
        return False
    return True

##Main
def main():
    bolean=True
    while bolean==True:
      try:
          user = input("Enter your Gmail address>> ")
          password = input("Enter app password to the above email address>> ")
          imap_url = "imap.gmail.com"
          con = imaplib.IMAP4_SSL(imap_url)
          con.login(user,password)
          filter = get_filters()
          con.select(filter)
          print("Selected")
          k, v = streamline_messages()
          msgs = get_emails(search(k, v, con), con)
          bolean=False
          for m in msgs:
              out= email.message_from_bytes(m[0][1])["FROM"]
              l = out.split("<")
              print()
              print(f"Sender's username: {l[0].strip()}")
              print(f"Sender\'s domain: {l[1].split('@')[1].strip('>')}")
      except socket.gaierror:
          print("Could not connect to host. Are you connected to the internet?")
          print("Please reconnect to the internet and try again.")
          exit()
      except KeyboardInterrupt:
          print("Ctrl+C recived!")
          print("Terminating further operations!")
          print("Goodbye!")
          exit()
      except imaplib.IMAP4.error as error:
          if "Invalid credentials" in repr(error):
              print("your username or password is incorrect! Please note  that the username and password are case sensetive!")
              print("Please try again!")
          else:
              print("The program exited due to an unidentified error. Please contact the developers and provide them with the following error message: \n")
              print(error)
              exit()

##Run main
if __name__=="__main__":
    main()
