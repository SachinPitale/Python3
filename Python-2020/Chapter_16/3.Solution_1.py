
class Laptop:
    def __init__(self, brand_name,model_name, price):
        # Instance variable
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price




L1 = Laptop('Lenovo','As900','38000')
L2 = Laptop('Dell','DL1300','48000')

print(L1.brand_name)
print(L2.brand_name)