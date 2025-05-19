from tinydb import TinyDB, Query

class TaskManager:
    def __init__(self, db_path="tasks.json"):
        self.db = TinyDB(db_path)
        self.tasks_table = self.db.table("tasks")
        self.reinforcers_table = self.db.table("reinforcers")

    def add_task(self, task):
        self.tasks_table.insert(task)

    def get_tasks(self):
        return self.tasks_table.all()

    def update_task(self, task_id, updates):
        Task = Query()
        self.tasks_table.update(updates, Task.id == task_id)

    def delete_task(self, task_id):
        Task = Query()
        self.tasks_table.remove(Task.id == task_id)

    def add_reinforcer(self, reinforcer):
        self.reinforcers_table.insert({"reinforcer": reinforcer})

    def get_reinforcers(self):
        return self.reinforcers_table.all()

    def delete_reinforcer(self, reinforcer_id):
        Reinforcer = Query()
        self.reinforcers_table.remove(Reinforcer.id == reinforcer_id)
