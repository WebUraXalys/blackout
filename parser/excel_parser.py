import pandas


group = input("Введіть через пробіл номери груп, які потрібно спарсити: ")
index = group.split()

for i in index:
    sheets = pandas.read_excel(f"excel/Grupa_GPV_{i}.xlsx")
    sheet = sheets.dropna(subset=['Вулиця'])  # Excluding rows with empty cell "Street"
    a = 0
    while True:
        try:
            otg = sheet['ОТГ'].iloc[a]
            city = sheet['Місто'].iloc[a]
            street = sheet['Вулиця'].iloc[a]
            try:
                buildings_list = sheet['Будинок'].iloc[a]
            except:
                buildings_list = []
            data = {
                        "OTG": otg,
                        "City": city,
                        "Street": street,
                        "Buildings": buildings_list,
                        "Group": i
                    }
            print(data)
            print('______________________________________________________________________')

            a += 1
        except:
            break
