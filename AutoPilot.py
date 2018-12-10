#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui
import time

class automateTask:

    def Instructions(self):
        #self.toggleScreenCast()
        try:
            print('Incase of Program Malfunction, Type "quit" in the input prompt or \nPress Ctrl-C to quit.')
            time.sleep(1)

            self.askOption()
        
        except KeyboardInterrupt:
            print('\nDone')

    def askOption(self):
        while True:
            try:    
                choice = input('Hi, what would you want me do (Reply with corresponding digits):\n1.Play a song\n2.Open a book\n3.Make a screencast\n4.Get Mouse Coordinates\n5.Scroll a page\n6.Deceive reCaptcha\n')
                if choice == '1':
                    self.playSong();
                elif choice == '2':
                    self.readPdf();
                elif choice == '3':
                    self.makeScreenCast();
                elif choice == '4':
                    self.getMouseCoordinates()
                elif choice == '5':
                    self.scrollPage()
                elif choice == '6':
                    self.deceivereCaptcha()
                elif choice == 'quit':
                    quit()
                else:
                    print("Invalid Response; Only reply with corresponding digits")
            except KeyboardInterrupt:
                print("\nDone")
    
    def playSong(self):
        try:
            pyautogui.press('winleft',)
            time.sleep(1) 
            pyautogui.click(659, 70)
            time.sleep(1)
            pyautogui.typewrite('rhythm',0.2)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(7)
            pyautogui.click(535, 356)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(29, 112)
            
            print('Song is now playing.....')
        
        except KeyboardInterrupt:
            print("\nDone")

    #new code
    def getMouseCoordinates(self):
        try:
            while True:
                # TODO: Get and print the mouse coordinates.
                x, y = pyautogui.position()
                positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
                print(positionStr, end='')
                print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            print("\nDone")
            self.Instructions()

    def makeScreenCast(self):
        try:
            
            time.sleep(2)
            
            pyautogui.press('winleft',)
            time.sleep(1) 
            pyautogui.click(659, 70)
            time.sleep(1)
            pyautogui.typewrite('LibreOffice writer',0.1)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.click(331, 297)
            time.sleep(1)

            self.toggleScreenCast()

            pyautogui.typewrite("Hey Guys,Told y'all about my new found love - PyAutoGUI module, for GUI Automation\n After going round it for some time, I made a little script that plays me Davido's Mind totally on its own\nBy the way even what you're reading now, inshort the whole video was made by the script also. Enjoy", .1)
            time.sleep(1)
            pyautogui.click(38,41)
            time.sleep(1)
            
            self.playSong()
            time.sleep(5)
            self.toggleScreenCast()
        
        except KeyboardInterrupt:
            self.toggleScreenCast()
            print('\nDone.')
        except pyautogui.FailSafeException:
            self.toggleScreenCast()
            print('\nDone.\n')
    
    def readPdf(self):
        try:
            time.sleep(3)
            pyautogui.press('winleft',)
            time.sleep(1) 
            pyautogui.click(659, 70)
            time.sleep(1)
            pyautogui.typewrite('Document Viewer', .2)
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.click(75, 199)
            time.sleep(1)
            pyautogui.press("enter")

            print('A PDF file has been opened for you......')
        except KeyboardInterrupt:
            print("\nDone")

    def toggleScreenCast(self):
            pyautogui.keyDown('ctrl') 
            pyautogui.keyDown('alt')
            pyautogui.keyDown('shift')
            pyautogui.keyDown('R')
            
            time.sleep(0.5)

            pyautogui.keyUp('R') 
            pyautogui.keyUp('shift')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('ctrl')

            time.sleep(1)
    
    def scrollPage(self):
        try:
            print("\nBefore using this feature, it's advised you minimize all unwanted windows,\nleaving only the one you want to scroll on. \nYou'd have 10 seconds to do this after providing all parameters.\n")
            time.sleep(1)
            orientation = input("Enter Desired Scroll length (Positive values for scrolling up, Negative for down)\n")
            orientation = int(orientation)
            delay = input("Enter delay(seconds) between scrolls\n"); delay = int(delay)
            self.countdown()
            time.sleep(1)
            pyautogui.click(698, 357)
            time.sleep(1)
            while True:
                pyautogui.scroll(orientation)
                time.sleep(delay)
        except KeyboardInterrupt:
            print("\nDone")
        except pyautogui.FailSafeException:
            print('\nDone.\n')
    
    def countdown(self):
        countdownTime = int(9)
        while countdownTime:
            mins, secs = divmod(countdownTime, 60)
            timeformat = '{:02d}:{:02d}'.format(mins,secs)
            print("You have " + timeformat + " left to focus on desired window", end='\r')
            time.sleep(1)
            countdownTime -= 1

    def deceivereCaptcha(self):
        x = input("Enter X Coordinate:\n");
        y = input("Enter Y Coordinate:\n");
        x = int(x);
        y = int(y);
        time.sleep(5) 
        pyautogui.click(x, y)
        time.sleep(6)
        pyautogui.press('winleft',)
        time.sleep(1)
        pyautogui.typewrite('LibreOffice writer',0.1)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.click(331, 297)
        time.sleep(1)
        pyautogui.typewrite("EBUKALOPER DO YOU BELIEVE ME NOW???? I DECEIVED reCaptcha LOL!", .1)
        time.sleep(1)
        #self.toggleScreenCast()
       
autopilot = automateTask()
autopilot.Instructions()