#composition

#without creating university object cant create  department object


class university:
    def __init__(self):
        self.dept=self.department()


    class  department:
        pass


u=university()

