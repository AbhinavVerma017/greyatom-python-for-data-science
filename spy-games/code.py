# --------------
#Code starts here

#Function to re
def read_file(path):
    file=open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence
sample_message=read_file(file_path)

file_path_1
file_path_2

message_1=read_file(file_path_1)
message_2=read_file(file_path_2)
print(message_1)
print(message_2)

def fuse_msg(message_a,message_b):
    quotient=(int(message_b)//int(message_a))
    return str(quotient)

secret_msg_1=fuse_msg(message_1,message_2)
print(secret_msg_1)
file_path_3

message_3=read_file(file_path_3)
print(message_3)

def substitute_msg(message_c):
    if(message_c=='Red'):
        sub='Army General'
    if(message_c=='Green'):
        sub='Data Scientist'
    if(message_c=='Blue'):
        sub='Marine Biologist'
    return sub

secret_msg_2=substitute_msg(message_3)
print(secret_msg_2)

file_path_4
file_path_5

message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list=message_d.split()
    b_list=message_e.split()
    c_list=[i for i in a_list if i not in b_list]
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3=compare_msg(message_4,message_5)
print(secret_msg_3)
file_path_6

message_6=read_file(file_path_6)
print(message_6)

def extract_mg(message_f):
    a_list=message_f.split()
    even_words=lambda x:bool(len(x)%2==0)
    b_list=filter(even_words,a_list)
    final_msg=" ".join(b_list)
    return final_msg

secret_msg_4=extract_mg(message_6)
print(secret_msg_4)
messages_parts=[secret_msg_3,secret_msg_1,secret_msg_4,secret_msg_2]
secret_msg=" ".join(messages_parts)

def write_file(secret_msg):
    file=open(path,'a+')
    file.write(secret_msg)
    file.close()

final_path=user_data_dir + '/secret_message.txt'

print(secret_msg)







    #Opening of the file located in the path in 'read' mode
    
    #Reading of the first line of the file and storing it in a variable
    
    #Closing of the file
    
    #Returning the first line of the file
    
    

#Calling the function to read f
    
    
    #Integer division of two numbers
    
    #Returning the quotient in string format
    
#Calling the function to read file  

#Calling the function to read file


#Calling the function 'fuse_msg'


#Printing the secret message 



#Function to substitute the message
    
    #If-else to compare the contents of the file
    
    
    #Returning the substitute of the message
    
    

#Calling the function to read file


#Calling the function 'substitute_msg'


#Printing the secret message



#Function to compare message

    
    #Splitting the message into a list
    
    
    #Splitting the message into a list
    
    
    #Comparing the elements from both the lists
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    

#Calling the function to read file


#Calling the function to read file


#Calling the function 'compare messages'


#Printing the secret message


#Function to filter message

    
    #Splitting the message into a list

    
    #Creating the lambda function to identify even length words
    
    
    #Splitting the message into a list
    
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    
    
#Calling the function to read file


#Calling the function 'filter_msg'


#Printing the secret message


#Secret message parts in the correct order



