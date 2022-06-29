'''
Created on 28 jun 2022

@author: Miguel
'''

from collections import namedtuple
from datetime import datetime


Podcast = namedtuple("Podcast", "titulo, suscriptores, valoracion,\
                     numero_valoraciones, categoria, episodios, \
                     fecha_ultimo, gratuito, etiquetas")


def existe_podcast_gratis(podcasts, etiqueta):
    res = False
    for p in podcasts:
        if etiqueta == p.etiquetas and p.gratuito == True \
                and p.fecha_ultimo == date.today():
            res = True
            break
    return res

def num_podcasts_por_categoria(podcasts, cat):
    podcasts_categoria = [p for p in podcasts if p.categoria == cat]
    
    media = sum(p.suscriptores for p in podcasts_categoria)/len(podcasts_categoria)
    
    return len([p for p in podcasts_categoria if p.suscriptores > media])


def n_podcasts_mas_valoracion(podcasts, n, m):
    res = ((p.titulo, p.valoracion/p.numero_valoracion) for p in podcasts \
           if p.numero_valoracion > m)
    
    res = sorted(res, key = lambda t:t[1], reverse = True)
    
    return res[:n]

def lista_ordenada_por_suscriptores(podcasts):
    podcasts_ordenados = sorted(podcasts, key = lambda p:p.suscriptores, reverse = True)
    
    res = [(p1.titulo, p2.suscriptores-p2.suscriptores) for p1, 
           p2 in zip(podcasts_ordenados, podcasts_ordenados[1:])]   
    
    return res


def etiqueta_mas_comun_en_gratuitos(podcasts):
    res = dict()
    for p in podcasts:
        if p.gratuito == True:
            for e in p.etiquetas:
                if e in res:
                    res[e] += 1
                else:
                    res[e] = 1
    
    return max(res.items(), key = lambda t:t[1])[0]
        

def n_podcasts_mas_suscriptores(podcasts, n=3):
    res = dict()
    for p in podcasts:
        categoria = p.categoria
        if categoria in res:
            res[categoria].append(p)
        else:
            res[categoria] = [p]
            
    for c, l in res.items():
        lista = sorted(l, key = lambda p:p.suscriptores, reverse=True)[:n]
        res[c] = [p.titulo for p in lista]
    
    return res
        
        