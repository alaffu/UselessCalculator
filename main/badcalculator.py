import pyautogui


print("Welcome to the most useless calculator in the world :)")


def find_calculator():
    """will find where the calculator is in the screen"""
    position = pyautogui.locateOnScreen("assets/calculator.png", confidence=0.95)
    return position


def locate_numbers(*numbers):
    """it locates the numbers in the calculator"""
    position = []
    img = "assets/nx.png"
    here = find_calculator()
    for i in numbers:
        img = "assets/n{}.png".format(i)
        position = pyautogui.locateOnScreen(img,
                                            confidence=0.95,
                                            grayscale=True,
                                            region=here
                                            )
    return position


def locate_symbols(*symbols):
    """locate symbols in the applications calculator"""
    position = None
    for i in symbols:
        if i == "*":
            pass
    return position


def write_numbers(numbers):
    """write all numbers in sequence in the calculator"""

    for i in numbers:
        position = locate_numbers(i)
        pyautogui.moveTo(position)
        pyautogui.click()

    pyautogui.moveTo(100, 200)
    pyautogui.click()


def clear_all():
    """will clear everything written in the calculator"""
    position = pyautogui.locateOnScreen("assets/nC.png", confidence=0.95)
    pyautogui.moveTo(position)
    pyautogui.click()
    go_back()
    return position


def go_back():
    """click back in the terminal"""
    pyautogui.moveTo(100, 200)
    pyautogui.click()


while True:
    j = input("Add all numbers to be clicked: ")
    list_numbers = [int(i) for i in str(j)]

    print("this is a list of numbers", list_numbers)
    write_numbers(list_numbers)
    # for i in list_numbers:
    #     write_numbers(i)

    keep_type = str(input("Do you want to keep typing?(Y/N): "))
    check = keep_type.upper()
    if check == "N":
        clear_all()
        break
