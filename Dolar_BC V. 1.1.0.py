from bs4 import BeautifulSoup
import requests
import re


class USD:

    def __init__(self, date_initial, date_final):
        self.list_dict = []
        self.date_initial = date_initial
        self.date_final = date_final
        self.values = []
        self.date_interval = {}
        self.analytic_page = ""
        self.url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"
        self.create_dictionary()
        self.page = self.access_url()
        self.get_content_page()
        self.find_class()
        self.find_tag()
        self.replace_pontuacion()
        self.delete_data_unnecessary()
        self.list_to_dict()

    def create_dictionary(self):
        self.date_interval = {"DATAINI": self.date_initial, "DATAFIM": self.date_final, "ChkMoeda": "61",
                              "RadOpcao": "1"}

    def access_url(self):
        try:
            page = requests.post(self.url, data = self.date_interval)
            self.analytic_page = BeautifulSoup(page.content, 'html.parser')
            return page
        except:
            page.close
            return

    def get_content_page(self):
        text_file = open("content of page.html", "wb")
        text_file.write(self.page.content)
        text_file.close()


    def find_class(self):
        self.class_found = self.analytic_page.find_all('tbody', attrs={'class': 'centralizado'})

    def find_tag(self):
        self.tag_found = re.findall(r'<td>(.*)</td>', str(self.class_found))

    def replace_pontuacion(self):
        for data in self.tag_found:
            try:
                data = float(data.replace(',', '.'))
                self.values.append(data)
            except:

                self.values.append(data)

    def delete_data_unnecessary(self):
        letter_kinde_coin = "A"
        for data in self.values:
            if data == letter_kinde_coin:
                self.values.remove(data)

    def show_values(self):
        try:
            return self.list_dict
        except IndexError:
            return []

    def USD2BRL(self, brl):
        try:
            value_buy = brl * self.values[len(self.values) - 2]
            value_sell = brl * self.values[len(self.values) - 1]
            conversion = {"Value of conversion (buy)": value_buy, "Value of conversion (sell)": value_sell}
            return conversion
        except IndexError:
            return

    def BRL2USD(self, usd):
        try:
            value_buy = usd / self.values[len(self.values) - 2]
            value_sell = usd/ self.values[len(self.values) - 1]
            conversion = {"Value of conversion (buy)": value_buy, "Value of conversion (sell)": value_sell}
            return conversion
        except IndexError:
            return
    def list_to_dict(self):
        temp_list = ["Date", "Buy", "Sell"]
        for item in range(0,len(self.values),3):
            slice_list = self.values[item:item + 3]
            temp_dict = dict(zip(temp_list, slice_list))
            self.list_dict.append(temp_dict)
