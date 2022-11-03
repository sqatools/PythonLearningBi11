from OOPS_Concepts.pkg1.school_details import school

"""
obj1 = school("1lAc", "12th", "NO")
print(obj1.__class__)
print(obj1.__module__)

obj1.show_school_city()
print(dir(obj1))
"""

class show_result(school):
    def __init__(self, fee, standard, groud):
        super(show_result, self).__init__(fee, standard, groud)

    def show_result(self):
        print("School got 90% result this year")


#obj = show_result("1lAc", "12th", "NO")
#obj.show_result()

#obj = school("1lAc", "12th", "NO")
#obj.show_result()