# dynamically typed variables
def dynamically_typed():
    print("Dynamically typed variable declaration ")
    name = "Yash"  # str
    age = 23  # int
    is_adult = True  # bool
    sun_sign = "A"  # also str - python doesn't have char
    print("Type of name is: ", type(name))
    print("Type of age is: ", type(age))
    print("Type of is_adult is: ", type(is_adult))
    print("Type of sun_sign is: ", type(sun_sign))


# using type hinting
# if we try to reassign variable to diff type we get message but code is still executed
def type_hinting():
    print("Variable declaration using type hinting")
    name: str = "Andy"
    age: int = 23
    is_adult: bool = False
    sun_sign: str = "Z"
    print("Type of name is: ", type(name))
    print("Type of age is: ", type(age))
    print("Type of is_adult is: ", type(is_adult))
    print("Type of sun_sign is: ", type(sun_sign))
    sun_sign = 26
    print("Type of sun_sign is: ",type(sun_sign))

# in Python since everything is an object,
# primitive types like int, float, str, bool are also classes.
# so we can also declare variables like

def using_class():
    print("Variable declaration using classPackage")
    name = str("Yash")
    age = int(23)
    is_adult = bool(True)
    sun_sign = str("P")
    print("Type of name is: ", type(name))
    print("Type of age is: ", type(age))
    print("Type of is_adult is: ", type(is_adult))
    print("Type of sun_sign is: ", type(sun_sign))


dynamically_typed()
# type_hinting()
# using_class()
