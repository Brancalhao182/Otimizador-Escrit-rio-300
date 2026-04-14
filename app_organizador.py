import customtkinter as ctk
from tkinter import filedialog
import os
import shutil

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)

            self.btn_reuniao = ctk.CTkButton(self,text="Reunião", fg_color="blue", command=self.organizar_reuniao)
            self.btn_reuniao.grid(row=3, column=0, padx=10, pady=10)

            self.btn_urgente= ctk.CTkButton(self, text="Urgente", fg_color="red", command=self.organizar_urgente)
            self.btn_urgente.grid(row=3, column=1, padx=10, pady=10)

            self.title("Otimizador de Escritório 300%")
            self.geometry("500x350")

            self.label = ctk.CTkLabel(self, text="Organizador de Arquivos Profissional",font=("Roboto", 20))
            self.label.grid(row=0, column=0, columnspan=2, pady=5)

            self.btn_selecionar = ctk.CTkButton(self, text="Selecionar Pasta para Limpar",command=self.escolher_pasta)
            self.btn_selecionar.grid(row=1, column=0, columnspan=2,pady=5)

            self.caminho_label = ctk.CTkLabel(self, text="Nenhuma pasta selecionada",font=("Reboto", 12), text_color="gray")
            self.caminho_label.grid(row=2, column=0, columnspan=2, pady=5)

            self.btn_run = ctk.CTkButton(self, text="Iniciar Organização", state="disabled", fg_color="green", command=self.executar)
            self.btn_run.grid(row=4, column=0, columnspan=2, pady=20)

        def escolher_pasta(self):
            pasta = filedialog.askdirectory()
            if pasta:
                    self.caminho_label.configure(text=pasta, text_color="white")
                    self.btn_run.configure(state="normal")
                    self.pasta_selecionada = pasta

        def executar(self):
            pasta = self.pasta_selecionada
            formatos = {
                "Imagens": [".jpg", ".png", ".jpeg"],
                "Documentos": [".pdf", ".docx", ".txt"],
                "Planilhas": [".xlsx", ".csv"],
                "Videos": [".mp4", "mkv", "mov"]
            }

            for arquivo in os.listdir(pasta):
                caminho_antigo = os.path.join(pasta, arquivo)

                if os.path.isfile(caminho_antigo):
                    extensao = os.path.splitext(arquivo)[1].lower()

                    for pasta_nome, extensões_lista in formatos.items():
                        if extensao in extensões_lista:
                            nova_pasta = os.path. join(pasta, pasta_nome)
                            os.makedirs(nova_pasta, exist_ok=True)
                            shutil.move(caminho_antigo, os.path.join(nova_pasta, arquivo))
            with open(os.path.join(pasta, "historico_de_limpeza.txt"), "a") as log:
                log.write(f"Faxina completa em: {pasta}\n")
                log.write("-" * 30 + "\n") 

            self.label.configure(text="Pasta Organizada 300%!", text_color="green")
        def organizar_reuniao(self):
            if hasatrr(self, 'pasta_selecionada'):
                pasta_reuniao = os.path.join(self.pasta_selecionada, "REUNIAO")
                os.makedirs(pasta_reuniao, exist_ok=True)
                self.label.configure(text="Pasta de Reunião Pronta!", text_color="blue")
            else:
                self.label.configure(text="selecione uma pasta primeiro", text_color="yellow")

        def organizar_urgente(self):
            if hasattr(self, 'pasta_selecionada'):
                pasta_urgente = os.path.join(self.pasta_selecionada, "URGENTE_PRIORIDADE")
                os.makedirs(pasta_urgente, exist_ok=True)
                self.label.configure(text="Área de Prioridade Criada!", text_color="red")
            else:
                self.label.configure(text="Selecione uma pasta primeiro!", text_color="yellow")        


if __name__=="__main__":
    app = App()
    app.mainloop()
    
