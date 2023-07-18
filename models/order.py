class Order():
    def __init__(self, customer_name, order_date, quantity, pc_part, description):
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.pc_part = pc_part
        self.description = description