from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Luis', idade=40)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Soares').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Josano').first()
    pessoa.idade = '35'
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Josano').first()
    pessoa.delete()

if __name__ == '__main__':
    exclui_pessoa()
    consulta_pessoas()
    #insere_pessoas()
    #altera_pessoa()