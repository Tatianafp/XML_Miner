import xml.etree.ElementTree as ET
import os
import csv
import pandas as pd
import types
import re

def create_dictAtos():
    #ATRIBUTOS GERAIS
    gerais = ['cod','documento','id', 'anotador', 'tipo']
    

    ### ABONO DE PERMANENCIA ###

    atributosAbonoPermanencia = ['Ato_Abono_Permanencia', 
                                 'nome', 
                                 'cargo_efetivo', 
                                 'matricula', 
                                 'matricula_SIAPE', 
                                 'classe', 
                                 'padrao', 
                                 'quadro',
                                 'orgao',
                                 'processo_SEI',
                                 'fundamento_legal',
                                 'vigencia']

    colunas = gerais + atributosAbonoPermanencia

    dictAbonoPermanencia = {}
    for atributo in atributosAbonoPermanencia:
        dictAbonoPermanencia[atributo] = []

    dfAbonoPermanencia = pd.DataFrame(columns = colunas)

    ### APOSENTADORIA ###

    atributosAposentadoria = ['Ato_Aposentadoria',
                              'tipo_aposentadoria',
                              'fundamento_legal',
                              'nome', 
                              'cargo_efetivo', 
                              'matricula', 
                              'matricula_SIAPE', 
                              'classe', 
                              'padrao', 
                              'quadro',
                              'orgao',
                              'vigencia',
                              'processo_SEI']

    dictAposentadoria = {}
    for atributo in atributosAposentadoria:
        dictAposentadoria[atributo] = []

    colunas = gerais + atributosAposentadoria
    dfAposentadoria = pd.DataFrame(columns = colunas)


    ### CESSÃO ###

    atributosCessao = ['Ato_Cessao',
                       'nome',
                       'matricula',
                       'matricula_SIAPE',
                       'cargo_efetivo',
                       'classe',
                       'padrao',
                       'orgao_cedente', 
                       'cargo_orgao_cessionario',
                       'simbolo',
                       'hierarquia_lotacao',
                       'orgao_cessionario',
                       'onus',
                       'fundamento_legal',
                       'processo_SEI',
                       'vigencia'
                      ]

    dictCessao = {}
    for atributo in atributosCessao:
        dictCessao[atributo] = []

    colunas = gerais + atributosCessao
    dfCessao = pd.DataFrame(columns = colunas)

    ### EXONERAÇÃO DE CARGO COMISSIONADO ###

    atributosExoneracaoComissionado = ['Ato_Exoneracao_Comissionado',
                                       'a_pedido_ou_nao',
                                       'nome', 
                                       'cargo_efetivo', 
                                       'matricula', 
                                       'matricula_SIAPE',
                                       'simbolo',
                                       'cargo_comissionado',
                                       'hierarquia_lotacao',
                                       'orgao',
                                       'vigencia',
                                       'motivo']

    dictExoneracaoComissionado = {}
    for atributo in atributosExoneracaoComissionado:
        dictExoneracaoComissionado[atributo] = []

    colunas = gerais + atributosExoneracaoComissionado
    dfExoneracaoComissionado = pd.DataFrame(columns = colunas)

    ### EXONERAÇÃO DE CARGO EFETIVO ###

    atributosExoneracaoEfetivo = ['Ato_Exoneracao_Efetivo',
                                  'nome', 
                                  'cargo_efetivo', 
                                  'matricula', 
                                  'matricula_SIAPE',
                                  'classe',
                                  'padrao',
                                  'carreira',
                                  'quadro',
                                  'orgao',
                                  'vigencia',
                                  'motivo',
                                  'fundamento_legal',
                                  'processo_SEI']

    dictExoneracaoEfetivo = {}
    for atributo in atributosExoneracaoEfetivo:
        dictExoneracaoEfetivo[atributo] = []

    colunas = gerais + atributosExoneracaoEfetivo
    dfExoneracaoEfetivo = pd.DataFrame(columns = colunas)

    ### NOMEAÇÃO DE CARGO COMISSIONADO ###

    atributosNomeacaoComissionado = ['Ato_Nomeacao_Comissionado', 
                                     'nome', 
                                     'cargo_efetivo', 
                                     'matricula', 
                                     'matricula_SIAPE', 
                                     'simbolo', 
                                     'cargo_comissionado', 
                                     'hierarquia_lotacao', 
                                     'orgao']

    dictNomeacaoComissionado = {}
    for atributo in atributosNomeacaoComissionado:
        dictNomeacaoComissionado[atributo] = []

    colunas = gerais + atributosNomeacaoComissionado
    dfNomeacaoComissionado = pd.DataFrame(columns = colunas)

    ### NOMEAÇÃO DE CARGO EFETIVO ###

    atributosNomeacaoEfetivo = ['Ato_Nomeacao_Efetivo', 
                               'processo_SEI',
                               'edital_normativo',
                               'data_edital_normativo',
                               'numero_dodf_edital_normativo',
                               'data_dodf_edital_normativo',
                               'edital_resultado_final',
                               'data_edital_resultado_final',
                               'numero_dodf_resultado_final',
                               'data_dodf_resultado_final',
                               'cargo',
                               'carreira',
                               'orgao',
                               'especialidade',
                               'candidato', 
                               'candidato_PNE'
                               ]

    dictNomeacaoEfetivo = {}
    for atributo in atributosNomeacaoEfetivo:
        dictNomeacaoEfetivo[atributo] = []

    colunas = gerais + atributosNomeacaoEfetivo
    dfNomeacaoEfetivo = pd.DataFrame(columns = colunas)

    ### RETIFICAÇÃO - APOSENTADORIA, PENSÔES E REVERSÕES ###

    atributosRetificacaoEfetivo = ['Ato_Retificacao_Efetivo',
                                   'tipo_documento',
                                   'numero_documento',
                                   'data_documento',
                                   'tipo_edicao',
                                   'numero_dodf',
                                   'data_dodf',
                                   'pagina_dodf',
                                   'tipo_ato',
                                   'nome',
                                   'matricula',
                                   'matricula_SIAPE',
                                   'cargo_efetivo',
                                   'classe',
                                   'padrao',
                                   'lotacao',
                                   'informacao_errada',
                                   'informacao_corrigida']

    dictRetificacaoEfetivo = {}
    for atributo in atributosRetificacaoEfetivo:
        dictRetificacaoEfetivo[atributo] = []

    colunas = gerais + atributosRetificacaoEfetivo
    dfRetificacaoEfetivo = pd.DataFrame(columns = colunas)

    ### RETIFICAÇÃO - EXONERAÇÃO E NOMEAÇÃO ###

    atributosRetificacaoComissionado = ['Ato_Retificacao_Comissionado',
                                        'tipo_documento',
                                        'data_documento',
                                        'tipo_edicao',
                                        'numero_dodf',
                                        'data_dodf',
                                        'pagina_dodf',
                                        'tipo_ato',
                                        'nome',
                                        'lotacao',
                                        'informacao_errada',
                                        'informacao_corrigida'
                                        ]

    dictRetificacaoComissionado = {}
    for atributo in atributosRetificacaoComissionado:
        dictRetificacaoComissionado[atributo] = []

    colunas = gerais + atributosRetificacaoComissionado
    dfRetificacaoComissionado = pd.DataFrame(columns = colunas)

    ### REVERSÃO ###

    atributosReversao = ['Ato_Reversao',
                         'nome',
                         'matricula',
                         'matricula_SIAPE',
                         'cargo_efetivo',
                         'classe',
                         'padrao',
                         'quadro',
                         'fundamento_legal',
                         'orgao',
                         'processo_SEI',
                         'vigencia']

    dictReversao = {}
    for atributo in atributosReversao:
        dictReversao[atributo] = []

    colunas = gerais + atributosReversao
    dfReversao = pd.DataFrame(columns = colunas)

    ### SUBSTITUICAO ###

    atributosSubstituicao = ['Ato_Substituicao',
                             'nome_substituto',
                             'matricula_substituto',
                             'cargo_substituto',
                             'simbolo_substituto',
                             'nome_substituido',
                             'matricula_substituido',
                             'cargo_objeto_substituicao',
                             'simbolo_objeto_substituicao',
                             'hierarquia_lotacao',
                             'orgao',
                             'motivo',
                             'data_inicial',
                             'data_final',
                             'matricula_SIAPE']

    dictSubstituicao = {}
    for atributo in atributosSubstituicao:
        dictSubstituicao[atributo] = []

    colunas = gerais + atributosSubstituicao
    dfSubstituicao = pd.DataFrame(columns = colunas)

    ### TORNADO SEM EFEITO - APOSENTADORIAS, PENSÕES E REVERSÕES ###

    atributosTornadoSemEfeitoApo = ['Ato_Tornado_Sem_Efeito_Apo',
                                'tipo_documento',
                                'numero_documento',
                                'data_documento',
                                'numero_dodf',
                                'data_dodf',
                                'pagina_dodf',
                                'nome',
                                'matricula',
                                'matricula_SIAPE',
                                'cargo_efetivo',
                                'classe',
                                'padrao',
                                'quadro',
                                'orgao',
                                'processo_SEI',
                                ]

    dictTornadoSemEfeitoApo = {}
    for atributo in atributosTornadoSemEfeitoApo:
        dictTornadoSemEfeitoApo[atributo] = []

    colunas = gerais + atributosTornadoSemEfeitoApo
    dfTornadoSemEfeitoApo = pd.DataFrame(columns = colunas)

    ### TORNADO SEM EFEITO - EXONERAÇÃO E NOMEAÇÃO ###

    atributosTornadoSemEfeitoExoNom = ['Ato_Tornado_Sem_Efeito_Exo_Nom',
                                        'tipo_documento',
                                        'data_documento',
                                        'tipo_edicao',
                                        'numero_dodf',
                                        'data_dodf',
                                        'pagina_dodf',
                                        'nome',
                                        'cargo_efetivo',
                                        'matricula',
                                        'matricula_SIAPE',
                                        'simbolo',
                                        'cargo_comissionado',
                                        'hierarquia_lotacao',
                                        'orgao']

    dictTornadoSemEfeitoExoNom = {}
    for atributo in atributosTornadoSemEfeitoExoNom:
        dictTornadoSemEfeitoExoNom[atributo] = []

    colunas = gerais + atributosTornadoSemEfeitoExoNom
    dfTornadoSemEfeitoExoNom = pd.DataFrame(columns = colunas)

    atributosTodos = ["conteudo"]
    colunas = gerais + atributosTodos
    dfTodos = pd.DataFrame(columns = colunas)    

    info_atos = {
        'Ato_Abono_Permanencia': {
            "atributos" : dictAbonoPermanencia,
            "dataframe" : dfAbonoPermanencia
        },
        'Ato_Aposentadoria': {
            "atributos" : dictAposentadoria,
            "dataframe" : dfAposentadoria
        },
        'Ato_Cessao': {
            "atributos" : dictCessao,
            "dataframe" : dfCessao
        },
        'Ato_Exoneracao_Comissionado': {
            "atributos" : dictExoneracaoComissionado,
            "dataframe" : dfExoneracaoComissionado
        },
        'Ato_Exoneracao_Efetivo': {
            "atributos" : dictExoneracaoEfetivo,
            "dataframe" : dfExoneracaoEfetivo
        },
        'Ato_Nomeacao_Comissionado': {
            "atributos" : dictNomeacaoComissionado,
            "dataframe" : dfNomeacaoComissionado
        },
        'Ato_Nomeacao_Efetivo': {
            "atributos" : dictNomeacaoEfetivo,
            "dataframe" : dfNomeacaoEfetivo
        },
        'Ato_Retificacao_Comissionado': {
            "atributos" : dictRetificacaoComissionado,
            "dataframe" : dfRetificacaoComissionado
        },
        'Ato_Retificacao_Efetivo': {
            "atributos" : dictRetificacaoEfetivo,
            "dataframe" : dfRetificacaoEfetivo
        },
        'Ato_Reversao': {
            "atributos" : dictReversao,
            "dataframe" : dfReversao
        },
        'Ato_Substituicao': {
            "atributos" : dictSubstituicao,
            "dataframe" : dfSubstituicao
        },
        'Ato_Tornado_Sem_Efeito_Apo': {
            "atributos" : dictTornadoSemEfeitoApo,
            "dataframe" : dfTornadoSemEfeitoApo
        },
        'Ato_Tornado_Sem_Efeito_Exo_Nom': {
            "atributos" : dictTornadoSemEfeitoExoNom,
            "dataframe" : dfTornadoSemEfeitoExoNom
        },
        'todos_atos': {
            "dataframe" : dfTodos
        }
    }
    
    return info_atos  

