import re
import locale

cost_1 = '''Rs.ARMB-Mumbai (Tel: 022-26572754/ 7738614145/ 9167259214), Goa - Ponda (Tel: 0832/ 2316988 / 9422413675)'''
cost = ''
if cost_1[0:3] == 'Rs.' or cost_1[0:3] == 'rs.':
    cost = cost_1[3:]
else:
    cost = cost_1

def price(cost):
    res = {}
    res['Price'] = []
    res['Formated'] = False
    regex_1 = False
    regex_2 = False

    pattern_01 = re.finditer(r'([\w\s\w|\w\s|\w\s\.|\w\s&\s]+):?\s?(Rs\.)\s?([\d,\.?]+)\s?(Lakhs|Lacs|Crores|Crore|Lac|Cr.|Cr|/-)', cost)
    pattern_02 = re.finditer(r'(\(?.\))?([\d,\.?]+)\s?(Lakhs|Lacs.|Lacs|Crores|Crore|Lac|Cr.|Cr|/-)\s?', cost)
    pattern_03 = re.finditer(r'(\(?\d{1,2}\))([\d,\.?]+)\s?', cost)
    pattern_04 = re.finditer(r'^(\d*)$', cost)


    patterns = [pattern_01, pattern_02, pattern_03, pattern_04]
    count = 0
    def crore(val):
        decimal = float(val)
        val = int(decimal * 10000000)
        locale.setlocale(locale.LC_ALL, '')
        res = 'Rs. ' + locale.format_string('%d', val, 1)
        return res
    def lakh(val):
        decimal = float(val)
        val = int(decimal * 100000)
        locale.setlocale(locale.LC_ALL, '')
        res = 'Rs. ' + locale.format_string('%d', val, 1)
        return res
    def noUnit(val):
        val_1 = int(float(str(val).replace(',', '')))
        locale.setlocale(locale.LC_ALL, '')
        res = 'Rs. ' + locale.format_string('%d', val_1, 1)
        return res

    for pattern in patterns:
        count += 1
        for match in pattern:
            if count == 2 and regex_1 == False:
                if match.group(3) == None or match.group(3) == '/-':
                    try:
                        res['Formated'] = True
                        res['Price'].append(noUnit(match.group(2)))
                    except Exception:
                        res['Price'] = [cost]
                        return res
                if "La" in str(match.group(3)):
                    try:
                        res['Price'].append(lakh(match.group(2)))
                        res['Formated'] = True
                    except Exception:
                        res['Price'] = [cost]
                        return res
                if "Cr" in str(match.group(3)):
                    try:
                        res['Price'].append(crore(match.group(2)))
                        res['Formated'] = True
                    except Exception:
                        res['Price'] = [cost]
                        return res
                regex_2 = True

            elif count == 1 and len(match.groups()) == 4:
                if match.group(4) == None or match.group(4) == '/-':
                    try:
                        res['Formated'] = True
                        res['Price'].append(match.group(1)+': '+noUnit(match.group(3)))
                    except Exception:
                        res['Price'] = [cost]
                        return res
                if "La" in str(match.group(4)):
                    try:
                        res['Price'].append(match.group(1)+': '+lakh(match.group(3)))
                        res['Formated'] = True
                    except Exception:
                        res['Price'] = [cost]
                        return res
                if "Cr" in str(match.group(4)):
                    try:
                        res['Price'].append(match.group(1)+': '+crore(match.group(3)))
                        res['Formated'] = True
                    except Exception:
                        res['Price'] = [cost]
                        return res
                regex_1 = True
            elif count == 3 and regex_2 == False and regex_1 == False:
                if match.group(2) != None:
                    try:
                        res['Formated'] = True
                        res['Price'].append(noUnit(match.group(2)))
                    except Exception:
                        res['Price'] = [cost]
                        return res
            elif count == 4 and len(match.groups()) == 1:
                try:
                    res['Formated'] = True
                    res['Price'].append(noUnit(match.group(1)))
                except Exception:
                    res['Price'] = [cost]
                    return res

    if res['Formated'] == False:
        res['Price'] = [cost]
    return res

res = price(cost)
print(res)

