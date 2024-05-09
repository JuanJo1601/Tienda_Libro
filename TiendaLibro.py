from Libro import Libro

class TiendaDeLibros:

    def __init__(self, caja):
        self.__caja = 1000000
        self.__catalogo = []

    def getCatalogo(self):
        return self.__catalogo
    
    def getCaja(self):
        return self.__caja
    
    def buscarLibroPorTitulo(self, titulo):
        libroBuscado = None

        for libro in self.__catalogo:
            if libro.getTitulo() == titulo:
                libroBuscado = libro
                break

        return libroBuscado
    
    def buscarLibroPorIsbn(self, isbn):
        isbnBuscado = None

        for isbn in self.__catalogo:
            if isbn.getIsbn() == isbn:
                isbnBuscado = isbn
                break
        
        return isbnBuscado

    def registrarLibro(self, isbn, titulo, precioVenta, precioCompra, cantidadActual, imagen):

        buscar = self.buscarLibroPorIsbn(isbn)
        nuevo = None
        if buscar == None:
            nuevo = Libro(titulo, isbn, precioVenta, precioCompra, cantidadActual, imagen)
            self.__catalogo.append(nuevo)

        return nuevo
    
    def eliminarLibro(self):
        buscar = self.buscarLibroPorIsbn
        eliminado = False
        if buscar:
            if buscar.getCantidadActual == 0:
                self.__catalogo.remove(buscar)
                eliminado = True
            
        return eliminado
    
    def darLibroMasEconomico(self):
        libroMasEconomico = None
        if (len(self.__catalogo)>0):
            libroMasEconomico = self.__catalogo[0]
            for Libro in self.__catalogo:
                if Libro.getPrecioVenta() < libroMasEconomico.getPrecioVenta():
                    libroMasEconomico = Libro
        return libroMasEconomico
        
        #Forma 2
        #for libroMasEconomico in self.__catalogo:
        #    if Libro.getPrecioVenta() < libroMasEconomico:
        #        libroMasEconomico = Libro
        #return libroMasEconomico
    
    def darLibroMasCostoso(self):
        libroMasCostoso = None
        libroMasCostoso = None
        if (len(self.__catalogo)>0):
            libroMasCostoso = self.__catalogo[0]
            for Libro in self.__catalogo:
                if Libro.getPrecioVenta() > libroMasCostoso.getPrecioVenta():
                    libroMasCostoso = Libro
        return libroMasCostoso
    
        #Forma 2
        #for libroMasCostoso in self.__catalogo:
        #    if Libro.getPrecioVenta() > libroMasCostoso:
        #        libroMasCostoso = Libro
        #return libroMasCostoso

    def Vender(self, cantidad, fecha, isbn = None, titulo = None):
        
        vendido = False
        buscado = self.buscarLibroPorIsbn(isbn)

        if titulo is not None and buscado is None:
            buscado = self.buscarLibroPorTitulo(titulo)
        
        if buscado:
            vendido = buscado.vender(cantidad, fecha)
            self.setCaja(self.getCaja+(cantidad*buscado.getPrecioVenta()))

        return vendido
    
    def Abastecer(self, cantidad, fecha, isbn)
