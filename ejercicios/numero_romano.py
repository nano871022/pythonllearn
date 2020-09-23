class NumeroRomano(object):
    def numeroARomano(self, n):
        recuerda = n
        numeroRomano = ""
        if n == 6:
            numeroRomano = "V"
            recuerda -= n-1
        elif n == 5:
            numeroRomano = "V"
            recuerda -= n
        elif n == 4:
            numeroRomano = "IV"
            recuerda -= n
        while recuerda >= 1:
            numeroRomano += "I"
            recuerda -= 1
        return numeroRomano
