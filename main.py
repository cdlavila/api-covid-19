from data import api
from ui import interface, filter_data


if __name__ == '__main__':
    registers_limit, departament_name = interface.menu()
    data = api.get_data(registers_limit, departament_name)
    filtered_data = filter_data.filter_columns(data)
    print(filtered_data)
