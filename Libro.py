class Libro:
    
    '''-------------------
    Metodos
    -------------------'''

    def __init__(self, pIsbn, pTitulo, pPrecioVenta, pPrecioCompra, pCantiddadActual, pImagen):
        self.__isbn = pIsbn
        self.__titulo = pTitulo
        self.__precioVenta = pPrecioVenta
        self.__precioCompra = pPrecioCompra
        self.__cantidadActual = pCantiddadActual
        self.__imagen = pImagen

    def getISBN(self):
        return self.__isbn
    
    def getTitulo(self):
        return self.__titulo
    
    def getPrecioVenta(self):
        return self.__precioVenta
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def getCantidadActual(self):
        return self.__cantidadActual
    
    def getImagen(self):
        return self.__imagen

