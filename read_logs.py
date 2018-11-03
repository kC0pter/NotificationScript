import requests
from time import sleep

bot_id = "" #Your Telegram Bot id
chat_id = "" #Your Telegram account or group chat id
time_need = 960 #15 min
message_for_time = "Logs have not changed in the last " + str(time_need / 60) + " minutes"

last_line = ""
last_received_message = []
r = 0

filter_1 = "Game is closed or not responding for more than 2 minutes. Restarting D3..." #filter for checking
filter_2 = "Running Step : clearWhimsydale" #filter for checking
filter_3 = "Running Step : theVault" #filter for checking
message_filter_1 = "ROS Bot crash" #message to Telegram if found matches with filter_1
message_filter_2 = "Whimsydale" #message to Telegram if found matches with filter_2
message_filter_3 = "The Vault" #message to Telegram if found matches with filter_3
number_of_filters = 0
filters_accept = False

while filters_accept == False:
    try:
        number_of_filters = int(input("""Input number of filter settings:
All filters - 1
Only filter_1 - 2
filter_1 and filter_2 - 3
filter_1 and filter_3 - 4\n"""))
        if 0 < number_of_filters < 5:
            print("Filters accept")
            filters_accept = True
        else:
            print("Input number from list")
    except:
        print("Input number from list")
print("Start reading logs.txt")
line_repeat = []
line_repeat2 = []

def checking(Filter, message):
    global line_repeat
    if Filter in line[-i] and not any(c in line[-i] for c in line_repeat):
            get = requests.get("https://api.telegram.org/bot" + bot_id + "/sendMessage?chat_id=" + chat_id + "&text=" + message)
            line_repeat.append(line[-i])
            print(line[-i])
            
def receiveCommand():
    global line_repeat2
    
    get = requests.get("https://api.telegram.org/bot" + bot_id + "/getUpdates?chat_id=" + chat_id)
    print(get)

while True:
    i = 0
    
    try:
        f = open('logs.txt','r') #You need to bring this script to folder with logs.txt
        #f = open('//Computer
                                        #name/Users/Username/Documents/RoS-BoT/Logs/logs.txt','r') #This if you
                                        #want to launch anywhere
    except:
        print("Cannot access to file")
        sleep(20)
        continue
        
    line = f.readlines()
    f.close()

    while i < 20:
        i+=1
        if i == 1:
            if last_line == line[-i]:
                r +=1
            else:
                r = 0
            if r == time_need / 20:
                print(last_line)
                get = requests.get("https://api.telegram.org/bot" + bot_id + "/sendMessage?chat_id=" + chat_id + "&text=" + message_for_time)
            last_line = line[-i]
        if number_of_filters == 1:
            checking(filter_1, message_filter_1)
            checking(filter_2, message_filter_2)
            checking(filter_3, message_filter_3)
        if number_of_filters == 2:
            checking(filter_1, message_filter_1)
        if number_of_filters == 3:
            checking(filter_1, message_filter_1)
            checking(filter_2, message_filter_2)
        if number_of_filters == 4:
            checking(filter_1, message_filter_1)
            checking(filter_3, message_filter_3)
        
    sleep(20)