from numpy import asarray as array, log10
class TF_IDF:
    def __init__(self, corpus):
        self.__corpus = corpus.get_corpus()
        self.__vocabulary = corpus.get_vocabulary()
        self.data = corpus.Data

    @property # funcion que calcula el TF con la formula TF(palabra) = nt/tt donde: nt es el numero de veces
    def TF(self): # que se repite el termino y tt es elnumero total de terminos.
        tf = []
        for i in range(len(self.__corpus)):
            tfe=[]
            for word in self.__vocabulary:
                tfe.append(self.data[word][f'doc{i+1}']/len(self.__corpus[i].split()))
            tf.append(tfe)
        return array(tf)
    
    @property # funcion que calcula el IDF usando la formula IDF(palabra)=log(n/wdf) donde: n es el numero de
    def IDF(self): # documentos y wdf es la cantidad de documentos en los que aparece la palabra.
        idf = []
        for text in self.__corpus:
            idfe = []
            for word in self.__vocabulary:
                n = log10((len(self.__corpus))/self.data[word]['exist in'])
                idfe.append(n)
            idf.append(idfe)
        return array(idf)
    
    @property # funcion que calcula el TF-IDF multiplicando las matrices TF e IDF, identificada como una propiedad
    def TF_IDF(self):
        return self.TF*self.IDF