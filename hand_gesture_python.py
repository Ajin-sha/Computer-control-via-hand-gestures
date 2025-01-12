import serial  
import time   
import pyautogui  
from plyer import notification


ArduinoSerial = serial.Serial('COM3', 9600) 
time.sleep(2)  

current_mode = 1  

def show_temp_notification(mode):
    
    messages = {
        1: "Mode 1: You can do pause/play now!",
        2: "Mode 2: You can adjust volume now!",
        3: "Mode 3: You can scroll now!",
        4: "Mode 4: You can present slide now!",
        5: "Mode 5: You can close tab now!"
    }
    
    
    notification.notify(
        title=f"Switched to Mode {mode}",
        message=messages[mode],
        app_name="Gesture Control",
        timeout=2  
    )

def switch_mode():
    global current_mode
    current_mode = (current_mode % 5) + 1  
    show_temp_notification(current_mode)


while True:
    try:
        
        incoming = ArduinoSerial.readline().decode('utf-8').strip()
        print(f"Incoming: {incoming}")

       
        if "Mode Switch" in incoming:
            switch_mode()

        
        if current_mode == 1:
            if "Action 1" in incoming: 
                pyautogui.typewrite(['space'], interval=0.2)  
        elif current_mode == 2:
            if "Action 1" in incoming:  
                pyautogui.hotkey('volumedown')  
            elif "Action 2" in incoming: 
                pyautogui.hotkey('volumeup') 

        elif current_mode == 3:
            if "Action 1" in incoming:  
                pyautogui.scroll(50) 
            elif "Action 2" in incoming: 
                pyautogui.scroll(-50)  

        elif current_mode == 4:
            if "Action 1" in incoming:  
                pyautogui.press('right')  
            elif "Action 2" in incoming:  
                pyautogui.press('left')  

        elif current_mode == 5:
            if "Action 1" in incoming:  
                pyautogui.hotkey('alt', 'f4')  

        time.sleep(0.1)  

    except Exception as e:
        print(f"Error: {e}")
