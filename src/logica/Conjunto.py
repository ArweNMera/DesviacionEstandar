# src/logica/Conjunto.py

class Conjunto:
    def __init__(self, conjunto):
        self.__conjunto = conjunto

    def promedio(self):
        """Calcula el promedio de los elementos del conjunto."""
        if len(self.__conjunto) > 0:
            return sum(self.__conjunto) / len(self.__conjunto)
        else:
            return None

    def desviacion_estandar(self):
        """Calcula la desviación estándar del conjunto."""
        if len(self.__conjunto) == 0:
            raise ValueError("El conjunto no puede estar vacío.")
        elif len(self.__conjunto) == 1:
            return 0  # Si solo hay un elemento, la desviación es 0
        else:
            # Cálculo de la desviación estándar
            promedio = self.promedio()
            varianza = sum((x - promedio) ** 2 for x in self.__conjunto) / len(self.__conjunto)
            return varianza ** 0.5