def acharConteudo(tipo, dictGeral, df,relation,paragrafo):
    #dentro de cada anotação
    conteudo = []        
            
    node_data = [] 
    for node in relation.findall('node'):
        annoId = node.get('refid')
        node_data.append(annoId)

    for i in node_data:
        for anno in paragrafo.findall('annotation'):
            if anno.get('id') == i:             
                for info in anno.findall('infon'):           
                    if info.get('key') == 'type':
                        tipoAnno = info.text
                                            
                if tipoAnno == tipo:
                    conteudo.append(anno.find('text').text)  
                    
    num1= dictGeral['id']
    num2= dictGeral['documento']
    codigo = num1+num2
    codigo = re.sub('[^0-9]', '', codigo)
    #print(codigo)
    anno_data = [] 
    anno_data.append(codigo)
    for item in dictGeral:
        escrever = dictGeral[item]
        anno_data.append(escrever)
                            
    anno_data.append(conteudo)
    
    df_length = len(df)
    df.loc[df_length] = anno_data

def acharEntidades(tipo, dictAto, dictGeral, df,relation,paragrafo):
    #dentro de cada anotação
    for entidade in dictAto:
        dictAto[entidade] = []           
            
    node_data = [] 
    for node in relation.findall('node'):
        annoId = node.get('refid')
        node_data.append(annoId)

    for i in node_data:
        for anno in paragrafo.findall('annotation'):
            if anno.get('id') == i:             
                for info in anno.findall('infon'):           
                    if info.get('key') == 'type':
                        tipoAnno = info.text
                                            
                for entidade in dictAto:
                    if tipoAnno == entidade:
                        dictAto[entidade].append(anno.find('text').text)          
                            
    num1= dictGeral['id']
    num2= dictGeral['documento']
    codigo = num1+num2
    codigo = re.sub('[^0-9]', '', codigo)

    anno_data = [] 

    anno_data.append(codigo) 

    for item in dictGeral:
        escrever = dictGeral[item]
        anno_data.append(escrever)
                            
    for item in dictAto:
        escrever = dictAto[item]
        anno_data.append(escrever)
    
    df_length = len(df)
    df.loc[df_length] = anno_data

