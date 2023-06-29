from tkinter import *

class CalculadoraAreaTriangulo:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 30
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Calculadora de Área de Triângulo")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.baseLabel = Label(self.segundoContainer,text="Base", font=self.fontePadrao)
        self.baseLabel.pack(side=LEFT)

        self.base = Entry(self.segundoContainer)
        self.base["width"] = 30
        self.base["font"] = self.fontePadrao
        self.base.pack(side=LEFT)
        
        self.alturaLabel = Label(self.terceiroContainer,text="Altura", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.terceiroContainer)
        self.altura["width"] = 30
        self.altura["font"] = self.fontePadrao
        self.altura.pack(side=LEFT)
        
        self.resposta = Label(self.quartoContainer, text="" , font=self.fontePadrao)
        self.resposta.pack()
        
        self.calcular = Button(self.quintoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calculaAreaTriangulo
        self.calcular.pack()

    def calculaAreaTriangulo(self):
        base = int(self.base.get())
        altura = int(self.altura.get())
        
        self.resposta["text"] = "A área é " + str((base * altura) / 2)


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        # selecionar qual calculadora sera usada
        
        CalculadoraAreaTriangulo()


root = Tk()
Application(root)
root.mainloop()