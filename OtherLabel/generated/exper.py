__author__ = 'a5'

def mapType(type):
    return{
            '5c' : ["5C LCD Ori", "butts"],
            '5s' : "5S LCD Ori",
            '6' : "6 LCD Ori",
            '6+' : "6+ LCD Ori",
            '5' : "5 LCD Ori",
    }[type]

print(mapType('5c')[1])