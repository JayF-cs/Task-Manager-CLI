from Task import Task
from Taskmanager import TaskManager
import sys

def main():

    manager = TaskManager()

    while True:
        print('Task Manager')
        print(20*'-')
        print('What would you like to do')
        print('1. Add a task')
        print('2. Remove a task')
        print('3. Mark task a complete')
        print('4. View task')
        print('5. View complete task')
        print('6. Quit')


        while True:
            try:
                while True:
                    user_choice = int(input('Choice > ').strip())
                    if user_choice not in [1,2,3,4,5,6]:
                        print('Please Pick One of the Availavle Options')
                    else:
                        break
                break
            except ValueError:
                print('Please Pick One of the Available Options')

        match user_choice:
            case 1:
                while True:
                    task_name = input('Task Name > ')
                    description = input('Descrition (Optional) > ')
                    due_date = input('Due Date (Optional) > ')
                    while True:
                        priority = input('Priority (High, Normal, Low) > ').strip().capitalize()
                        if priority not in ['High','Normal','Low','']:
                            print('Please choose either High, Normal, or Low')
                        else:
                            break

                    task = Task(task_name,description,due_date,priority)
                    manager.add_task(task=task)
                    while True:
                        another = input('Would you like to add another task (Y,N) > ').lower()
                        if another in ['y','n']:
                            break
                    if another == 'n':
                        break
                

            case 2:
                while True:
                    print('Task: ')
                    print(20*'-')
                    manager.view_task()
                    print('\n')
                    answer = input('What task would you like to remove > ')
                    if manager.remove_task(answer):
                        while True:
                            another = input('Would you like to remove another task (Y,N) > ').lower()
                            if another in ['y','n']:
                                break
                        if another == 'n':
                            break
                    else:
                        print('Task was not listed')
                        print('Please try another task')
            
            case 3:
                while True:
                    print('Task: ')
                    print(20*'-')
                    manager.view_task()
                    print('\n')
                    answer = input('What task would you like to mark as complete > ')
                    if manager.complete_task(answer):
                        while True:
                            another = input('Would you like to mark another task complete (Y,N) > ')
                            if another.lower() in ['y','n']:
                                break
                        if another.lower() == 'n':
                            break
                    else:
                        print('Task was not listed')
                        print('Please try another task')
            
            case 4:
                print('Tasks')
                print(20*'-')
                manager.view_task()

            case 5:
                print('Completed Tasks')
                print(20*'-')
                manager.view_completed()

            case 6:
                while True:
                    answer = input('Are you sure you want to quit? (Y/N)').lower().strip()
                    if answer not in ['y','n']:
                        print('Please answer with either a Y or N')
                    else:
                        break

                if answer == 'y':
                    sys.exit('Goodbye')
        
        while True:
            another_action = input('Would you like to do something else (Y,N) > ')
            if another_action.lower().strip() in ['y','n']:
                break
        
        if another_action.lower().strip() == 'n':
            print("Goodbye")
            break
if __name__ == '__main__':
    main()