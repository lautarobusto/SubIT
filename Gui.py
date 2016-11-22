from tkinter import *
from tkinter import ttk
from main import *


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.initialize_user_interface()

    def initialize_user_interface(self):
        p = 2
        self.tree = ttk.Treeview(self.master, columns=("Descargas", "Descripcion"))
        self.tree.heading('#0', text='Nombre')
        self.tree.heading('#1', text='Descargas')
        self.tree.heading('#2', text='Descripcion')
        self.tree.column('#1', stretch=YES)
        self.tree.column('#2', stretch=YES)
        self.tree.column('#0', stretch=YES)

        self.title = Label(self.master, text="Titulo:")
        self.season = Label(self.master, text="Temporada (Series):", )
        self.chapter = Label(self.master, text="Capitulo (Series):", )
        self.buscar = Button(self.master, text="Buscar Subtitulo", command=self.enviar_consulta)
        self.titleEntry = Entry(self.master)
        self.seasonEntry = Entry(self.master)
        self.chapterEntry = Entry(self.master)
        self.frame_1 = Frame(self.master, width=10)
        self.frame_2 = Frame(self.master, width=10)
        self.title.grid(row=0, column=0, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.season.grid(row=1, column=0, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.chapter.grid(row=2, column=0, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.titleEntry.grid(row=0, column=2, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.seasonEntry.grid(row=1, column=2, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.chapterEntry.grid(row=2, column=2, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.buscar.grid(row=0, column=4, ipadx=p, ipady=p, padx=p, pady=p, sticky='nsew')
        self.tree.grid(row=4, columnspan=5, sticky='nsew', ipadx=p, ipady=p, padx=p, pady=p)
        self.treeview = self.tree
        self.treeview.bind("<Double-1>", self.wget)

    def wget(self, event):

        for item in self.treeview.selection():
            item_text = self.treeview.item(item, "value")
            download_rar(item_text[0])

    def enviar_consulta(self):
        subtitulos = getsubs(geturl(self.titleEntry.get(), self.seasonEntry.get(), self.chapterEntry.get()))
        if self.treeview is not None:
            self.clear_tree()
        for item in subtitulos:
            self.treeview.insert('', 'end', text=item.titulo, values=(item.link, item.descripcion))

    def clear_tree(self):
        self.treeview.delete(*self.treeview.get_children())


root = Tk()
app = Application(root)
root.mainloop()
