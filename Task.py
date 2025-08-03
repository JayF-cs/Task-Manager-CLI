class Task:

    def __init__(self, task_name, description = '', due_date =None, priority = 'Normal'):
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        
        return (
            f"Task: {self.task_name} | "
            f"Description: {'N/A' if self.description == '' else self.description} | "
            f"Due Date: {'N/A' if self.due_date is None else self.due_date} | "
            f"Priority: {self.priority}"
        )
