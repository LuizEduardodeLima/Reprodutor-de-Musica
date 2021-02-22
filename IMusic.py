from tkinter import *
import tkinter as tk
from pygame import mixer
from PIL import Image, ImageTk
from tkinter import filedialog
import os
from tkinter import messagebox

class Tela:
    #Método construtor:
    def __init__(self, master):

        self.minhaTela = master

        #Caracteristicas da nossa interface:

        #Adicionando título a interface:
        self.minhaTela.title('Music Player Python ')

        #Adicionando o tamanho da interface - (largura x altura) -> (750 x 450):
        self.minhaTela.geometry('700x450')

        #Tornando nossa interface com tamanho fixo:
        self.minhaTela.resizable(width=0, height=0)

        #Variavél que irá guardar as musicas:
        self.play_list = []

        #Variável que vai servir de index para nossa lista:
        self.tocar = 0

        #Variável que irá guarda o status de reprodução:
        self.status = False

        #Variável de controle para o botão mudo e botão pausar:
        self.mudo_status = False
        self.pausado = False

        #Variável de controle de volume:
        mixer.init()
        self.volume = mixer.music.get_volume()

        #Variável para mostrar a musica que está reproduzindo, na tela:
        self.reproduzindo = StringVar()
        self.reproduzindo.set('Reproduzindo: ')

        #Variável para mostrar o diretorio atual:
        self.diretorio_atual = StringVar()
        self.diretorio_atual.set('Diretório Atual: ')

        # Criando Menu da janela:
        self.barra_do_menu = tk.Menu(self.minhaTela)
        self.minhaTela.config(menu=self.barra_do_menu)

        # Criando um novo Menu e adicionando a um menu já existente:
        self.sub_menu = tk.Menu(self.barra_do_menu, tearoff=0)

        self.sub_menu.add_command(label='Pasta', command=self.buscar_diretorio)

        self.barra_do_menu.add_cascade(label='Buscar', menu=self.sub_menu)


        #Criando todos os botões da aplicação:

        img_1 = Image.open('imagens/menos.png')
        self.img_menos = ImageTk.PhotoImage(img_1)
        self.lbl = tk.Button(self.minhaTela, image=self.img_menos, relief=tk.GROOVE, command=self.diminuir_volume, background='#000921')
        self.lbl.image = self.img_menos
        self.lbl.place(x=0, y=350)

        img_3 = Image.open('imagens/mudo.png')
        self.img_voltar = ImageTk.PhotoImage(img_3)
        self.btn_mudo = tk.Button(self.minhaTela, image=self.img_voltar, relief=tk.GROOVE, command=self.ativar_mudo, background='#000921')
        self.btn_mudo.image = self.img_voltar
        self.btn_mudo.place(x=100, y=350)

        img_4 = Image.open('imagens/voltar.png')
        self.img_voltar = ImageTk.PhotoImage(img_4)
        self.btn_voltar = tk.Button(self.minhaTela, image=self.img_voltar, relief=tk.GROOVE, command=self.voltar_musica, background='#000921')
        self.btn_voltar.image = self.img_voltar
        self.btn_voltar.place(x=200, y=350)

        img_5 = Image.open('imagens/passar.png')
        self.img_passar = ImageTk.PhotoImage(img_5)
        self.btn_passar = tk.Button(self.minhaTela, image=self.img_passar, relief=tk.GROOVE, command=self.passar_musica, background='#000921')
        self.btn_passar.image = self.img_passar
        self.btn_passar.place(x=300, y=350)

        img_6 = Image.open('imagens/play.png')
        self.img_play = ImageTk.PhotoImage(img_6)
        self.btn_play = tk.Button(self.minhaTela, image=self.img_play, relief=tk.GROOVE, command=self.play, background='#000921')
        self.btn_play.image = self.img_play
        self.btn_play.place(x=400, y=350)

        img_7 = Image.open('imagens/pause.png')
        self.img_pause = ImageTk.PhotoImage(img_7)
        self.btn_pause = tk.Button(self.minhaTela, image=self.img_pause, relief=tk.GROOVE, command=self.pausar_musica, background='#000921')
        self.btn_pause.image = self.img_pause
        self.btn_pause.place(x=500, y=350)

        img_8 = Image.open('imagens/stop.png')
        self.img_stop = ImageTk.PhotoImage(img_8)
        self.btn_stop = tk.Button(self.minhaTela, image=self.img_stop, relief=tk.GROOVE, command=self.stop, background='#000921')
        self.btn_stop.image = self.img_stop
        self.btn_stop.place(x=600, y=350)

        img_doguinho = Image.open('imagens/doguinho.jpg')
        self.img_doguinho = ImageTk.PhotoImage(img_doguinho)
        self.lbl_doguinho = Label(self.minhaTela, image=self.img_doguinho, relief=tk.SUNKEN, background='#000921')
        self.lbl_doguinho.image = self.img_doguinho
        self.lbl_doguinho.place(x=0, y=-120)

        img_2 = Image.open('imagens/mais.png')
        self.img_mais = ImageTk.PhotoImage(img_2)
        self.lbl = tk.Button(self.minhaTela, image=self.img_mais, relief=tk.GROOVE, command=self.aumentar_volume, background='#000921')
        self.lbl.image = self.img_mais
        self.lbl.place(x=-5, y=247)

        self.musica_atual = tk.Label(textvariable=self.reproduzindo, foreground='#000921', font='Arial 14 bold')
        self.musica_atual.place(x=10, y=10)

        self.lbl_diretorio_atual = tk.Label(textvariable=self.diretorio_atual, foreground='#000921', font='Arial 12 bold')
        self.lbl_diretorio_atual.place(x=10, y=50)

    def play(self):
        #Iniciando o mixer:
        mixer.init()
        '''Com a condição criada abaixo, o botão play perderá temporariamente sua funcionalidade durante a execução da
        musica, evitando assim que o usuário pare a execução ao apertar o botão novamente durante a reprodução'''
        if mixer.music.get_busy() == 0 and len(self.play_list) > 0:
            mixer.music.load(self.play_list[self.tocar])
            mixer.music.set_volume(0.3)
            self.volume = mixer.music.get_volume()
            mixer.music.play()
            self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])

        else:
            if mixer.music.get_busy() != 1:
                messagebox.showinfo('Aviso', 'Nenhuma musica MP3 encontrada')

    #Funcionalidades:
    def pausar_musica(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.pausado = True
        else:
            if self.pausado:
                mixer.music.unpause()

    def stop(self):
        #Parar a musica:
        if mixer.music.get_busy():
            mixer.music.stop()
            self.reproduzindo.set('Reproduzindo: Stop')
            #índice de reprodução volta ao inicio:
            self.tocar = 0

    def passar_musica(self):
        #Aumenta o índice de reprodução:
        self.tocar += 1
        #Verificando se o índice é maior que os elementos existentes na lista: play_list
        if mixer.music.get_busy():
            if self.tocar > len(self.play_list) - 1:
                #Se o índice for maior, ele volta a posição 0 e a reprodução volta ao inicio:
                self.tocar = 0
                mixer.music.load(self.play_list[self.tocar])
                self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])
                mixer.music.set_volume(0.3)
                mixer.music.play()
            else:
                #Senão ele passará a musica:
                mixer.music.load(self.play_list[self.tocar])
                self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])
                mixer.music.set_volume(0.3)
                mixer.music.play()

    def voltar_musica(self):
        #Diminui o índice de reprodução:
        self.tocar -= 1
        #Verificando se o índice é menor que 0:
        if mixer.music.get_busy():
            if self.tocar < 0:
                #Se o índice for menor, ele volta a ultima posição da nossa lista:
                self.tocar = (len(self.play_list) - 1)
                mixer.music.load(self.play_list[self.tocar])
                self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])
                mixer.music.set_volume(0.3)
                mixer.music.play()
            else:
                #Senão ele passará a musica:
                mixer.music.load(self.play_list[self.tocar])
                self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])
                mixer.music.set_volume(0.3)
                mixer.music.play()

    def ativar_mudo(self):
        if mixer.music.get_busy() and self.mudo_status == False:
            self.volume_atual = mixer.music.get_volume()
            mixer.music.set_volume(0.0)
            self.reproduzindo.set('Reproduzindo: Mudo')
            self.mudo_status = True
        else:
            if mixer.music.get_busy():
                mixer.music.set_volume(self.volume_atual)
                self.reproduzindo.set('Reproduzindo: ' + self.nome_musica[self.tocar])
                self.mudo_status = False

    def aumentar_volume(self):
        if mixer.music.get_busy():
            self.volume += 0.1
            if self.volume > 1:
                self.volume = 0.99
                mixer.music.set_volume(self.volume)
            else:
                mixer.music.set_volume(self.volume)


    def diminuir_volume(self):
        if mixer.music.get_busy():
            self.volume -= 0.1
            if self.volume < 0:
                self.volume = 0.0
                mixer.music.set_volume(self.volume)
            else:
                mixer.music.set_volume(self.volume)


    def buscar_diretorio(self):
        self.caminho = filedialog.askdirectory(title='Selecione uma Pasta')
        buscar_mp3 = os.listdir(self.caminho)
        self.play_list = []
        for x in buscar_mp3:
            if '.mp3' in x:
                self.play_list.append(self.caminho + '/' + x)
        self.diretorio_atual.set('Diretório Atual: ' + self.caminho)
        '''A playlist vai ficar com todo o caminho que o mixer deve seguir para reproduzir a muica, ex: 
        C:/Downloads/musicas/muisca.mp3 estamos criando um for dentro de outro para separar esse camiho do nome da musica
        e adicionalo a nossa nova lista chamada nome.musica, para então poder seta-la na tela'''
        self.nome_musica = []

        for x in self.play_list:
            self.a = x.split('/')
            for y in self.a:
                if '.mp3' in y:
                    self.nome_musica.append(y)

root = tk.Tk()

Tela(root)

root.mainloop()
