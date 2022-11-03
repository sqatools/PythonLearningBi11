class school:
    # class variable
    name = "Convent School"
    _city = "Mumbai"
    __address  = "Borvali"

    def __init__(self,  fee, standard,  groud):
        self.fee = fee
        self._stand = standard
        self.__ground = groud

    def show_school_fee(self):
        print("standard:",  self._stand)

    def _check_groud_availability(self):
        print("Availability :", self.__ground)

    def __show_all_details(self):
        print("fee :", self.fee)
        print("standard :", self._stand)
        print("ground :", self.__ground)

    @classmethod
    def show_school_city(cls):
        print(cls._city)

    @classmethod
    def school_class_method(cls):
        print(cls.name)
        cls.show_school_city()

    @staticmethod
    def multiplication_number(num1, num2):
        print(num1*num2)

    def show_result(self):
        pass

if __name__ == '__main__':
    obj = school("2lAc", "1oth", "Yes")
    print(obj.__class__)
    print(obj.__module__)

