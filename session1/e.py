class Task:
    def __init__(self) -> None:
        print("################")
        print("running Task E...")
        print("################")

    def task1(self):
        self.A = list(range(10, 21))
        self.B = list(range(20, 31))
        print(f"task1: A: {self.A}")
        print(f"task1: B: {self.B}")

    def task2(self):
        self.B[4] = self.A[2] + self.A[3]
        self.B[5] *= 2
        print(f"task2: B: {self.B}")

    def task3(self):
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        print(f"task3: A: {self.A}")

    def task4(self):
        i = 3
        j = 5
        self.B[i], self.A[j] = self.A[j], self.B[i]
        print(f"A: {self.A}, B: {self.B}")

    def runTasks(self):
        self.task1()
        self.task2()
        self.task3()
        self.task4()


if __name__ == "__main__":
    task = Task()
    task.runTasks()
    print(task.B[3])