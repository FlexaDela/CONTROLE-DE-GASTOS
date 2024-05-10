#importando sqlite
import sqlite3 as lite

#criando conexão
con = lite.connect('dados.db')

#------------------funções de inserção--------------------------
#inserir categoria
def inserir_categoria(i):
 with con:
    cur = con.cursor()
    query= "INSERT INTO Categoria(nome) VALUES (?)"
    cur.execute(query,i)

#inserir Receitas
def inserir_receita(i):
 with con:
    cur = con.cursor()
    query= "INSERT INTO Receitas(categoria,adicionado_em,valor) VALUES (?,?,?)"
    cur.execute(query,i)

#inserir Gastos
def inserir_gasto(i):
 with con:
    cur = con.cursor()
    query= "INSERT INTO Gastos(categoria,adicionado_em,valor) VALUES (?,?,?)"
    cur.execute(query,i)
#-----------------------------------------------------------------




#-----------------------funções para deletar----------------------------------
#deletar receitas
def deletar_receitas(i):
  with con:
    cur = con.cursor
    query = "DELETE FROM Receitas WHERE id=?"
    cur.execute(query,i)

#deletar Gastos
def deletar_gastos(i):
  with con:
    cur = con.cursor
    query = "DELETE FROM Gastos WHERE id=?"
    cur.execute(query,i)
#---------------------------------------------------------------------------



#-----------------------funções para ver dados----------------------------------
#Ver Categoria
lista_intens = []

with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM Categoria")
  linha = cur.fetchall()
#-------------------------------------------------------------------------------