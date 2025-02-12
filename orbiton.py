def eh_n(n):
    '''
    eh_n: int -> booleano           
    Verifica se o número fornecido está no intervalo de orbitas válidas (2-5).
    '''
    return type(n) == int and 2<=n<=5


    #TAD posição
#Construtores 

def cria_posicao(col: str, lin: int):
    '''
    cria_posicao: str x int -> posicao          
    recebe uma cadeia de caracteres que corresponde a uma coluna e um inteiro que corresponde a uma linha e devolve uma posição correspondente
    '''

    if not(type(col) == str and type(lin) == int and col in ('a','b','c','d','e','f','g','h','i','j') and 1<= lin <= 10):
        raise ValueError('cria_posicao: argumentos invalidos')
    return (col, lin)


#Seletores

def obtem_pos_col(p):
    '''
    obtem_pos_col: posicao -> str         
    Devolve a coluna associada à posição p.
    '''

    return p[0]

def obtem_pos_lin(p):
    '''
    obtem_pos_lin: posicao -> int       
    Devolve a linha associada à posição p.
    '''

    return p[1]



#Reconhecedor
def eh_posicao(arg):
    '''
    eh_posicao: universal -> booleano        
    Verifica se o argumento dado corresponde a uma posição válida no tabuleiro.
    '''

    return type(arg) == tuple and len(arg) == 2 and type(arg[0])==str and type(arg[1])==int and arg[0] in 'abcdefghij' and 0<arg[1]<=10


#Testes
def posicoes_iguais(p1, p2):
    '''
    posicoes_iguais: universal x universal -> booleano
    Verifica se duas posições são iguais.
    '''

    return eh_posicao(p1) and eh_posicao(p2) and obtem_pos_col(p1) == obtem_pos_col(p2) and obtem_pos_lin(p1) == obtem_pos_lin(p2) 


#Transformadores
def posicao_para_str(p):
    '''
    posicao_para_str: posicao -> str
    Transforma uma posição p numa representação em string.
    '''

    return obtem_pos_col(p) + str(obtem_pos_lin(p))



def str_para_posicao(s):
    '''
    str_para_posicao: str -> posicao.
    Converte uma string numa posição válida do tabuleiro.
    '''

    return cria_posicao(s[0],int(s[1:]))




#Funcões de alto nível

def obter_colunas(n):
    '''
    obter_colunas: int -> tuplo           
    Retorna as colunas disponíveis num tabuleiro de Orbito-n.
    '''

    colunas = ('a','b','c','d','e','f','g','h','i','j')
    return colunas[:2*n]


def eh_posicao_valida(p, n):
    '''
    eh_posicao_valida: posicao x int -> booleano             
    Verifica se a posição é valida segundo o o tamanho do tabuleiro.
    '''

    return eh_posicao(p) and obtem_pos_col(p) in obter_colunas(n) and 0 < obtem_pos_lin(p) <= n*2    



def orbita_pos(n,p):
    '''
    orbito_pos: int x posição -> int             
    Devolve a órbita onde a posição se encontra (a órbita nº 1 é a do exterior).
    '''
    col, lin = obtem_pos_col(p), obtem_pos_lin(p)
    for i in range(n):
        if obter_colunas(n)[i] == col or obter_colunas(n)[-i-1] == col or i+1 == lin or n*2-i == lin:
            return i+1     #Primeira orbita é a do exterior e ultima é a do meio



def posicoes_orbita(n,orb):
    '''
    posicoes_orbita: int x int -> tuplo                 
    Devolve um tuplo com todas as posições da orbita orb de um tabuleiro com n orbitas
    organizadas conforme a leitura do tabuleiro. 
    '''
    colunas = obter_colunas(n)
    res = ()
    for col2 in colunas[orb-1:n*2-orb+1]:
        res += (cria_posicao(col2, orb),)

    for lin in range(orb+1,n*2-orb+1):
        for col in (colunas[orb-1],colunas[-orb]):
            res += (cria_posicao(col, lin),)

    for col2 in colunas[orb-1:n*2-orb+1]:
        res += (cria_posicao(col2, n*2-orb+1),)
    return res



