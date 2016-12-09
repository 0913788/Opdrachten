class Card():
    def __init__(self, type, value, effect=None):
        self.type = type
        self.value = value
        if(effect == None):
            self.effect=effect
        else:
            self.effect=self.SetEffect(effect)
    
    #String representation of a card.
    def ToString(self):
        return self.type +" "+ str(self.value)

    #TODO
    def SetEffect(self, effect): pass