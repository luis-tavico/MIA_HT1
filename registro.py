import pickle
import os

class Profesor:
    def __init__(self, tipo, id_profesor, CUI, nombre, curso):
        self.tipo = tipo
        self.id_profesor = id_profesor
        self.CUI = CUI
        self.nombre = nombre 
        self.curso = curso

    def __str__(self):
        return f"Tipo: {self.tipo}, ID: {self.id_profesor}, CUI: {self.CUI}, Nombre: {self.nombre}, Curso: {self.curso}"

class Estudiante:
    def __init__(self, tipo, id_estudiante, CUI, nombre, carnet):
        self.tipo = tipo
        self.id_estudiante = id_estudiante
        self.CUI = CUI
        self.nombre = nombre
        self.carnet = carnet

    def __str__(self):
        return f"Tipo: {self.tipo}, ID: {self.id_estudiante}, CUI: {self.CUI}, Nombre: {self.nombre}, Carnet: {self.carnet}"

def write_file(data, file):
    mode = 'ab' if os.path.exists(file) else 'wb'
    with open(file, mode) as file:
        pickle.dump(data, file)

def read_file(file):
    with open(file, 'rb') as file:
        while True:
            try:
                instance = pickle.load(file)
                yield instance
            except EOFError:
                break

def main():

    mode = 'ab' if os.path.exists('datos.bin') else 'wb'
    with open('datos.bin', mode) as file:
        pass

    while True:
            print(" -----------MENU-PRINCIPAL----------- ")
            print("| 1. Registro de Profesor            |")
            print("| 2. Registro de Estudiante          |")
            print("| 3. Ver Registros                   |")
            print("| 4. Sallir                          |")
            print(" ------------------------------------ ")
            option = int(input("Ingrese una opcion: "))

            if option == 1:
                type = input("Ingrese el tipo: ")
                id = int(input("ingrese el ID: "))
                cui = input("Ingrese el CUI: ")
                name = input("Ingrese el nombre: ")
                course = input("Ingrese el curso: ")
                new_professor = Profesor("profesor", id, cui, name, course)
                write_file(new_professor, 'datos.bin')
                print("¡Profesor registrado exitosamente!\n")

            elif option == 2:
                type = input("Ingrese el tipo: ")
                id = int(input("ingrese el ID: "))
                cui = input("Ingrese el CUI: ")
                name = input("Ingrese el nombre: ")
                license = input("Ingrese el carnet: ")
                new_student = Estudiante("estudiante", id, cui, name, license)
                write_file(new_student, 'datos.bin')
                print("¡Estudiante registrado exitosamente!\n")

            elif option == 3:
                print(" -----------REGISTROS----------- ")
                try:
                    for item in read_file("datos.bin"):
                        print(item)
                except FileNotFoundError:
                    print("¡El archivo no existe!\n")
                print("")

            elif option == 4:
                print("¡Ejecucion Finalizada!\n")
                break

            else:
                print("¡Ingrese una opcion valida!")
    
if __name__ == '__main__':
    main()