def posicoes_tab(n):
    '''
    posicoes_tab: int -> tuplo                    
    Devolve um tuplo com todas as posições de um tabuleiro com n orbitas de cima para baixo seguido da esquerda para a direita.    
    '''

    tab = ()
    for lin in range(1, n*2+1):
        for col in obter_colunas(n):
            tab += (cria_posicao(col, lin),)
    return tab       




def obtem_posicoes_adjacentes(p, n, d):
    '''
    obtem_posicoes_adjacentes: posicao x int x booleano -> tuplo           
    Devolve as posições adjacentes à posição p no tabuleiro de Orbito-n.            
    Retorna posições ortogonais se d é False; todas as posições adjacentes se d é True.
    '''
    col, lin = obtem_pos_col(p),  obtem_pos_lin(p)
    mudar_prx_coluna, mudar_ant_coluna = chr(ord(col)+1), chr(ord(col)-1)
    res = ()
    salto = 1 if d else 2
    adj = [(col,lin-1),  (mudar_prx_coluna,lin-1),             #Todas as posições adj por ordem horária
             (mudar_prx_coluna,lin),  (mudar_prx_coluna,lin+1),
             (col, lin+1),  (mudar_ant_coluna, lin+1),
             (mudar_ant_coluna, lin),  (mudar_ant_coluna, lin-1)]
    for pos in range(0,len(adj),salto):
        if adj[pos][0] in [chr(x+97) for x in range(n*2)] and 1<=adj[pos][1]<=n*2:
            res += (cria_posicao(adj[pos][0], adj[pos][1]),)
    return  res  




def ordena_posicoes(t: tuple, n):
    '''
    ordena_posicoes: tuplo x int -> tuplo          
    Ordena as posições de t de acordo com a ordem de leitura do tabuleiro de Orbito-n.
    '''
    ordenado = ()
    for orb in range(n, 0, -1):
        for pos in posicoes_orbita(n, orb):
            if pos in t:
                ordenado += (pos,)
    return ordenado




    #TAD pedra--------------------------------------------------------
#Construtor

def cria_pedra_branca():
    '''
    cria_pedra_branca: {} -> pedra          
    Cria uma pedra branca (representação interna -1).
    '''

    return -1


def cria_pedra_preta():
    '''
    cria_pedra_preta: {} -> pedra       
    Cria uma pedra preta (representação interna 1).
    '''

    return 1


def cria_pedra_neutra():
    '''
    cria_pedra_neutra: {} -> pedra      
    Cria uma pedra neutra (representação interna 0).
    '''

    return 0


#Reconhecedor
def eh_pedra(arg):
    '''
    eh_pedra: universal -> booleano
    Verifica se o argumento dado é uma pedra válida.
    '''

    return type(arg) == int and (arg == -1 or arg == 1 or arg == 0)


def eh_pedra_branca(p):
    '''
    eh_pedra_branca: pedra -> booleano          
    Verifica se a pedra p é branca.
    '''

    return p == -1

def eh_pedra_preta(p):
    '''
    eh_pedra_preta: pedra -> booleano         
    Verifica se a pedra p é preta.
    '''

    return p == 1


#Teste
def pedras_iguais(p1, p2):
    '''
    pedras_iguais: universal x universal -> booleano         
    Verifica se duas pedras são iguais.
    '''

    return p1 == p2

#Transformador
def pedra_para_str(p):
    '''pedra_para_str: pedra -> str            
    Converte uma pedra para uma string ('X' para preta, 'O' para branca, ' ' para neutra).
    '''

    if eh_pedra_preta(p):
        return 'X'
    elif eh_pedra_branca(p):
        return 'O'
    else:
        return ' '
    

