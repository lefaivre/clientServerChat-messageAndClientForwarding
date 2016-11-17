import socket
import sys

#server address
server_address = "108.173.198.18"
#client address
client_address = ""
#server port
server_port = 2000
#client port
client_port = 2100

#create the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind the socket to the client address and port
client_socket.bind((client_address, client_port))

while 1:
    #get this client's ID
    source = raw_input("Please enter a 10 digit ID: ")
    if(len(source) != 10):
        print("Sorry, ID must be 10 digits. Please try again: ")
    else:
        break

#initialize the sequence number
sequence_number = 0

while 1:
    #increment the sequence number
    sequence_number += 1
    sequence_number_string = str(sequence_number)
    
    #create an empty message
    message = ""
    
    #program options:    
    option = input("Press 1 to send a message,\nPress 2 to receive messages,\nPress 3 to quit: ")
    
    #send a message to the other client
    if(option == 1):
        #create the message (based on the option given)
        #message format:       
        #seq. no
        message += sequence_number_string
        message += "/"      
        #type (send or get)
        message += "send"
        message += "/"      
        #source (ID for this client)
        message += source
        message += "/"      
        #destination (ID for the other client)
        message += raw_input("Please enter the destination client's 10 digit ID: ")
        message += "/"      
        #payload
        while 1:
            payload = raw_input("Please enter the message (max 160 characters): ")
            if(len(payload) > 160):
                print("Sorry, message must be <= 160 characters. Please try again: ")
            else:
                break
        message += payload
        print(message)
        break
    
    elif(option == 2):
        #create the message (based on the option given)
        #message format:
        #seq. no
        message += sequence_number_string
        message += "/"
        #type (send or get)
        message += "get"
        message += "/"
        #source (ID for this client)
        message += source
        message += "/"
        #remaining fields will be empty
        message += ""
        message += "/"
        message += ""
        print(message)
        break
    
    else:
        print("Goodbye.")
        #close the connection and the program
        client_socket.close()
        sys.exit(0)
    