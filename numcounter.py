#imports
import time

#values
value = 0
max_num = 20
speed_output = 0.5

#def value + 1
def numcounter():
    global value
    if value > max_num:
        print (f"value > {max_num}")
    else:
        value = value + 1
        time.sleep(speed_output)
        print (f"value: {value}")
        numcounter()

numcounter()