#Funções de alto nível
def eh_pedra_jogador(p):
    '''
    eh_pedra_jogador: pedra -> booleano           
    Verifica se a pedra p é de um jogador (branca ou preta).
    '''

    return eh_pedra_branca(p) or eh_pedra_preta(p)


def pedra_para_int(p):
    '''
    pedra_para_int: pedra -> int       
    Converte uma pedra para um inteiro (1 para preta, -1 para branca, 0 para neutra).'''

    if eh_pedra_preta(p):
        return 1
    elif eh_pedra_branca(p):
        return -1
    else:
        return 0
    

    #TAD tabuleiro
#Construtor
def cria_tabuleiro_vazio(n):
    '''
    cria_tabuleiro_vazio: int -> tabuleiro           
    Cria um tabuleiro vazio de Orbito-n. Gera um ValueError se o número de órbitas for inválido.
    '''

    if not(eh_n(n)):
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    linha = [cria_pedra_neutra()] *n*2
    tab = []
    for _ in range(n*2):
        tab.append(linha.copy())
    return tab   #Representação do tab
    



def coordenadas(pos):
    '''
    coordenadas: posição -> tuplo       
    Devolve as coordenada de pos no tabuleiro
    '''
    return (obtem_pos_lin(pos)-1, ord(obtem_pos_col(pos))-97)




def cria_tabuleiro(n, tp, tb):
    '''
    cria_tabuleiro: int x tuplo x tuplo -> tabuleiro         
    Cria um tabuleiro com n órbitas, posicionando pedras pretas em tp e brancas em tb.          
    Verifica a validade dos argumentos, gerando ValueError se inválidos.
    '''

    if not(eh_n(n) and type(tp)==tuple and type(tb)==tuple and len(tp)==len(set(tp)) and len(tb)==len(set(tb))):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    tab = cria_tabuleiro_vazio(n)
    for pos in tp:
        if not(eh_posicao_valida(pos, n) and pos not in tb):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        idx_linha, idx_coluna = coordenadas(pos)
        tab[idx_linha][idx_coluna] = cria_pedra_preta()
    for pos in tb:
        if not(eh_posicao_valida(pos, n)):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        idx_linha, idx_coluna = coordenadas(pos)
        tab[idx_linha][idx_coluna] = cria_pedra_branca()
    return tab
        

def cria_copia_tabuleiro(t):
    '''
    cria_copia_tabuleiro: tabuleiro -> tabuleiro    
    Cria uma cópia do tabuleiro t.
    '''

    return [x.copy() for x in t]



#Seletores
def obtem_numero_orbitas(t):
    '''
    obtem_numero_orbitas: tabuleiro -> int          
    Retorna o número de órbitas do tabuleiro t.
    '''

    return len(t) // 2


def obtem_pedra(t, p):
    '''
    obtem_pedra: tabuleiro x posicao -> pedra             
    Devolve a pedra que está na posição p do tabuleiro t.              
    Se a posição está vazia, retorna uma pedra neutra.
    '''
    
    idx_linha, idx_coluna = coordenadas(p)
    if pedras_iguais(t[idx_linha][idx_coluna], cria_pedra_branca()):
        return cria_pedra_branca()
    elif pedras_iguais(t[idx_linha][idx_coluna], cria_pedra_preta()):
        return cria_pedra_preta()
    else:
        return cria_pedra_neutra()





def obtem_linha_horizontal(t, p):
    '''
    obtem_linha_horizontal: tabuleiro x posicao -> tuplo        
    Retorna todas as posições e pedras da linha horizontal que passa pela posição p.
    '''

    lin = obtem_pos_lin(p)
    idx_linha = coordenadas(p)[0]
    return tuple((cria_posicao(chr(97+x),lin), t[idx_linha][x]) for x in range(len(t[idx_linha])))





