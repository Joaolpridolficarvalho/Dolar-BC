from bs4 import BeautifulSoup
import requests
import re


class Dolar:


    def __init__(self, date_initial, date_final):

        self.date_initial = date_initial
        self.date_final = date_final
        self.values = []
        date_range = {"DATAINI": date_initial, "DATAFIM": date_final, "ChkMoeda": "61", "RadOpcao": "1"}

        url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"

        try:
            page = requests.post(url, data=date_range)  # request ok
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            page.status_code
            page.close()

        text_file = open("content of page.html", "wb")

        text_file.write(page.content)
        text_file.close()

        text_file = open("content of page.html", "rb")
        soup = BeautifulSoup(text_file, 'html.parser')
        text_file.close()
        result = soup.find_all('tbody', attrs={'class': 'centralizado'})
        #        print(result)
        result = re.findall(r'<td>(.*)</td>', str(result))


        for data in result:
            try:
                data = float(data.replace(',', '.'))
                self.values.append(data)
            except:
                self.values.append(data)


        # removing column "TIPO"
        for data in self.values:
            if data == "A":
                self.values.remove(data)

        for value in self.values:
            print(value)

    def show_values(self):
        try:
            return self.values
        except IndexError:
            return []

    def convert_Reais_in_dollars(self, reais):
        try:
            conversion = reais / self.values[1]
            return conversion
        except IndexError:
            return
