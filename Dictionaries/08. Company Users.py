def find(dict_1,word):
    for words in dict_1.values():
        if word in words:
            return True
    else:
        return False


class Company:

    def __init__(self):
        self.my_company = {}

    def add_employee(self, company, employee_id):
        if company not in self.my_company:
            self.my_company[company] = [employee_id]
        else:
            if not find(self.my_company,employee_id):
                self.my_company[company].append ( employee_id )

    def __repr__(self):
        sorted_my_company= dict ( sorted ( self.my_company.items (), key=lambda x: x[0], reverse=False ) )
        result = ''
        for key, value in sorted_my_company.items():
            result += f"{key}"+'\n'
            for i in range ( 0, len ( value ) ):
                current_value = value[i]
                result += f"-- {current_value}" + '\n'
        return result


company = Company ()

while True:
    command = input ()
    if command == 'End':
        break
    company_name, employee_id = command.split ( ' -> ' )
    company.add_employee ( company_name, employee_id )

print ( company )