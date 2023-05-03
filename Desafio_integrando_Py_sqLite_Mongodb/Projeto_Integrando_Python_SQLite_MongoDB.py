from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String, BINARY, DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy import text

import pymongo
import pprint


class App:
    def __init__(self):
        """ Cria conexão com o banco sqLite """
        # Criando ta banco na memoria.
        self.engine = create_engine("sqlite:///:memory")

        # Faz conexão com o banco.
        self.metadata_obj = MetaData()

        """ Conexão com o pyMongo """
        client = pymongo.MongoClient(
            "mongodb://pymongo:Asus1@ac-uimn9pi-shard-00-00.vdqgzlu.mongodb.net:27017,ac-uimn9pi-shard-00-01.vdqgzlu.mongodb.net:27017,ac-uimn9pi-shard-00-02.vdqgzlu.mongodb.net:27017/?ssl=true&replicaSet=atlas-1t5tjv-shard-0&authSource=admin&retryWrites=true&w=majority")

        self.db = client.collection
        self.collection = self.db.cliente_contas

    def cria_tabela_cliente(self):
        """ Cria estrutura tabela cliente """
        cliente = Table("cliente", self.metadata_obj,
                        Column("id", Integer, primary_key=True),
                        Column("name", String(40), nullable=False),
                        Column("cpf", String(9)),
                        Column("endereco", String(50), nullable=False)
                        )
        # Cria tabelas.
        # Consultado dados tabela ususário
        self.metadata_obj.create_all(self.engine)

    def insere_dados_cliente(self):
        """ Inserindo dados tabela cliente """
        with self.engine.connect() as connection:
            sql_insert = text("insert into cliente values "
                              "(1, 'Antonio', '123456789', 'Rua nova Goiania-GO'),"
                              "(2, 'Guilehrme', '234567891', 'Praceta Barreiro-ST'),"
                              "(3, 'Kleiby', '456789258', 'Rua sem saida Aparecida de Goiania-GO'),"
                              "(4, 'Carlos', '147852369', 'Rua velha Anapolis-GO'),"
                              "(5, 'Chelsea', '321654987', 'Praceta alfredo keil Bareiro-ST'),"
                              "(6, 'Joao', '456820369', 'Rua Certa Jussara-GO'),"
                              "(7, 'Marcelo', '014782369', 'Rua Menor Sao Paulo-SP'),"
                              "(8, 'Abadia', '573951489', 'Rua Dupla Rio de Janeiro-RJ')"
                              )

            result = connection.execute(sql_insert)
            connection.commit()

    def manipula_dados_clliente(self):
        """ Manipulando dados tabela cliente """
        with self.engine.connect() as connection:
            # Consultado dados tabela ususário
            sql = text("select * from cliente")

            # Executando a cunsulta.
            result = connection.execute(sql)
            connection.commit()

            # Imprimindo o resultado um a um.
            for row in result:
                print(row)

    def cria_tabela_conta(self):
        """ Cria estrutura tabela conta """
        # cria estrutura tabela conta.
        conta = Table("conta", self.metadata_obj,
                      Column("id", BINARY, primary_key=True),
                      Column("tipo", String, nullable=False),
                      Column("agencia", String, nullable=False),
                      Column("num", Integer, nullable=False),
                      Column("id_cliente", Integer, ForeignKey(
                          "cliente.id"), nullable=False),
                      Column("saldo", DECIMAL)
                      )

        # Cria tabelas.
        self.metadata_obj.create_all(self.engine)

    def insere_dados_conta(self):
        """ Inserindo dados tabela conta """
        with self.engine.connect() as connection:
            sql_insert = text("insert into conta values "
                              "(1, 'corrente', '1841', 001456, 1, 1500),"
                              "(2, 'corrente', '2580', 005878, 5, 1550),"
                              "(3, 'poupanca', '1732', 000025, 3, 1600),"
                              "(4, 'corrente', '1576', 000379, 8, 1650),"
                              "(5, 'poupanca', '0947', 015870, 2, 1700),"
                              "(6, 'poupanca', '2358', 002403, 7, 1800),"
                              "(7, 'poupanca', '0701', 000041, 6, 1900),"
                              "(8, 'corrente', '1001', 000006, 4, 2000),"
                              "(9, 'corrente', '1001', 000006, 5, 2745),"
                              "(10, 'corrente', '1001', 000006, 8, 3000)"
                              )
            result = connection.execute(sql_insert)
            connection.commit()

    def manipula_dados_conta(self):
        """ Manipulando dados tabela conta """
        with self.engine.connect() as connection:
            # Consultado dados tabela ususário
            sql = text("select * from conta")

            # Executando a cunsulta.
            result = connection.execute(sql)
            connection.commit()

            # Imprimindo o resultado um a um.
            for row in result:
                print(row)

    def manipula_dados_cliente_contas(self):
        """ Manipulando dados tabelas cliente e conta """
        with self.engine.connect() as connection:
            # Consultado dados tabelas cliente e conta.
            sql = text("select cliente.id, cliente.name, cliente.cpf, "
                       "conta.tipo, conta.agencia, conta.num, conta.saldo "
                       "from cliente "
                       "inner join conta "
                       "on cliente.id = conta.id_cliente "
                       "order by cliente.name")

            # Executando a cunsulta.
            result = connection.execute(sql)
            connection.commit()

            return result

    def new_method(self, result):
        return result

    def cria_colecao_cliente_contas(self, colecao):
        post = colecao

        result = self.posts.insert_many(post)
        print(result.inserted_ids)


def main():
    """ Inicializa o sistema """
    banco = App()

    # Cliente
    banco.cria_tabela_cliente()
    banco.insere_dados_cliente()

    # Conta
    banco.cria_tabela_conta()
    banco.insere_dados_conta()

    # Cliente contas
    colecao = banco.manipula_dados_cliente_contas()

    # Insere dados na coleção um a um
    for row in colecao:
        banco.collection.insert_one(row._asdict())

    # Imprime dados coleção uma a um
    for post in banco.collection.find():
        pprint.pprint(post)


main()
