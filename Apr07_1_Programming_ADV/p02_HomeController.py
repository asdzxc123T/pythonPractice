# C
from p02_Doctor import Doctor
from p02_V import ConsoleScreen


if __name__ == "__main__":
    guest = ConsoleScreen.getGuestInfo()
    Doctor.calculate(guest)
    ConsoleScreen.printBMI(guest)