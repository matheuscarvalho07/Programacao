import tkinter as tk
import time

#O erro estava na linha 47, porque o ChatGPT colocou o comando "self.root.after(1000, self.atualizar_cronometro)" dentro do if, e ao retirá-lo de dentro do if, 
#o cronômetro volta a atualizar, assim ele funciona.

class Cronometro:
    def init(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.root.geometry("300x200")

        self.lbl_tempo = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.lbl_tempo.pack(pady=20)

        self.btn_iniciar = tk.Button(root, text="Iniciar", command=self.iniciar_cronometro)
        self.btn_iniciar.pack(pady=10)

        self.btn_parar = tk.Button(root, text="Parar", state=tk.DISABLED, command=self.parar_cronometro)
        self.btn_parar.pack(pady=10)

        self.tempo_inicial = 0
        self.cronometro_ligado = False

    def iniciar_cronometro(self):
        if not self.cronometro_ligado:
            self.tempo_inicial = time.time()
            self.atualizar_cronometro()

            self.btn_iniciar.config(state=tk.DISABLED)
            self.btn_parar.config(state=tk.NORMAL)
            self.cronometro_ligado = True

    def parar_cronometro(self):
        if self.cronometro_ligado:
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_parar.config(state=tk.DISABLED)
            self.cronometro_ligado = False

    def atualizar_cronometro(self):
        if self.cronometro_ligado:
            tempo_passado = int(time.time() - self.tempo_inicial)
            horas = tempo_passado // 3600
            minutos = (tempo_passado % 3600) // 60
            segundos = (tempo_passado % 3600) % 60
            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            self.lbl_tempo.config(text=tempo_formatado)

        self.root.after(1000, self.atualizar_cronometro)

root = tk.Tk()
cronometro = Cronometro()
root.mainloop()