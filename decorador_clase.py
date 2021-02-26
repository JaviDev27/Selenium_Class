class ClaseDecoradora:
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        print('se llama a la clase decorradora')
        self.fnc(*args, **kwargs)


@ClaseDecoradora
def hablar(mensaje):
    print(mensaje)


hablar('Hola')
