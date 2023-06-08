
#step1
months_named = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months_named)

#step2
months_numbered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(months_numbered)

#step3
months_dict1 = zip(months_named, months_numbered)
months_dict = dict(months_dict1)
print(months_dict)

#step4
months_named.clear()
print(months_named)
months_numbered.clear()
print(months_numbered)

#step5
printed_dict = list(months_dict.items())
print(printed_dict)

#step6
months_extracted = list(months_dict.keys())
print(months_extracted)

months_extracted.sort()
print(months_extracted)





