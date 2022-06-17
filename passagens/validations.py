def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino estão iguais."""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se possui algum numero no campo."""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua numeros neste campo'

def ida_maior_que_volta(data_ida, data_volta, lista_de_erros):
    """Verifica se a data da ida é maior do que a de volta."""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor do que a data de ida'

def ida_maior_que_hoje(data_ida, data_pesquisa, lista_de_erros):
    """Verifica se a data de ida é maior que a data de hoje"""
    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que a data de hoje.'