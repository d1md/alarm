from datetime import *
from playsound import playsound
hour = int(input("Give me the hour"))
minute = int(input("Give me the minute"))
second = int(input("Give me the seconds"))
day = input("Pm or am")
running = True

if day == "pm":
    hour += 12

while running:
    if datetime.now().hour == hour and datetime.now().minute == minute and datetime.now().second == second:
        running = False
playsound('D:\\Programare\\Python\\repositories\\alarm\\alarm\\alarm\\alarm-sound.mp3')

