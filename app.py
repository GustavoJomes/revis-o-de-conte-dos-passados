from Modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexican food', 'comida mexicana')
restaurante_japones = Restaurante('japa', 'japonesa')

restaurante_mexicano.alternar_estado()

restaurante_mexicano.receber_avaliacao('João', 5)
restaurante_mexicano.receber_avaliacao('Pedro', 4)
restaurante_mexicano.receber_avaliacao('Carlos', 8)
restaurante_mexicano.receber_avaliacao('Ronaldo', 10)


def main():
    Restaurante.listar_restaurantes()
if __name__ == '__main__':
    main()