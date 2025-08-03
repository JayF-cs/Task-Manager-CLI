from Task import Task
from tabulate import tabulate
import json


class TaskManager:

    def __init__(self):
        self._tasks = []
        self.completed = []
        self.read_from_file()

    def add_task(self, task):
        if any(t.task_name.lower() == task.task_name.lower() for t in self._tasks):
            print('That task already exists!')
        else: 
            self._tasks.append(task)
            self.save_to_file()

    def remove_task(self, task_name):
        for task in self._tasks:
            if task.task_name.lower() == task_name.lower():
                print(f'{task.task_name} has been removed...')
                self._tasks.remove(task)
                self.save_to_file()
                return 1
        
        return 0

    def complete_task(self,task_name):
        for task in self._tasks:
            if task.task_name.lower() == task_name.lower():
                self.completed.append(task)
                self._tasks.remove(task)
                self.view_completed()
                self.save_to_file()
                return 1
        
        return False


    def view_task(self):
        print('Task List:')
        if self._tasks == []:
            print('No Tasks Found!')
            return
        headers = ['Task Name','Description','Due Date','Priority']
        taskdata = [[t.task_name,t.description if t.description != '' else 'N/A',t.due_date if t.due_date != None else 'N/A',t.priority] for t in self._tasks]
        print(tabulate(taskdata,headers=headers,tablefmt='grid'))

    def view_completed(self):
        if self.completed == []:
            print('No Tasks Found!')
            return
        print('Completed Tasks:')
        headers = ['Task Name','Description','Due Date','Priority']
        taskdata = [[t.task_name,t.description if t.description != '' else 'N/A',t.due_date if t.due_date != None else 'N/A',t.priority] for t in self.completed]
        print(tabulate(taskdata,headers=headers,tablefmt='grid'))

    def save_to_file(self, filename = 'data.json'):
        if not self._tasks and not self.completed:
            return
        data = {
            'tasks': [vars(t) for t in self._tasks],
            'completed' : [vars(c) for c in self.completed]
        }

        with open(filename, 'w') as f:
            json.dump(data,f,indent=4)
        pass

    def read_from_file(self, filename = 'data.json'):

        try:
            with open(filename,'r') as f:
                data = json.load(f)
                self._tasks = [Task(**t) for t in data['tasks']]
                self.completed = [Task(**c) for c in data['completed']]
        except (FileNotFoundError, json.JSONDecodeError,ValueError):
            pass
    