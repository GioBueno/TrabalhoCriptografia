# -*- coding: utf-8 -*-
import hashlib
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.users


class HashCriptografico:
  def __init__(self):
      self.login = raw_input("-- Digite seu Login -- \n")
      self.senha = raw_input("-- Digite sua senha -- \n")

  def buscarUsuario(self):
    senha = self.criandoHash()
    cursor = db.users.find_one({'_id': self.login})
    valorHash = cursor['hash']
    nome = cursor['_id']
    if valorHash == senha:
        print '-- Hash validado --\n' + valorHash
        print '-- Senha Inserida --\n' + senha
    else:
        print '-- Ou ' + nome + ' senha errada --'

  def update(self):
    db.users.insert_one({"_id": self.login, "senha": self.senha, "hash": self.exibirHash(), "tamanho_hash": len(self.exibirHash())})
    print '-- Usuario Adicionado --'

  def exibirHash(self):
    hashCriado = self.criandoHash()
    return hashCriado

  def criandoHash(self):
    senha = self.senha
    hashGerado = hashlib.sha512(senha).hexdigest()
    return hashGerado

if __name__ == '__main__':
    value = raw_input('-- Para adicionar um usuario digite I ou para validar um usuaririo digite V\n-- ')
    while value == 'i':
        '-- Insira o login e senha para criar um usuario -- \n'
        gerarHash = HashCriptografico()
        gerarHash.update()
        value = raw_input('-- Para adicionar um usuario digite I ou para validar um usuaririo digite V\n-- ')
    else:
        '-- Autenticar Usuario --\n'
        gerarHash = HashCriptografico()
        gerarHash.buscarUsuario()

