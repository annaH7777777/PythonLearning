import random

def finish_message(is_win):
    message = "You won!" if is_win else "You lost!"
    print(message)

def main():
    roll_number = 0
    goal_number = 0
    while True:
        first_num = random.randint(1, 6)
        second_num = random.randint(1, 6)
        num_sum = first_num + second_num
        print(f'The sum of dice is {first_num} + {second_num} = {num_sum}')
        if roll_number == 0:
            if num_sum == 7 or num_sum == 11:
                finish_message(True)
                break
            elif num_sum == 2 or num_sum == 3 or num_sum == 12:
                finish_message(False)
                break
            else:
                goal_number = num_sum
                print(f'Now your goal number is {goal_number}')
        else:
            if num_sum == goal_number:
                finish_message(True)
                break
            elif num_sum == 7:
                finish_message(False)
                break
        roll_number += 1


if __name__ == "__main__":
    main()