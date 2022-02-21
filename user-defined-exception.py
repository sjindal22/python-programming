class CustomException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))

try:
    raise CustomException("Custom exception has been raised")

except CustomException as e:
    print(e.value)
