def menu():
    print("\nBIENVENIDO A DATOS ABIERTOS COLOMBIA, EN ESTA SECCIÓN PODRAS CONSULTAR LOS CASOS DE COVID-19 EN EL PAÍS")
    registers_limit = int(input("Digite el limite de registros: "))
    departament_name = input("Digite el departamento (EN MAYUSCULA): ")
    return [registers_limit, departament_name]
