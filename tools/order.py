from tools.corpy import Corpy as cp
from tools.tfidf import TF_IDF as tfidf
import tools.simbycos as sc
from tools.ordenador import quicksort as qs

def busquedaordenada(query, reseñas):
    res = []
    res2 = []
    for i in range(len(reseñas)):
        res.append(reseñas[i][2])
    corp = cp(res)
    TF_IDF = tfidf(corp)
    qv = sc.queryvector(query,corp.get_vocabulary(),TF_IDF.IDF)
    tf = TF_IDF.TF_IDF
    for a in range(len(reseñas)):
        b= sc.sbc(qv,tf[a])
        if b !=0:
            res2.append([reseñas[a][0],reseñas[a][1],reseñas[a][2],reseñas[a][3],b])
    size = len(res2)
    qs(res2,0,size-1,True)
    
    return res2



