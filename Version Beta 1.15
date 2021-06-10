import time 
runtel = 1

def display_time():
    current_time = tm.strftime('%H:%M:%S %p')
    clock_label['text'] = current_time
    my_window.after(200,display_time)

print("Hello!")
print(" ")
print("Welcome to PythonOS, an open source operating system made in python. It's a command line, similar to older operating systems from a long time ago. I don't know why I made this, I guess I just had too much spare time on my hands.")
print(" ")
print("Type /help for some commands")

while runtel == 1:

    print(" ")
    ask = input("What would you like to do? \n")

    if ask == "/help":
        print("So you need help! Right back at you. \n")
        print("/write: Write to new text file \n")
        print("/read: Reads out saved text file \n")
        print('/del: Delete selcted text file \n')
        print("/time: Gives exact time and date \n")
        print("/calculate: Solves equations \n")
        print("/esc: Exits to shell \n")

    elif ask == "/calculate":
        print(" ")
        time_for_math = input("What is your equation? \n")
        print(eval(time_for_math))
    elif ask == "/esc":
            print(" ")
            print("Shutting Down Program... \n")
            print("Entering Shell. \n")
            runtel = 0
    elif ask == "/time":
        print(" ")
        print(time.asctime())

    elif ask == "/read":
        print(" ")
        reader = input("File Name: \n")
        import pickle
        with open(reader, 'rb') as f:
            textsession = pickle.load(f)
            print(textsession)
    elif ask == "/write":
        print("")
        print("Creating A Text File... \n")
        filename = input("What do you want the file to be called? \n")
        textsession = input('Enter text: \n')
        print(textsession)
        print(" ")
        save = input("Do you want to save this? Y for yes, N for no. \n")
        if save == "N":
            print("Deleting...")
            textsession = 0
        elif save == "Y":
            import pickle
            with open(filename, 'wb') as f:
                pickle.dump([textsession], f)
            print("Saved At", time.asctime())
            textsession = 0
    elif ask == "/del":
        import os
        print('')
        filenamequery = input("What is the filename? Please end the name in the .pickle file-extention. \n")
        if os.path.exists(filenamequery):
            
            os.remove(filenamequery)
            print("File Deleted")
        else:
            print("The file does not exist")
 


    
        
        
        
        
        
        
    
        
        

    


    
    
    
