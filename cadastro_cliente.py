from tkinter import*
import tkinter as tk

class DadosCliente:
    
    def __init__(self, master=None):
        self.fontePadrao = ('Courier new', '12', 'bold')
        self.dados1 = Frame(master) #titulo
        self.dados1['pady'] = 20
        self.dados1.pack()
        
        self.dados2 = Frame(master) #nome cliente
        self.dados2['pady'] = 10
        self.dados2.pack()
        
        self.dados3 = Frame(master)#e-mail
        self.dados3['pady'] = 10
        self.dados3.pack()
        
        self.dados4 = Frame(master) #fone cliente
        self.dados4['pady'] = 10
        self.dados4.pack()
        
        self.dados5 = Frame(master) # endereço
        self.dados5['pady'] = 10
        self.dados5.pack()
        
        self.dados6= Frame(master) #
        self.dados6 ['pady'] = 10
        self.dados6.pack()
        
        self.dados7= Frame(master)#mensagem
        self.dados7 ['pady'] = 5
        self.dados7.pack()
       
        
           
        self.titulo = Label(self.dados1, text='Cadastro de clientes')
        self.titulo ['font'] = ('Verdana', '14','bold')
        self.titulo.pack()       
        
        self.nome_cliente = Label(self.dados2, text ='Nome:', font= self.fontePadrao)
        self.nome_cliente.pack (side= LEFT)
        
        self.inserir_nome = Entry (self.dados2)
        self.inserir_nome ['width'] = 50
        self.inserir_nome ['font'] = self.fontePadrao
        self.inserir_nome.pack (side= LEFT)
        
        self.email_cliente = Label( self.dados3, text ='E-mail:', font=self.fontePadrao)
        self.email_cliente.pack (side= LEFT)
        
          
        self.inserir_email = Entry (self.dados3)
        self.inserir_email ['width'] = 50
        self.inserir_email ['font']= self.fontePadrao
        self.inserir_email.pack (side= LEFT)
        
        self.fone_cliente = Label (self.dados4, text='Celular:', font= self.fontePadrao)
        self.fone_cliente.pack (side= LEFT)
        
                
        self.inserir_fone = Entry (self.dados4)
        self.inserir_fone['width']= 50
        self.inserir_fone['font']= self.fontePadrao
        self.inserir_fone.pack(side= LEFT)
        
        self.end_cliente = Label (self.dados5, text ='Endereço:', font= self.fontePadrao)
        self.end_cliente.pack (side= LEFT)
        
        self.inserir_end = Entry (self.dados5)
        self.inserir_end ['width']= 50
        self.inserir_end ['font']= self.fontePadrao
        self.inserir_end.pack(side= LEFT)
        
        self.mensagem = Label(self.dados7, text= 'Ola! Novo Cliente.')
        self.mensagem ['font'] = ('Verdana', '8','bold')
        self.mensagem.pack()
        
        #def mudar_mensagem():
            #self.mensagem ['text']='Cliente cadastrado'
        
        def bt_onclick1():
            print(self.inserir_nome.get(), self.inserir_email.get(), self.inserir_fone.get(), self.inserir_end.get())
                            
         
        self.btcadastrar = Button (self.dados6)
        self.btcadastrar ['text'] = 'Cadastrar Cliente'
        self.btcadastrar ['font'] = self.fontePadrao
        self.btcadastrar ['command'] = bt_onclick1
        #self.btcadastrar ['command'] = mudar_mensagem
        self.btcadastrar.pack ()
        
       
                              

janela = tk.Tk()
janela.title ('Loja de Roupas Antonia')
DadosCliente (janela)
janela.geometry ('600x400+600+400')
janela.mainloop()



