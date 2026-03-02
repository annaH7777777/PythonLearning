import time

def main():
    second_delay = 1
    time_str = input('Insert time to count down (h:m:s)')
    parts = time_str.split(':')
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        print("Invalid time format, expected h:m:s")
        return
    hour = int(parts[0])
    minute = int(parts[1])
    second = int(parts[2])
    if hour < 0  or minute < 0 or second < 0 or minute > 59 or second > 59:
        print("Invalid time format, expected h:m:s")
        return
    print(f"time is  {hour}:{minute}:{second}")
    while True:
        time.sleep(second_delay)
        second -= second_delay
        if second < 0:
            second = 59
            minute -= 1
        if minute < 0:
            minute = 59
            hour -= 1
        if hour < 0:
            print("Time's up!")
            break
        hour_first_symbol = '0' if hour < 10 else ''
        minute_first_symbol = '0' if minute < 10 else ''
        second_first_symbol = '0' if second < 10 else ''
        print(f"{hour_first_symbol}{hour}:{minute_first_symbol}{minute}:{second_first_symbol}{second}")

if __name__ == "__main__":
   main()