class Pokemon():
    def __init__(self, nome = "", ID = 0, HP = 0, AT = 0, DF = 0, SP_AT = 0, SP_DF = 0, SP = 0, golpes = []):
        self.nome = nome
        self.ID = ID
        self._HP = HP
        self._AT = AT
        self._DF = DF
        self._SP_AT = SP_AT
        self._SP_DF = SP_DF
        self._SP = SP
        self._golpes = golpes
        
    def atribuiHP(self, HP):
        self._HP = HP
        
    def atribuiAT(self, AT):
        self._AT = AT
        
    def atribuiDF(self, DF):
        self._DF = DF
        
    def atribuiSP_AT(self, SP_AT):
        self._SP_AT = SP_AT
    
    def atribuiSP_DF(self, SP_DF):
        self._SP_DF = SP_DF
    
    def atribuiSP(self, SP):
        self._SP = SP
    
    def aprendeGolpe(self, golpe):
        self._golpes.append(golpe)

pk1 = Pokemon("Blastoise", 9, 79, 83, 100, 85, 105, 78, ["Bubble","Tackle", "Tail Whip"])

print(pk1.__dict__)

pk2 = Pokemon()
pk2.nome = "Charizard"
pk2.ID = 6
pk2.atribuiHP(78)
pk2.atribuiAT(84)
pk2.atribuiDF(78)
pk2.atribuiSP_AT(109)
pk2.atribuiSP_DF(85)
pk2.atribuiSP(100)
pk2.aprendeGolpe("Ember")
pk2.aprendeGolpe("Growl")

print(pk2.__dict__)