def obtem_linha_vertical(t, p):
    '''
    obtem_linha_vertical: tabuleiro x posicao -> tuplo           
    Retorna todas as posições e pedras da linha vertical que passa pela posição p.
    '''

    col = obtem_pos_col(p)
    idx_coluna = coordenadas(p)[1]
    return tuple((cria_posicao(col,lin), t[lin-1][idx_coluna]) for lin in range(1, len(t)+1))





def obtem_linhas_diagonais(t, p):
    '''
    obtem_linhas_diagonais: tabuleiro x posicao -> tuplo x tuplo          
    Retorna todas as posiçoes e pedras das linhas diagonais (principal e antidiagonal) que passam pela posição p.
    '''

    n = obtem_numero_orbitas(t)
    coluna, linha = obtem_pos_col(p), obtem_pos_lin(p)
    ate_ultima_pos_l, ate_primeira_pos_l =  n*2 - linha, linha - 1  #Calcular ultima e primeira linha
    col = obter_colunas(n)
    res_dig = ((p,obtem_pedra(t,p)),)   #Diagonal
    res_anti = ((p,obtem_pedra(t,p)),)  #Antidiagonal
    for i in range(1, ate_ultima_pos_l + 1):         #Diagonal para baixo
        if  col[-1] >= chr(ord(coluna)+i):
            pos_dig =  cria_posicao(chr(ord(coluna)+i),linha+i)
            res_dig += ((pos_dig, obtem_pedra(t,pos_dig)),)   

    for i in range(1, ate_primeira_pos_l + 1):      #Diagonal para cima
        if  col[0] < chr(ord(coluna)-i+1):
            pos_dig =  cria_posicao(chr(ord(coluna)-i),linha-i)      
            res_dig = ((pos_dig, obtem_pedra(t,pos_dig)),) + res_dig

    for i in range(1, ate_ultima_pos_l + 1):         #antiDiagonal para baixo
        if  col[0] < chr(ord(coluna)-i+1):
            pos_anti =  cria_posicao(chr(ord(coluna)-i),linha+i)
            res_anti = ((pos_anti, obtem_pedra(t,pos_anti)),) + res_anti

    for i in range(1, ate_primeira_pos_l + 1):         #antidiagonal para cima
        if  col[-1] >= chr(ord(coluna)+i):
            pos_anti = cria_posicao(chr(ord(coluna)+i),linha-i)
            res_anti += ((pos_anti, obtem_pedra(t,pos_anti)),)

    return res_dig, res_anti




def obtem_posicoes_pedra(t, j):
    '''
    obtem_posicoes_pedra: tabuleiro x pedra -> tuplo            
    Devolve todas as posições ocupadas por pedras iguais a j no tabuleiro t.            
    '''

    tuplo = ()
    for pos in posicoes_tab(obtem_numero_orbitas(t)):
        if pedras_iguais(obtem_pedra(t, pos),j):
            tuplo += (pos,)
    return ordena_posicoes(tuplo, obtem_numero_orbitas(t))




#Modificador
def coloca_pedra(t, p, j):
    '''
    coloca_pedra: tabuleiro x posicao x pedra -> tabuleiro          
    Coloca a pedra j na posição p do tabuleiro t de forma destrutiva.
    '''

    idx_linha, idx_coluna= coordenadas(p)
    t[idx_linha][idx_coluna] = j
    return t



def remove_pedra(t, p):
    '''
    remove_pedra: tabuleiro x posicao -> tabuleiro          
    Remove a pedra da posição p no tabuleiro t de forma destrutiva.
    '''

    idx_linha, idx_coluna= coordenadas(p)
    t[idx_linha][idx_coluna] = 0
    return t



#Reconhecedor
def eh_tabuleiro(arg):
    '''
    eh_tabuleiros: universal -> booleano           
    Verifica se o argumento dado é um tabuleiro válido para o jogo.
    '''

    if not (type(arg)==list and 4<= len(arg) <= 10):
        return False
    for linha in arg:
        if not(type(linha)==list and len(arg) == len(linha)):
            return False
    return True


