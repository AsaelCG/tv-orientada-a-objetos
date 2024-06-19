#canales, volumen, contraste
class TV:
    
    def __init__(self, marca, tamanio, volumen=6):
        self.marca = marca
        self.tamanio = tamanio
        #aqui podemos utilizar valores por default
        self.prendida = False
        self.VOL_MAX = 10
        self.VOL_MIN = 0
        self.VOL_actual = volumen
        self.lista_canales = [2,4,5,7,10,12]

    def cambiar_volumen(self, volumen):
        if self.prendida:
            self.VOL_actual = self.VOL_actual + volumen
            if self.VOL_actual > self.VOL_MAX:
               self.VOL_actual = self.VOL_MAX
            if self.VOL_actual < self.VOL_MIN:
                self.VOL_actual = self.VOL_MIN

    def power (self):
        if (self.prendida):
            self.prendida = False
        else: 
            self.prendida = True

    def estatus_actual(self):
        return f"================\n{self}\n\tPower:{self.prendida}\n\tVolumen:{self.VOL_actual}\n====================="
        

    def __repr__(self):
        return f'{self.marca} - {self.tamanio} pulgadas'