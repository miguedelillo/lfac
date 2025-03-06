class t_estado():
    nombre = None
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return str(self.nombre)
    def __repr__(self):
        return repr(self.nombre)
    def __eq__(self, value):
        return str(self) == str(value)
    def __hash__(self):
        return hash(self.nombre)
    
t_simbolo = str

#class t_simbolo():
#    representacion = None
#    def __init__(self, representacion):
#        self.representacion = representacion
#    def __str__(self):
#        return str(self.representacion)
#    def __repr__(self):
#        return repr(self.representacion)
        
class t_transicion():
    transiciones : dict[t_estado, t_simbolo] = dict()
    def __init__(self, transiciones: dict[t_estado, t_simbolo]):
        self.transiciones = transiciones

    def __setitem__(self, clave, valor):
        self.transiciones[clave] = valor

    def __getitem__(self, clave):
        try:
            return self.transiciones[clave]
        except:
            return False

    

    def __str__(self):
        return str(self.transiciones)
    def __repr__(self):
        return repr(self.transiciones)

class t_automata():
    estados : set[t_estado] = set()
    alfabeto : set[t_simbolo]= set()
    transicion : t_transicion= dict()
    estado_inicial : t_estado = None
    estados_finales : set[t_estado]= set()
    estado_actual : t_estado = None
    log = ''


    def __init__(self, estados : set[t_estado], alfabeto : set[t_simbolo], transicion : t_transicion, estado_inicial : t_estado, estados_finales : set[t_estado]):
        assert estado_inicial in estados, 'El estado inicial tiene que pertenecer al conjunto de estados del autómata'
        assert estados_finales.issubset(estados)
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicion = transicion
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def leer_cadena(self, cadena, print_log = False):
        self.log = f'Estado inicial: {self.estado_inicial}. Cadena: {cadena}'
        self.estado_actual = self.estado_inicial
        for paso, simbolo in enumerate(cadena):
            if simbolo not in self.alfabeto:
                self.log += f'\nEl símbolo {simbolo} no está en el alfabeto del AFD'
                if print_log: print(self.log)
                return False
                

            siguiente_estado = self.transicion[(self.estado_actual, simbolo)]

            if not siguiente_estado: 
                self.log += f'\nNo existe la transición ({self.estado_actual}, {simbolo}).'
                if print_log: print(self.log)
                return False

            cadena_actual = cadena if paso == 0 else cadena_actual[1:]

            self.log += f'\nPaso {paso}. ({self.estado_actual},{cadena_actual}) ⊢ ({siguiente_estado},{cadena_actual[1:]}).'
            self.estado_actual = siguiente_estado
        if print_log: print(self.log)
        return self.estado_actual in self.estados_finales
        

    def ver_log(self):
        return self.log
    def __str__(self):
        return f"Estados: {self.estados}. \nAlfabeto: {self.alfabeto}. \nFunción de transición: {self.transicion}. \nEstado inicial: {self.estado_inicial}. \nEstados finales: {self.estados_finales}."
    
        
