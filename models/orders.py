class Order:
    def __init__(self, id, styles_id, sizes_id, metals_id):
        self.id = id
        self.styles_id = styles_id
        self.sizes_id = sizes_id
        self.metals_id = metals_id
        self.metal = None
        self.size = None
        self.style = None
        
