from validator import validate

print(validate(buildings='1, 10 а, 11а, 12') == ['1', '10а', '11а', '12'])
print(validate(buildings='1, 11 А, 11-Б, Діл.19') == ['1', '11а', '11б'])
print(validate(buildings='') == [])
