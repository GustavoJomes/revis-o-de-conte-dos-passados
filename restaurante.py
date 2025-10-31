import os

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'𝐍𝐨𝐦𝐞 𝐝𝐨 𝐑𝐞𝐬𝐭𝐚𝐮𝐫𝐚𝐧𝐭𝐞'.ljust(25)} | {'𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐚'.ljust(25)} | {'𝐒𝐭𝐚𝐭𝐮𝐬'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

Restaurante.listar_restaurantes()
