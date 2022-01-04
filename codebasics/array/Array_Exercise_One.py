data = {
    "January": 2020,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}
months = ["January","February","March","April","May","June","July","August","October","November","December"]

def compare(month1:str, month2:str)->int:
    value = data[month1] - data[month2]
    return int(value)

def income(num_months:int)->int:
    income = 0
    for i in range(num_months):
        month = months[i]
        income += int(data[month])
    return income

def find(ammount:int)->bool:
    for key, value in data.items():
        if data[key]==ammount:
            return True
        else:
            continue
    return False

def add(month:str, ammount:int)->dict:
    data[month] = ammount
    return data

def refund(month:str, new_ammount:int)->dict:
    data[month]= int(data[month])-new_ammount
    return data


