from api import datos_abiertos as da
from ui import interface, filter_information as fi


registers_limit, departament_name = interface.menu()
data = da.colsult(registers_limit, departament_name)
filtered_data = fi.filter_columns(data)
print(filtered_data)
