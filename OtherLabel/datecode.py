__author__ = 'a5'

import datetime


def monthToNum(date):
    return{
            '01' : "J",
            '02' : "F",
            '03' : "M",
            '04' : "A",
            '05' : "Y",
            '06' : "U",
            '07' : "L",
            '08' : "G",
            '09' : "S",
            '10' : "O",
            '11' : "N",
            '12' : "D"
    }[date]



def getEncoded():
    today = datetime.date.today()
    today = str(today)
    year = today[2:4]
    mo = today[5:7]
    mo = monthToNum(mo)
    day = today[8:10]
    ##supplier and invoice number
    supplier = "L"
    invoice_number = "18"
    code = year+mo+day+supplier+invoice_number
    return code


print(getEncoded())