def extrair_anotacoes(xmls,modo):   
    roots = []
    info_atos = create_dictAtos()
    dictGerais = {'documento':'x','id':'x', 'anotador':'x', 'tipo':'x'}
    
    for xml in xmls:
        tree = ET.parse(xml)
        root = tree.getroot()
        roots.append(root)
    '''
    tree = ET.parse(xml)
    root = tree.getroot()
    roots.append(root)
    '''
    for root in roots:
        for documento in root.findall('document'):
            #dentro do documento
            for idx in documento.findall('id'):
                dictGerais['documento'] = idx.text
            for paragrafo in documento.findall('passage'):
                #dentro de cada parágrafo
                for relation in paragrafo.findall('relation'):
                    #dentro de cada relacao

                    dictGerais['id'] = relation.get('id')

                    for infon in relation.findall('infon'):
                        if infon.get('key') == 'annotator':
                            dictGerais['anotador'] = infon.text  

                    for infon in relation.findall('infon'):
                        if infon.get('key') == 'type':
                            tipo = infon.text
                            dictGerais['tipo'] = infon.text   

                            if modo == "separado":
                                acharEntidades(tipo, info_atos[tipo]["atributos"], dictGerais, info_atos[tipo]["dataframe"],relation,paragrafo)
                            elif modo == "junto":
                                acharConteudo(tipo, dictGerais, info_atos["todos_atos"]["dataframe"],relation,paragrafo)

    all_dfs = {}

    if modo == "separado":
        for i in info_atos:
            all_dfs[i] = info_atos[i]["dataframe"]
    elif modo == "junto":
         all_dfs["todos_atos"] = info_atos["todos_atos"]["dataframe"]
    
    return all_dfs