#Testes
def tabuleiros_iguais(t1, t2):
    '''
    tabuleiros_iguais: universal x universal -> booleano             
    Verifica se dois tabuleiros são iguais.
    '''
    
    if not(eh_tabuleiro(t1) and eh_tabuleiro(t2) and len(t1) == len(t2)):
        return False
    for linha in range(len(t1)):
        for pos in range(len(t1[linha])):
            if not pedras_iguais(t1[linha][pos],t2[linha][pos]):
                return False         
    return True



#Transformador
def tabuleiro_para_str(t):
    '''
    tabuleiro_para_str: tabuleiro -> str             
    Converte o tabuleiro t para uma representação em string.
    '''

    tab_dic = {-1: 'O', 0: ' ', 1: 'X'}
    tamanho = len(t)
    tabuleiro = '    '
    for col in range(tamanho):
        tabuleiro += f'{obter_colunas(obtem_numero_orbitas(t))[col]}   '
    tabuleiro = tabuleiro[:-3] + '\n'
    for i_linha in range(len(t)):
        tabuleiro += f'0{i_linha+1} ' if i_linha < 9 else f'{i_linha+1} '
        for pos in t[i_linha]:
            tabuleiro += f'[{pedra_para_str(pos)}]'
            tabuleiro += '-'
        tabuleiro = tabuleiro[:-1]
        if i_linha != len(t) - 1:
            tabuleiro += '\n    '
            for _ in range(len(t[i_linha])):
                tabuleiro += '|   '
            tabuleiro = tabuleiro[:-3]
            tabuleiro += '\n'
    return tabuleiro




#Funcoes Auxiliares
def move_pedra(t, p1, p2):
    '''
    move_pedra: tabuleiro x posicao x posicao -> tabuleiro          
    Move a pedra da posição p1 para a posição p2 no tabuleiro t de forma destrutiva.
    '''

    t = coloca_pedra(t,p2,obtem_pedra(t,p1))
    t = remove_pedra(t,p1)
    return t



def obtem_posicao_seguinte(t, p, s):
    '''
    obtem_posicao_seguinte: tabuleiro x posicao x booleano -> posicao             
    Retorna a posição seguinte a p na mesma órbita, no sentido horário se s é True e anti-horário se False.
    '''

    n = obtem_numero_orbitas(t)
    orb_pos = orbita_pos(n,p)
    if (obtem_pos_col(p) == obter_colunas(n)[-orb_pos] and obtem_pos_lin(p)!=orb_pos) or (obtem_pos_col(p) != obter_colunas(n)[orb_pos-1] and obtem_pos_lin(p)==n*2-orb_pos+1):
        direcao = -1 if s else 0   #Caso pertença ao triangulo inferior do tabuleiro (como obtem_posicoes_adjacentes está organizada por sentido horário) vai buscar a ultima pos do tuplo criado
    else:
        direcao = 0 if s else -1   #Mesmo caso, mas com o triangulo superior
    return list(filter(lambda x: x in posicoes_orbita(n, orb_pos), obtem_posicoes_adjacentes(p,n,False)))[direcao]



def roda_tabuleiro(t):
    '''
    roda_tabuleiro: tabuleiro -> tabuleiro            
    Roda todas as pedras do tabuleiro t para a sua posição seguinte em sentido anti-horário de forma destrutiva.
    '''

    n = obtem_numero_orbitas(t)
    novo_tab = cria_copia_tabuleiro(t)
    for orb in range(1,n+1):
        orbito = posicoes_orbita(n, orb)
        pri_pos = orbito[0]
        for _ in range(len(orbito)):
            t = coloca_pedra(t, obtem_posicao_seguinte(t, pri_pos, False), obtem_pedra(novo_tab, pri_pos))
            pri_pos = obtem_posicao_seguinte(t, pri_pos, False)
    return t



