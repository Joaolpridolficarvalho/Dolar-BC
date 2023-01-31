from bs4 import BeautifulSoup
import requests
import re


class USD:


    def __init__(self, date_initial, date_final):

        self.date_initial = date_initial
        self.date_final = date_final
        self.values = []
        self.date_interval = {}
        self.analytic_page = ""
        self.url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=consultarBoletim"
        self.create_dictionary()
        self.page = self.access_url()
        self.get_content_page()
        self.analytic_file()
        self.find_class()
        self.find_tag() 
        self.replace_pontuacion()
        self.delete_data_unnecessary()

    def create_dictionary (self):
          self.date_interval = {"DATAINI": self.date_initial, "DATAFIM": self.date_final, "ChkMoeda": "61", "RadOpcao": "1"}
    
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
        
    def analytic_file(self):
        text_file = open("content of page.html", "rb")
        analysis = BeautifulSoup(text_file, 'html.parser')
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
                self.values.append("date")
                self.values.append(data)
    def delete_data_unnecessary(self):
        letter_kinde_coin = "A"
        for data in self.values:
            if data == letter_kinde_coin:
                self.values.remove(data)
    def show_values(self):
        try:
            return self.values
        except IndexError:
            return []
    

    def USD2BRL(self, brl):
    
        try:
            conversion = brl / self.values[len(self.values)-1]
            return conversion
        except IndexError:
            return
    
    def BRL2USD(self, usd):
        try:
            conversion = usd * self.values[len(self.values)-2]
            return conversion
        except IndexError:
            return
    
