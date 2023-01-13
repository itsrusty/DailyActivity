from data import dataTasked
import os

def run():

    # functions
    def addTask():
        dataTask = input("ingresa tarea nueva: ")
        contentTask = input("información de la tarea: ")

        # create file task
        fileTask = open("./data/" + dataTask + ".txt", 'a+')
        fileTask.write(contentTask)
        fileTask.close()

        run()
        print()

    options = {"1": "Crear nueva tarea",
               "2": "Ver tareas pendientes", "3": "Borrar pendiente"}

    def readTask():
        print()
        dataTasked.showData()
        optionsReadTask = ["borrar tarea", "leer tarea"]
        print()
        for x in optionsReadTask:
            print("opciones extra: " + x)
        op = input()
        if (op == "1"):
            deleteTask()
        elif (op == "2"):
            read = input("ingresa el nombre del archivo a leer: ")
            with open("./data/" + read, "r") as f:
                content = f.read()
                print(content)

    # delete section
    def deleteTask():
        # show data directory
        dataTasked.showData()
        nameTask = input("ingresa nombre de la tarea a borrar: ")

        # delete task
        os.remove("./data/" + nameTask)
        print("tarea eliminada")
        run()

    # **index**
    print("Bienvenido!")
    print()

    for listOptions in options.items():
        print(listOptions)

    opt = input("Selecciona una opción: ")
    if (opt == str(1)):
        addTask()
    elif (opt == str(2)):
        readTask()
    elif (opt == str(3)):
        deleteTask()


# run script
if __name__ == '__main__':
    run()