def verifica_linha_pedras(t, p, j, k):
    '''
    verifica_linha_pedras: tabuleiro x posicao x pedra x int -> booleano            
    Verifica se existe uma linha com k ou mais pedras consecutivas do jogador com pedras j.
    '''

    if k <= 0:
        return True
    for linha in (obtem_linha_horizontal(t,p),obtem_linha_vertical(t,p))+obtem_linhas_diagonais(t,p):
        posicoes = [x for x in dict(linha).keys()]     #Conseguir só as posições
        idx = posicoes.index(p)
        for i in range(k):
            if sum(pedra_para_int(obtem_pedra(t,pos)) for pos in posicoes[idx-i:idx+k-i]) == k*pedra_para_int(j):
                return True
    return False



#Funcões Auxiliar--------------------------------
#2.2.1
def eh_vencedor(t,j):
    '''
    eh_vencedor: tabuleiro x pedra -> booleano           
    Verifica se o jogador com pedras j possui uma linha completa com pedra do mesmo valor.
    '''

    for pos in obtem_posicoes_pedra(t, j):
        if verifica_linha_pedras(t,pos,j,obtem_numero_orbitas(t)*2):
            return True
    return False



#2.2.2
def eh_fim_jogo(t):
    '''
    eh_fim_jogo: tabuleiro -> booleano              
    Verifica se o jogo terminou (empate ou vitória de qualquer jogador).
    '''

    for j in (cria_pedra_branca(),cria_pedra_preta()):
        if eh_vencedor(t,j):
            return True
    if len(obtem_posicoes_pedra(t,cria_pedra_neutra())) == 0:
        return True
    return False


#2.2.3
def escolhe_movimento_manual(t):
    '''
    escolhe_movimento_manual: tabuleiro -> posicao           
    Permite ao jogador escolher uma posição livre para colocar uma pedra.
    Repete o pedido até que uma posição válida seja escolhida.
    '''

    pedido = input('Escolha uma posicao livre:')
    possiveis = ()
    for pos in obtem_posicoes_pedra(t,cria_pedra_neutra()):
        possiveis += (posicao_para_str(pos),)
    while pedido not in possiveis:
        pedido = input('Escolha uma posicao livre:')
    return str_para_posicao(pedido)



#Facil
def facil(t,j):
    '''
    facil: tabuleiro x pedra -> posicao            
    Escolhe uma posição para a pedra do jogador j utilizando a estratégia "fácil".
    '''

    n = obtem_numero_orbitas(t)
    novo_t = roda_tabuleiro(cria_copia_tabuleiro(t))
    for pos in obtem_posicoes_pedra(t, cria_pedra_neutra()):
        pos_seg = obtem_posicao_seguinte(t,pos,False)
        adj = ordena_posicoes(obtem_posicoes_adjacentes(pos_seg, n, True),n)
        for pos_adj in adj:
            if pedras_iguais(j,obtem_pedra(novo_t,pos_adj)):
                return pos
    return obtem_posicoes_pedra(t,cria_pedra_neutra())[0]




#Normal
def normal(t, j):
    '''
    normal: tabuleiro x pedra -> posicao             
    Escolhe uma posição para a pedra do jogador j utilizando a estratégia "normal".
    '''

    n = obtem_numero_orbitas(t)
    marcar_k = 0
    marca_pos = ()
    outro_j = cria_pedra_preta() if pedras_iguais(j, cria_pedra_branca()) else cria_pedra_branca()
    for jogador in (j, outro_j):       #Começa por observar o caso das próprias peças e depois as do adversário
        novo_t = roda_tabuleiro(cria_copia_tabuleiro(t)) if pedras_iguais(jogador,j) else roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(t)))   
        for pos in obtem_posicoes_pedra(t,cria_pedra_neutra()):
            pos_seg = obtem_posicao_seguinte(t,pos,False) if pedras_iguais(jogador,j) else obtem_posicao_seguinte(novo_t,obtem_posicao_seguinte(t,pos,False),False)
            novo_t = coloca_pedra(novo_t, pos_seg, jogador)
            for k in range(n*2,0,-1):
                if verifica_linha_pedras(novo_t, pos_seg, jogador, k):
                    if k == n*2:
                        return pos
                    elif k > marcar_k:
                        marcar_k = k
                        marca_pos = (pos,)
                    else:
                        marca_pos += (pos,)
            novo_t = remove_pedra(novo_t, pos_seg)
    return marca_pos[0]



