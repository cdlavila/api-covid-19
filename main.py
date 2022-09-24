from api import datos_abiertos
from ui import interface, filter_information


if __name__ == '__main__':
    registers_limit, departament_name = interface.menu()
    data = datos_abiertos.get_data(registers_limit, departament_name)
    filtered_data = filter_information.filter_columns(data)
    print(filtered_data)
