class Operaciones():
    def suma(self, sumando1, sumando2):
        for n in (sumando1, sumando2):
            if not isinstance(n,int) and not isinstance(n,float):
                raise TypeError("No es un int ni un float")
        return sumando1+sumando2

