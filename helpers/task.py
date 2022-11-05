class TaskBase:
    def __init__(self, name, output=True) -> None:
        """Initialize a TaskBase object."""
        self.name = name
        self.output = output

    def task_to_list(list):
        """Decorator to add a function to a list of tasks.
        Function should return a dictionary of variables to log."""

        def subtask(func):
            list.append(func)
            return func

        return subtask

    @staticmethod
    def intInput(varname):
        """Get an integer input from the user."""
        while True:
            try:
                return int(input(f"Enter {varname}: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def runTasks(self):
        """Run all tasks in the tasklist."""
        self.log("################")
        self.log(f"running Task {self.name}...")
        self.log("################")
        for task in self.tasklist:
            res = task(self)
            if res:
                self.log(task.__name__, **res)
        self.log("done")
        self.log("################")

    def log(self, msg, **vars):
        """Print a message with variables.
        Checks if output is enabled."""
        if not self.output:
            return
        if not vars:
            print(msg)
            return
        var_list = []
        msg += ":"
        for key, value in vars.items():
            var_list.append(f"{key} = {value}")
        var_str = "; ".join(var_list)
        print(msg, var_str)


def runSession(file, dir=""):
    """Run all tasks in all files in directory of the file.
    Optional argument dir can be used to specify a child directory.
    Ignores main.py and files starting with _."""
    from os.path import dirname, basename, isfile, join
    import glob
    import importlib
    import sys

    files = glob.glob(join(dirname(file), dir, "*.py"))
    for f in files:
        if not isfile(f):
            continue
        fname = basename(f)
        if f.endswith("main.py") or fname.startswith("_"):
            continue
        modname = f"{dir}.{fname[:-3]}" if dir else fname[:-3]
        importlib.import_module(modname)
        mod = sys.modules[modname]
        try:
            mod.Task(mod.__name__).runTasks()
        except Exception as e:
            print(e)
        print("\n")
