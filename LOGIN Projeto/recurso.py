import tkinter as tk
from tkinter import messagebox, simpledialog

class GerenciadorInventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Inventário")

        # Dicionário para armazenar recursos
        self.recursos = {
            'Equipamentos': [],
            'Veículos': [],
            'Dispositivos de Segurança': []
        }
        
        # Frame para seleção de categoria
        self.frame_categoria = tk.Frame(root)
        self.frame_categoria.pack(padx=10, pady=10)

        self.label_categoria = tk.Label(self.frame_categoria, text="Categoria:")
        self.label_categoria.pack(side=tk.LEFT)

        self.categoria_var = tk.StringVar(value='Equipamentos')
        self.categoria_menu = tk.OptionMenu(self.frame_categoria, self.categoria_var, *self.recursos.keys())
        self.categoria_menu.pack(side=tk.LEFT)

        # Frame para campo de entrada e botões
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(padx=10, pady=10)

        self.label_recurso = tk.Label(self.frame_entrada, text="Nome do Recurso:")
        self.label_recurso.pack(side=tk.LEFT)

        self.entrada_recurso = tk.Entry(self.frame_entrada, width=30)
        self.entrada_recurso.pack(side=tk.LEFT, padx=5)

        self.botao_adicionar = tk.Button(self.frame_entrada, text="Adicionar", command=self.adicionar_recurso)
        self.botao_adicionar.pack(side=tk.LEFT)

        self.botao_atualizar = tk.Button(self.frame_entrada, text="Atualizar", command=self.atualizar_recurso)
        self.botao_atualizar.pack(side=tk.LEFT, padx=5)

        self.botao_remover = tk.Button(self.frame_entrada, text="Remover", command=self.remover_recurso)
        self.botao_remover.pack(side=tk.LEFT)

        # Lista para exibir os recursos
        self.lista_recursos = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.lista_recursos.pack(padx=10, pady=10)

        # Atualiza a lista inicial
        self.atualizar_lista()

        # Atualiza a lista quando a categoria muda
        self.categoria_var.trace('w', lambda *args: self.atualizar_lista())

    def obter_categoria(self):
        return self.categoria_var.get()

    def adicionar_recurso(self):
        recurso = self.entrada_recurso.get()
        categoria = self.obter_categoria()
        if recurso:
            if recurso in self.recursos[categoria]:
                messagebox.showwarning("Aviso", "O recurso já está na lista!")
            else:
                self.recursos[categoria].append(recurso)
                self.atualizar_lista()
                self.entrada_recurso.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "O campo de recurso está vazio!")

    def atualizar_recurso(self):
        selecionado = self.lista_recursos.curselection()
        recurso_antigo = None
        if selecionado:
            categoria = self.obter_categoria()
            indice = selecionado[0]
            recurso_antigo = self.recursos[categoria][indice]
            novo_nome = simpledialog.askstring("Atualizar Recurso", f"Atualizar '{recurso_antigo}' para:")
            if novo_nome:
                if novo_nome in self.recursos[categoria]:
                    messagebox.showwarning("Aviso", "O novo nome já existe na lista!")
                else:
                    self.recursos[categoria][indice] = novo_nome
                    self.atualizar_lista()
            else:
                messagebox.showwarning("Aviso", "O novo nome não pode ser vazio!")
        else:
            messagebox.showwarning("Aviso", "Nenhum recurso selecionado para atualização!")

    def remover_recurso(self):
        selecionado = self.lista_recursos.curselection()
        if selecionado:
            categoria = self.obter_categoria()
            indice = selecionado[0]
            recurso_removido = self.recursos[categoria].pop(indice)
            self.atualizar_lista()
            messagebox.showinfo("Info", f"Recurso '{recurso_removido}' removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhum recurso selecionado para remoção!")

    def atualizar_lista(self):
        categoria = self.obter_categoria()
        self.lista_recursos.delete(0, tk.END)
        for recurso in self.recursos[categoria]:
            self.lista_recursos.insert(tk.END, recurso)

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorInventario(root)
    root.mainloop()
