#creating decorator 

def login_Required(func):
    def inner(name,is_Login):
        if is_Login == False:
            print("Buddy Please login")
        else:
            return func(name, is_Login)

    return inner


@login_Required
def home_Page(name, is_Login):
    print("Home Page")


home_Page("Rahul", True)
home_Page("Modi", False)