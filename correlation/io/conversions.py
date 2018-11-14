import math

def singular(word):
    """ removes trailing s from a string """

    if word[-1] == 's':
        word = word[:-1]

# seconds as base unit
_si_time = {"second"  : 1.0,
            "minute"  : 60.0,
            "hour"    : 3600.0,
            "day"     : 86400.0,
            "week"    : 604800.0,
            "year"    : 31622400.0,
            "decade"  : 316224000.0,
            "century" : 3162240000.0,
           }

_si_len = {"mm" : 0.001,
           "cm" : 0.01,
           "dm" : 0.1,
           "m"  : 1.0,
           "km" : 1000.0,
           "in" : 0.0254,
          }

def convert_si(val, from_unit, to_unit):

    return val * _si_time[from_unit]/_si_time[to_unit]

#testing

if __name__ == "__main__":
    
    print(convert_si(5, "week", "minute"))