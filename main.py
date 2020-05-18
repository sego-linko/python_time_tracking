from datetime import datetime
import csv
from datetime import timedelta
def main():


    print("\nHi Nana, Hope you are great."
          "Kindly let me know what you need today.\n")

    print("\nKindly choose a number:"
          "\n 1. Start timer"
          "\n 2. Check wages for current task"
          "\n 3. Exit program")
    choice = int(input())

    if choice == 1:
        start_time = datetime.now()
        print(start_time.strftime("\nStarting time is : %X"))
        print(start_time.strftime("\nTime : %H:%M"))
        print("Kindly enter  a number to stop the timer")
        stop = int(input())
        end_time = datetime.now()
        print(end_time.strftime("\nEnding time is : %X"))
        print(end_time.strftime("\nTime : %H:%M)"))
        # time difference calculation
        t = (end_time - start_time)
        secs = t.seconds
        minutes = ((secs/60)%60)/60.0
        hours = secs/3600
        total_hours = round(hours + minutes, 2)
        # wage calculation (difference *5, result in $)
        wage = total_hours*5
        # add append to file
        with open('wages.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['Start date', 'Start time', 'End date', 'End time ', 'Total hour ', 'Pay'])
            newFileWriter.writerow([start_time.strftime("%x"), start_time.strftime("%H:%M%p"), end_time.strftime("%x"), end_time.strftime("%H:%M%p"), total_hours, f"$ {wage}"])
        print("This work session was successfully added\n\n")
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        main()
    elif choice == 2:
        print("\nKindly check your file named 'wages.csv' ")
        main()
    elif choice == 3:
        print("\nThanks for using this program. See you soon.")
        exit()
    else:
        print('\nSorry, you entered and invalid choice. Kindly try again.')
        main()

if __name__ == "__main__":
        main()

