class SkiRental:
    def __init__(self,p_skis,p_board):
        self.p_skis = p_skis
        self.p_board = p_board
    
    def preco_ski(self):
        return self.p_skis

    def preco_snowboarsd(self):
        return self.p_board

    def reserva(self,n_skis,n_board):
        return n_skis*self.p_skis + n_board*self.p_board
    
    def __repr__(self):
        return f'Ski: {self.p_skis}; Snowboard: {self.p_board}'