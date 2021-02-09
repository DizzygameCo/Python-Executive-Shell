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
    ask = input("What would you like to do?")

    if ask == "/help":
        print("So you need help! Right back at you.")
        print(" ")
        print("/write = Create Text File")
        print(" ")
        print("/read = Reads Out A Text File")
        print(" ")
        print("/time = Gives You The Exact Time And Date")
        print(" ")
        print("/calculate = Calclates A Problem")
        print(" ")
        print("/esc = Stops The Program And Turns Into A Plain Python Shell")

    elif ask == "/calculate":
        print(" ")
        time_for_math = input("What is your equation?")
        print(" ")
        print(eval(time_for_math))
    elif ask == "/esc":
            print(" ")
            print("Shutting Down The Operating System")
            print(" ")
            print("Okay! The Running Window Has Stopped, Entering Shell.")
            runtel = 0
    elif ask == "/time":
        print(" ")
        print(time.asctime())

    elif ask == "/read":
        print(" ")
        reader = input("What is the name of the file?")
        print(" ")
        import pickle
        with open(reader, 'rb') as f:
            textsession = pickle.load(f)
            print(textsession)
    elif ask == "/write":
        print("")
        print("Creating A Text File...")
        print(" ")
        filename = input("What do you want the file to be called?")
        print(" ")
        textsession = input('What would you like to write?')
        print(' ')
        print(textsession)
        print(" ")
        save = input("Do you want to save this? Y for yes, N for no.")
        print('')
        if save == "N":
            print("Deleting...")
            textsession = 0
        elif save == "Y":
            import pickle
            with open(filename, 'wb') as f:
                pickle.dump([textsession], f)
            print("Saved At", time.asctime())
            textsession = 0
 


    
        
        
        
        
        
        
    
        
        

    


    
    
    
