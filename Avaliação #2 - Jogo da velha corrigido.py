import tkinter as tk
from tkinter import messagebox

#Para corrigir o problema, além de diminuir o tamanho da janela, também diminuí o espaçamento entre os botões, o tamanho da fonte, a altura (height) e a largura (width) deles.

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        self.janela.geometry("400x400")
        self.janela.resizable(False, False)

        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        self.botoes = []

        frame = tk.Frame(self.janela)
        frame.pack(pady=20)

        for i in range(3):
            for j in range(3):
                botao = tk.Button(frame, text='', font=('Arial', 20, 'bold'), width=4, height=2,
                                  command=lambda row=i, col=j: self.realizar_jogada(row, col))
                botao.grid(row=i, column=j, padx=10, pady=10)
                self.botoes.append(botao)

    def realizar_jogada(self, row, col):
        if self.tabuleiro[row][col] == '':
            self.tabuleiro[row][col] = self.turno
            self.botoes[row * 3 + col].config(text=self.turno, bg=self.get_cor_jogador(self.turno))

            if self.verificar_vitoria(self.turno):
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.turno} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.alterar_turno()

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if (self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == jogador or
                    self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == jogador):
                return True

        if (self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador or
                self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador):
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento == '':
                    return False
        return True

    def alterar_turno(self):
        if self.turno == 'X':
            self.turno = 'O'
        else:
            self.turno = 'X'

    def reiniciar_jogo(self):
        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        for botao in self.botoes:
            botao.config(text='', bg='SystemButtonFace')

    def get_cor_jogador(self, jogador):
        if jogador == 'X':
            return 'blue'
        else:
            return 'red'

    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelha()
jogo.iniciar()