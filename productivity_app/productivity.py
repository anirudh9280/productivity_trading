import json 
import time
from datetime import datetime, timedelta
import random
from termcolor import cprint 

def load_tasks():
    with open("/Users/anirudhannabathula/Desktop/dev/productivity_app/tasks.json", "r") as f:
        tasks = json.load(f)
    return tasks
def get_tasks_schedule(tasks):
    tasks_start_time = datetime.now()
    schedule = []
    for task, minutes in tasks.items():
        end_time = tasks_start_time + timedelta(minutes=minutes)
        schedule.append((task, tasks_start_time, end_time))
        task_start_time = end_time
    return schedule

def main():
    tasks = load_tasks()
    schedule = get_tasks_schedule(tasks)
    current_index = 0
    while True:
        now = datetime.now()
        current_task, start_time, end_time = schedule[current_index]
        remaining_time = end_time - now
        remaining_minutes = int(remaining_time.total_seconds() // 60)
        print("")
        for index, (task, s_time, e_time) in enumerate(schedule):
            if index < current_index:
                # task is completed
                print(f"{task} done: {e_time.strftime('%H:%M')}")
            elif index == current_index:
                # current task 
                if remaining_minutes < 2:
                    cprint(f'{task} < 2m left', "white", "on_red", attrs=["blink"])
                elif remaining_minutes < 5:
                    cprint(f'{task} - {remaining_minutes} mins', "white", "on_red")
                else:
                    cprint(f'{task} - {remaining_minutes} mins', "white", "on_red")
            else:
                print(f'{task} @ {s_time.strftime("%H:%M")}')

        list_of_reminders = [
            "get your bread up lil bro", 
            "100% effort?"
        ]

        random_reminder = random.choice(list_of_reminders)
        print("✨" + random_reminder)
        if now >= end_time:
            current_index += 1
            if current_index >= len(schedule):
                cprint("all tasks are completed", "white", "on_green")
                break
        time.sleep(15)
main()


                    
                    



                

        
    

