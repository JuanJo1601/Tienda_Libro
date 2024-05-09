from Transacion import Transaccion

class Libro:
    
    def __init__(self, isbn, titulo, precioVenta, precioCompra, cantidadActual, imagen):
        self.__transacciones = []
        self.__isbn = isbn
        self.__titulo = titulo
        self.__precioVenta = precioVenta
        self.__precioCompra = precioCompra
        self.__cantidadActual = cantidadActual
        self.__imagen = imagen

    def getISBN(self):
        return self.__isbn 

    def setIsbn(self, nIsbn):
        self.__isbn = nIsbn

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, nTitulo):
        self.__titulo = nTitulo
    
    def getPrecioVenta(self):
        return self.__precioVenta

    def setPrecioVenta(self, nPrecioVenta):
        self.__precioVenta = nPrecioVenta
    
    def getPrecioCompra(self):
        return self.__precioCompra
    
    def setPrecioCompra(self, nPrecioCompra):
        self.__precioCompra = nPrecioCompra
    
    def getCantidadActual(self):
        return self.__cantidadActual

    def setCantidadActual(self, nCantidadActual):
        self.__cantidadActual = nCantidadActual
    
    def getImagen(self):
        return self.__imagen
    
    def setImagen(self, nImagen):
        self.__imagen = nImagen

    def vender(self, cantidad, fecha):
        vendido = False
        if cantidad <= self.getCantidadActual():
            
            self.setCantidadActual(self.getCantidadActual()-cantidad)
            nueva = Transaccion(1, cantidad, fecha)
            self.__transacciones.append(nueva)
            vendido = True

        return vendido

    def abastecer(self, cantidad, fecha):

        self.setCantidadActual(self.getCantidadActual()+cantidad)
        nueva = Transaccion(2, cantidad, fecha)
        self.__transacciones.append(nueva)
