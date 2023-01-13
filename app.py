def run():

    # functions
    def addTask():
        dataTask = input("ingresa tarea nueva: ")
        typeTask = input("ingresa el tipo de la tarea: ")

        # create file task
        fileTask = open("./public/" + dataTask + ".txt", 'a+')

    options = {"1": "Crear nueva tarea",
               "2": "Ver tareas pendientes", "3": "Borrar pendiente"}

    def showTask():
        print("show")

    def deleteTask():
        print("delete")
    print("Bienvenido!")
    print()
    for x in options.keys():
        for y in options.values():
            print(x + " " + y)
            break
    opt = input("Selecciona una opción: ")
    if (opt == str(1)):
        addTask()
    elif (opt == str(2)):
        showTask()
    elif (opt == str(3)):
        deleteTask()


# run script
if __name__ == '__main__':
    run()
