class Order():

    def __init__(self, id, stylesId, sizesId, metalsId):
        self.id = id
        self.stylesId = stylesId
        self.sizesId = sizesId
        self.metalsId = metalsId

new_order = Order(1, 3, 3, 3)