#2.2.4
def escolhe_movimento_auto(t,j,lvl):
    '''
    escolhe_movimento_auto: tabuleiro x pedra x str -> posicao          
    Escolhe automaticamente uma posição para a pedra do jogador j, de acordo com a estratégia lvl.
    '''

    if lvl == 'facil':
        return facil(t, j)
    elif lvl == 'normal':
        return normal(t,j)
    


def orbito(n,modo,jog):
    '''orbito: int x str x str -> int           
    Função principal para jogar uma partida de Orbito-n. Permite jogar contra o computador 
    (modos "fácil" e "normal") ou em modo "2jogadores". Devolve 1 para vitória do jogador com pedras pretas,
    -1 para o jogador com pedras brancas, ou 0 para empate.
    '''
    if not(eh_n(n) and type(modo) == str and modo in ('facil','normal','2jogadores') and type(jog)==str and jog in (pedra_para_str(cria_pedra_branca()), pedra_para_str(cria_pedra_preta()))):
        raise ValueError('orbito: argumentos invalidos')
    print(f'Bem-vindo ao ORBITO-{n}.')
    if modo in ('facil','normal'):
        print(f"Jogo contra o computador ({modo}).\nO jogador joga com '{jog}'.")
    else:
        print('Jogo para dois jogadores.')
    t = cria_tabuleiro_vazio(n)
    print(tabuleiro_para_str(t))
    jogador = cria_pedra_preta() if jog == 'X' else cria_pedra_branca()
    adversario = cria_pedra_branca() if jog == 'X' else cria_pedra_preta()
    turno = 0 if pedras_iguais(jogador, cria_pedra_preta()) else 1
    while not eh_fim_jogo(t):
        if turno % 2 == 0:
            if modo in ('facil','normal'):
                print('Turno do jogador.')
            else:
                print(f"Turno do jogador '{pedra_para_str(jogador)}'.")
            t = roda_tabuleiro(coloca_pedra(t, escolhe_movimento_manual(t), jogador))
            print(tabuleiro_para_str(t))
        else:
            if modo in ('facil','normal'):
                print(f"Turno do computador ({modo}):")
            else:
                print(f"Turno do jogador '{pedra_para_str(adversario)}'.")
            t = roda_tabuleiro(coloca_pedra(t, escolhe_movimento_auto(t, adversario,modo), adversario)) if modo in ('facil','normal') else \
                roda_tabuleiro(coloca_pedra(t, escolhe_movimento_manual(t), adversario))
            print(tabuleiro_para_str(t))
        turno += 1
    if len(obtem_posicoes_pedra(t,cria_pedra_neutra())) == 0 or (eh_vencedor(t,jogador) and eh_vencedor(t,adversario)):
        print('EMPATE')
        return 0
    elif eh_vencedor(t,jogador):
        if modo in ('facil','normal'):
            print('VITORIA')
        else:
            print(f"VITORIA DO JOGADOR '{pedra_para_str(jogador)}'")
        return pedra_para_int(jogador)  
    elif eh_vencedor(t, adversario):
        if modo in ('facil','normal'):
            print('DERROTA')
        else:
            print(f"VITORIA DO JOGADOR '{pedra_para_str(adversario)}'")
        return pedra_para_int(adversario)

