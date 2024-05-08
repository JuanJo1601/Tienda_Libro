
class Transaccion:

    '''-------------------
    Atributos
    -------------------'''

    fecha = ''
    TIPO = {
        'abast' : 'Abastecimiento',
        'venta' : 'Venta'
    }

    '''-------------------
    Metodos
    -------------------'''

    def __init__(self, pFecha, pTipo, pCantidad):
        self.__fecha = pFecha
        self.__tipo = (self.TIPO.abast, self.TIPO.venta)[pTipo]
        self.__cantidad = pCantidad

    def getTipo(self):
        return self.__tipo

    def getFecha(self):
        return self.__fecha
    
    def getCantidad(self):
        return self.__cantidad
    
