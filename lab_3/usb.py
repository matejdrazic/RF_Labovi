def main():

    file_path = "setupapi.dev.log"

    parseSetupApi(file_path)


def parseSetupApi(setup_file):

    file = open(setup_file)

    lines = file.readlines()

    installed_string = "[Device Install (Hardware initiated)"

    for i, line in enumerate(lines):
        if installed_string in line and "USBSTOR" in line:
            output(lines[i].split('#')[1].split('&')[1], lines[i+1].strip('> '))


def output(usb_line, date):

    print(usb_line)
    print(date)


main()