import webbrowser, sys, pyperclip

#Check if the address is provided as a command line argument or stored on user's clipboard
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #Combines the full address into a string separated by spaces

else:
    address = pyperclip.paste() #Pastes the copied address into the variable

webbrowser.open('www.google.com/maps/place/' + address)