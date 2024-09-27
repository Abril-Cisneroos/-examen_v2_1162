# clase
class Veterinaria1162:
    def diccionario_sucursales_1162(self):
        sucursales={
            "ID sucursal:": 110201,
            "Nombre: ": "Veterinara estrella",
            "Direccion: ": "Av. de la  raza, calle falsa #7643",
            "Telefono: ": 65612345678,
            "Correo electronico: ": "vetestrella0@gmail.com",
            "Gerente a cargo: ": "Abril Cisneros Hernadez",
            "Horarios:": "lunes-sabado: 24h; domingos: 8am-8pm"
        }
        for a,c in sucursales.items():
            print(a,c)
    def diccionario_cliente_1162(self):
        clientes={
            "ID cliente :": 223080,
            "Nombre: ": "Itzel Cisneros Gonzales",
            "Correo electronico:": "itzelcis@gmail.com",
            "Telefono: ": 6567876545,
            "ID mascota: ": 110201,
            "Historial compra: ": "primera compra: cita para revision genareal  ultima compra: medicamento para desparacitar perros pequeños",
            "Historial de visitas: ": "primera viita: febrero/04/2022 ultima visita: septiembre/20/2024"            
        }
        for d,f in clientes.items():
            print(d,f)
    def diccionario_empleados_1162(self):
        empleados={
            "ID empleado:": 738393,
            "Nombre: ": "Frida Abril Cisneros Hernandez",
            "Direccion: ": "Av. Tecnologico, calle falsa #9763",
            "Telefono: ": 6563137887,
            "Correo electronico: ": "unempleado@gmail.com",
            "Cargo o puesto": "Gerente",
            "Horarios de trabajo :": "lunes-sabado: 8:00am-5:00pm",  
            "Salario: ": 4000           
        }
        for g,h in empleados.items():
            print(g,h)
    def diccionario_mascotas_1162(self):
        mascotas={
            "ID mascota:": 987654,
            "Nombre: ": "Canela",
            "Especie: ": "Mamifero",
            "Edad: ": "1 año",
            "Peso en kg:": 5,  
            "ID cliente": 223080,    
            "Historil medico:": "Alergias: ninguna, Operaciones:ninguna"                  
        }
        for i,j in mascotas.items():
            print(i,j)


#objeto
obj=Veterinaria1162()

# llamar a las funciones
print("  ")
print("Diccionario de sucursales")
obj.diccionario_sucursales_1162()
print("  ")
print("Diccionario de empleados")
obj.diccionario_empleados_1162()
print("  ")
print("Diccionario de clientes")
obj.diccionario_cliente_1162()
print("  ")
print("Diccionario de mascotas")
obj.diccionario_mascotas_1162()
print("  ")





