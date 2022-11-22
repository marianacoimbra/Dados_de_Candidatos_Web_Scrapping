class Utils:
    def __init__(self, response):
        self.response = response

    def __get_name(self):
        name = self.response.xpath(f'//*[@id="identificacao"]/div/div/div[3]/div/div/div[2]/div[1]/ul/li[1]/text()').get().strip()
        return name

    def __get_birthDate(self):
        info = self.response.xpath(f'//*[@id="identificacao"]/div/div/div[3]/div/div/div[2]/div[1]/ul/li[5]/text()').get().strip()
        return info

    
    def __get_presences_plenary(
        self,
    ):
        try:
            presences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[1]/text()').get().strip()
            return presences
        except:
            return None

    def __get_plenary_absences(
        self,
    ):
        try:
           absences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[3]/text()').get().strip()
           return absences
        except:
            return None 

    def __get_jusified_plenary_absences(
        self,
    ):
        try:
            justified_absences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[1]/dl/dd[2]/text()').get().strip()
            return justified_absences
        except:
            return None 
        
    def __get_presences_commisions(
        self,
    ):
        try:
            persences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[1]/text()').get().strip()
            return persences
        except:
            return None

    def __get_absences_commisions(
        self,
    ):
        try:
            absences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[3]/text()').get().strip()
            return absences
        except:
            return None

    def __get_absences_commisions_justified(
        self,
    ):
        try:
            justified_absences = self.response.xpath(f'//*[@id="atuacao-section"]/div[2]/ul[2]/li[2]/dl/dd[2]/text()').get().strip()
            return justified_absences
        except:
            return None

    def __get_total_expenses_par(
        self,
    ):
        table = self.response.xpath('//*[@id="gastomensalcotaparlamentar"]')
        rows = table.xpath('//tr')
        total = rows[1].xpath('td//text()').extract()[1].strip()

        return total

    def ___get_expenses_par(
        self,
        ):
        expenses = []
        rows = self.response.xpath('//*[@id="gastomensalcotaparlamentar"]/tbody/tr')
        for row in rows:
            expense = {
                     'month' : row.xpath('td[1]//text()').extract_first(),
                    'expense' : row.xpath('td[2]//text()').extract_first(),
                 }
            expenses.append(expense)
        return expenses


    def __get_total_expenses_gab(
        self,
    ):
        table = self.response.xpath('//*[@id="gastomensalverbagabinete"]')
        rows = table.xpath('//tr')
        total = rows[1].xpath('td//text()').extract()[1]

        return total

    def __get_expenses_gab(
        self,
        ):
        expenses = []
        rows = self.response.xpath('//*[@id="gastomensalverbagabinete"]/tbody/tr')
        for row in rows:
            expense = {
                     'month' : row.xpath('td[1]//text()').extract_first(),
                     'expense' : row.xpath('td[2]//text()').extract_first(),
                    }
            expenses.append(expense)
        return expenses

    def __get_gross_salary(
        self,
    ):
        row = self.response.xpath('//*[@class="recursos-beneficios-deputado-container"]/li[2]/div/a/text()').extract()
        salary = float(row[0].split("\n")[1].replace(".", "").replace(",", "."))
        return salary

    def __get_trips(
        self,
    ):
        trips = self.response.xpath('//*[@class="recursos-beneficios-deputado-container"]/li[5]/div/a/text()').get()
        return trips

    def main(self, gender):

        data = {
            "nome": self.__get_name(),
            "genero": gender,
            "presença_plenario": self.__get_presences_plenary(),
            "ausencia_plenario": self.__get_plenary_absences(),
            "ausencia_justificada_plenario": self.__get_jusified_plenary_absences(),
            "presenca_comissao": self.__get_presences_commisions(),
            "ausencia_comissao": self.__get_absences_commisions(),
            "ausencia_justificada_comissao": self.__get_absences_commisions_justified(),
            "data_nascimento": self.__get_birthDate(),
            "gasto_total_par": self.__get_total_expenses_par(),
            "gasto_jan_par": self.___get_expenses_par()[0],
            "gasto_fev_par": self.___get_expenses_par()[1],
            "gasto_mar_par":self.___get_expenses_par()[2],
            "gasto_abr_par": self.___get_expenses_par()[3],
            "gasto_mai_par": self.___get_expenses_par()[4],
            "gasto_jun_par": self.___get_expenses_par()[5],
            "gasto_jul_par": self.___get_expenses_par()[6],
            "gasto_ago_par": self.___get_expenses_par()[7],
            "gasto_set_par": self.___get_expenses_par()[8],
            "gasto_out_par": self.___get_expenses_par()[9],
            #não tem os expenses referentes a esses meses na tabela do html
            "gasto_nov_par": "não contabilizados",
            "gasto_dez_par": "não contabilizados",
            "salario_bruto_par": self.__get_gross_salary(), 
            "gasto_total_gab": self.__get_total_expenses_gab(),
            "gasto_jan_gab": self.__get_expenses_gab()[0],
            "gasto_fev_gab": self.__get_expenses_gab()[1],
            "gasto_mar_gab": self.__get_expenses_gab()[2],
            "gasto_abr_gab": self.__get_expenses_gab()[3],
            "gasto_mai_gab": self.__get_expenses_gab()[4],
            "gasto_jun_gab": self.__get_expenses_gab()[5],
            "gasto_jul_gab": self.__get_expenses_gab()[6],
            "gasto_ago_gab": self.__get_expenses_gab()[7],
            "gasto_set_gab": self.__get_expenses_gab()[8],
            "gasto_out_gab": self.__get_expenses_gab()[9],
            #não tem os expenses referentes a esses meses na tabela do html
            "gasto_nov_gab": "não contabilizados",
            "gasto_dez_gab": "não contabilizados",
            "salario_bruto": self.__get_gross_salary(),
            "quant_viagem": self.__get_trips()
        }
        return data
