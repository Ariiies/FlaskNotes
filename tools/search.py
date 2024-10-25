from .corpy import Corpy as cp
#import DataBaseManager as dbm
from .tfidf import TF_IDF as tfidf
from .simbycos import queryvector, simbycos



#reseñas = dbm.show_all2()

class forSearch:
    def __init__(self, corpus):
        self.__corpus = corpus
        self.__ref,self.__data, self.__id, self.__date = [], [], [], []
        for item in self.__corpus:
            self.__ref.append(item[1])
            self.__data.append(item[2])
            self.__id.append(item[0])
            self.__date.append(item[3])
        self.corp =  cp(self.__data)
        self.tf_idf = tfidf(self.corp)


    def queryvector(self, query):
        return queryvector(query, self.corp.get_vocabulary(), self.tf_idf.IDF)

    def allquery(self, query):
        result = []
        for i in range(len(self.__ref)):
            result.append(simbycos(self.queryvector(query), self.tf_idf.TF_IDF[i]))
        return result

    def listOrder(self, query):
        n=0
        dic = []
        for dt in self.allquery(query):
            dic.append((self.__id[n],self.__ref[n],self.__data[n],self.__date[n],dt))
            n+=1

        ndic=[]
        for n in range(len(dic)):
            flag=0
            for par in dic:
                if par[4]>flag:
                    flag = par[4]
                
            for n2 in range(len(dic)):
                if dic[n2][4]== flag:
                    ndic.append(dic[n2])
                    dic[n2]=(-1,-1,-1,-1,-1)
        return ndic
    

#result = forSearch(reseñas)  
#datos = result.listOrder("Nolan")
#print("--- Resultados de la busqueda ---")
#for a in range(len(datos)):
#    print(f"para Nolan en el documento  {datos[a][0]} =", datos[a][1])


