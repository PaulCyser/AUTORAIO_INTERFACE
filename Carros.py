import tkinter as tk
from time import sleep


cores = {
    'azul': '\033[0:34m',
    'amarelo': '\033[1:33m',
    'roxo': '\033[1:35m',
    'azul2': '\033[1:34m'
}


def mostrar_carros():
    carro = int(entry_carro.get())
    carro_selecionado = instrucoes_var.get()
    # Implemente a lógica para mostrar os carros disponíveis com base na seleção.

    if 1 <= carro <= 11:
        label_resultado.config(text=f"CARREGANDO OS CARROS DISPONIVEIS ...")
        janela.update()
        sleep(2)

        carros_disponiveis = {
            1: [
                'Audi A3, Preço: R$ 124.900,00, Ano: 2018',
                'Audi A4, Preço: R$ 172.990,00, Ano: 2017',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            2: [
                'Celta, Preço: R$ 16,202, Ano: 2012',
                'Corsa, Preço: R$ 20,500.00, Ano: 2012',
                'Corsa Classic, Preço: R$ 30,500.00, Ano: 2012',
                'Cruze, Preço: R$ 89,900.00, Ano: 2017',
                'Joy, Preço: R$ 50,090.00, Ano: 2019',
                'Onix, Preço: R$ 67,900.00, Ano: 2018',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            3: [
                'C3, Preço: R$ 44,000.00, Ano: 2019',
                'C3 Picasso, Preço: R$ 48,000.00, Ano: 2017',
                'C4 Cactus, Preço: R$ 69,000.00, Ano: 2018',
                'C4 Picasso, Preço: R$ 125,000.00, Ano: 2019',
                'C4, Preço: R$ 52,090.00, Ano: 2016',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            4: [
                'Argo, Preço: R$ 50,090.00, Ano: 2019',
                'Bravo, Preço: R$ 70,000.00, Ano: 2018',
                'Mobi, Preço: R$ 48,672.00, Ano: 2019',
                'Palio, Preço: R$ 29,800.00, Ano: 2015',
                'Siena, Preço: R$ 45,900.00, Ano: 2018',
                'Toro, Preço: R$ 83,900.00, Ano: 2017',
                'Uno, Preço: R$ 42,900.00, Ano: 2017',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            5: [
                'Ka, Preço: R$ 53,000.00, Ano: 2019',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            6: [
                'City, Preço: R$ 63,400.00, Ano: 2017',
                'Civic, Preço: R$ 124,900.00, Ano: 2018',
                'Fit, Preço: R$ 65,050.00, Ano: 2016',
                'HR-V, Preço: R$ 91,500.00, Ano: 2016',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            7: [
                'Creta, Preço: R$ 77,890.00, Ano: 2019',
                'HB20, Preço: R$ 37,990.00, Ano: 2018',
                'Ix35, Preço: R$ 98,810.00, Ano: 2019',
                'I30, Preço: R$ 38,890.00, Ano: 2019',
                'Tucson, Preço: R$ 42,800.00, Ano: 2013',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            8: [
                'Pegeout 208, Preço: R$ 41,000.00, Ano: 2015',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            9: [
                'Duster, Preço: R$ 56,900.00, Ano: 2017',
                'Kwid, Preço: R$ 29,000.00, Ano: 2018',
                'Hilux, Preço: R$ 119,550.00, Ano: 2018',
                'Logan, Preço: R$ 44,690.00, Ano: 2018',
                'Sandero, Preço: R$ 40,380.00, Ano: 2017',
                'Sw4, Preço: R$ 169,700.00, Ano: 2018',
                'Yaris, Preço: R$ 74,590.00, Ano: 2018',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            10: [
                'Corolla, Preço: R$ 130,990.00, Ano: 2020',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ],
            11: [
                'Gol, Preço: R$ 45,737.00, Ano: 2016',
                'Golf, Preço: R$ 80,000.00, Ano: 2019',
                'Jetta, Preço: R$ 97,900.00, Ano: 2018',
                'Nivus, Preço: R$ 110,000.00, Ano: 2016',
                'Polo, Preço: R$ 64,636.00, Ano: 2019',
                'T-Cross, Preço: R$ 115,000.00, Ano: 2018',
                'Virtus, Preço: R$ 73,470.00, Ano: 2018',
                'Voyage, Preço: R$ 51,556.00, Ano: 2017',

                'GRAVE O PREÇO E FECHE A JANELA PARA CONTINUAR'
            ]
        }

        label_resultado.config(text="ESTES SÃO OS CARROS QUE TEMOS DISPONIVEIS:")
        for carro_info in carros_disponiveis[carro]:
            label_carros_disponiveis = tk.Label(janela, text=carro_info)
            label_carros_disponiveis.pack()

    else:
        label_resultado.config(text="Opção inválida. Tente novamente.")

    janela.update()


janela = tk.Tk()
janela.title("Escolha de Carros")


label_instrucoes = tk.Label(janela, text="SELECIONE A MARCA DO CARRO DESEJADO")
label_instrucoes.pack()

instrucoes = ["1 - AUDI", "2 - CHEVROLET", "3 - CITROËN", "4 - FIAT", "5 - FORD",
              "6 - HONDA", "7 - HYUNDAI", "8 - PEUGEOT", "9 - RENAULT", "10 - TOYOTA", "11 - VOLKSWAGEM"]
instrucoes_var = tk.StringVar(janela)
instrucoes_var.set(instrucoes[0])

instrucoes_menu = tk.OptionMenu(janela, instrucoes_var, *instrucoes)
instrucoes_menu.pack()

label_instrucoes = tk.Label(janela, text="DIGITE O NUMERO DA OPÇÃO DA MARCA SELECIONADA")
label_instrucoes.pack()

entry_carro = tk.Entry(janela)
entry_carro.pack()

button_analisar = tk.Button(janela, text="Verificar Carros Disponíveis", command=mostrar_carros)
button_analisar.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()

