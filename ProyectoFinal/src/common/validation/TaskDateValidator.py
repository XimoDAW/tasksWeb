from datetime import datetime

def startDateValidator(startDate):
    date = datetime.strftime(datetime.strptime(startDate, "%Y-%m-%d"), "%d-%m-%Y")
    dateToday = datetime.now().strftime("%d-%m-%Y")

    if (date < dateToday):
        raise Exception('No puedes insertar una fecha inicial anterior a la fecha actual')
    