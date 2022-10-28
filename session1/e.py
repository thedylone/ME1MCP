from helpers.task import TaskBase


class Task(TaskBase):
    def __init__(self, name="", output=True) -> None:
        super().__init__(name, output)
        self.A = None
        self.B = None

    def task1(self):
        self.A = list(range(10, 21))
        self.B = list(range(20, 31))
        self.log(f"task1: A: {self.A}")
        self.log(f"task1: B: {self.B}")

    def task2(self):
        self.B[4] = self.A[2] + self.A[3]
        self.B[5] *= 2
        self.log(f"task2: B: {self.B}")

    def task3(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.log(f"task3: A: {self.A}")

    def task4(self):
        i = 3
        j = 5
        self.B[i], self.A[j] = self.A[j], self.B[i]
        self.log(f"A: {self.A}, B: {self.B}")


if __name__ == "__main__":
    task = Task("E")
    task.runTasks()
    print(task.B[3])
