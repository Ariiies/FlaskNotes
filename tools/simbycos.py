from numpy import asarray as array, dot, linalg as norm 

#(Vector of a Query) funcion que vectoriza una consulta(query) multiplicando la frecuencia de la palabra
# en el query entre la logngitud de este por el IDF de la palabra en el corpus, recibe la consulta como parametro (string)
def queryvector(query, vocabulary, idf): 
    nq = []
    bow = {}
    for word in query.split():
        if word in bow: bow[word] = bow[word] + 1
        else: bow[word] = 1
    for ele in vocabulary:
        if ele in bow: nq.append(bow[ele]/len(query.split()))
        else: nq.append(0)
    return array(nq*idf[0])  

# (Similitud By Cosene)
def simbycos(vector1, vector2): # funcion que calcula la simitud por cosenos de 2 vectores, recibe como parametro 2 listas (list, array) de valores de igual longitud
    return dot(vector1, vector2)/(norm.norm(vector1)*norm.norm(vector2))    

def simbycos2(vector1, vector2): # funcion que calcula la simitud por cosenos de 2 vectores, recibe como parametro 2 listas (list, array) de valores de igual longitud
    try: 
        result = dot(vector1, vector2)/(norm.norm(vector1)*norm.norm(vector2)) 
    except Exception as e:
        return None
    return result

def sbc(A,B):
    pp, ma, mb = dot(A, B), norm.norm(A), norm.norm(B)   
    if pp == 0.0:
        return 0.0
    sc = pp / (ma * mb) 
    return sc


# para copiar la data con una referencia nueva # recibe la data y un array con las referencias nuevas
def new_reference(data,refrence):
    result={}
    cont_keys, cont_cont, value, values, keys2 = [], [], [], [],[]
    for items in data.items():
        cont_keys.append(items[0])
        cont_cont.append(items[1])
        keys2=[]
        for keys in items[1].keys():
            keys2.append(keys)
    for cont in cont_cont:
        value=[]
        for cont in cont.values():
            value.append(cont)
        values.append(value)
        
    for i in range(len(cont_keys)):
        result[cont_keys[i]]={}
        for a in range(len(keys2)):
            if keys2[a] == f'doc{a+1}':
                result[cont_keys[i]].update({refrence[a]:values[i][a]})
            else:
                result[cont_keys[i]].update({keys2[a]:values[i][a]})
    return result

def new_reference2(data, reference):
    result = {}
    c = 0
    for ele in data.items():
        if ele[0] == f"doc{c+1}":
            result[reference[c]] = {}
            result[reference[c]].update(ele[1])
            c+=1
        else:
            result[ele[0]] = {}
            result[ele[0]].update(ele[1])
    return result