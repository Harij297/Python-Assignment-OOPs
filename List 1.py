import logging
logging.basicConfig(filename="List 1.log",level=logging.INFO,format="%(levelname)s,%(message)s,%(asctime)s")
l=[[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) ,set([23,4,5,45,4,4,5,45,45,4,5]) , {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8},["ineuron" , "data science "]]

class List:
        def ExctractList(self,v):
            '''Extract List data type alone from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                n=[]
                logging.info("Entereed data is %s",v)
                for i in v:
                    logging.info("Taken data is %s", i)
                    if type(i)==list:
                        n.append(i)
                return n
            except Exception as e:
                logging.error(e)

        def ExctractDict(self,v):
            '''Extract Dictionary data type alone from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                n=[]
                logging.info("Entereed data is %s",v)
                for i in v:
                    logging.info("Taken data is %s", i)
                    if type(i)==dict:
                        n.append(i)
                return n
            except Exception as e:
                logging.error(e)
        def ExctractTuple(self,v):
            '''Extract Tuple data type alone from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                n=[]
                logging.info("Entereed data is %s",v)
                for i in v:
                    logging.info("Taken data is %s", i)
                    if type(i)==tuple:
                        n.append(i)
                return n
            except Exception as e:
                logging.error(e)
        def ExtractNumber(self,v):
            '''Extract Number from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                a1 = []
                for i in v:
                    if type(i) ==list or type(i) == tuple:
                        for j in i:
                            if type(j) == int or type(j) == float:
                                a1.append(j)
                    elif type(i) == set:
                        c1 = list(i)
                        for j in i:
                            a1.append(j)
                return a1
            except Exception as e:
                logging.error(e)
        def SumAllNumber(self,v):
            '''Extract Sum of numbers from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                a1 = []
                b = 0
                for i in l:
                    if type(i) == list or type(i) == tuple:
                        for j in range(0, len(i)):
                            if type(i[j]) == int and type(i[j] == float):
                                a1.append(i[j])
                    elif type(i) == set:
                        c1 = list(i)
                        for j in range(0, len(i)):
                            a1.append(c1[j])
                for i in a1:
                    b = b + i
                return b
            except Exception as e:
                logging.error(e)
        def OddNumberList(self,v):
            '''Extract Odd Number from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                b1 = []
                for i in l:
                    if type(i) == list:
                        for j in range(0, len(i)):
                            if type(i[j]) == int or type(i[j]) == float:
                                if i[j] % 2 != 0:
                                    b1.append(i[j])
                return b1
            except Exception as e:
                logging.error(e)
        def IneuronOutput(self,v):
            '''Extract Ineuron from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                c1=[]
                d1=[]
                for i in l:
                    if type(i) != set and type(i) != dict:
                        for j in range(0, len(i)):
                            if i[j] == "ineuron":
                                d1.append(i[j])

                    elif type(i) == dict:
                        n = tuple(i.keys())
                        b = tuple(i.values())
                        for j in n:
                            if j=="ineuron":
                                d1.append(j)
                        for o in b:
                            if o == "ineuron":
                                d1.append(o)
                return d1
            except Exception as e:
                logging.error(e)
        def OccuranceNumber(self,v):
            '''Extract Occurrence of each item from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                b1 = []
                h1 = []
                for i in v:
                    if type(i) == list or type(i) == tuple:
                        for j in range(0, len(i)):
                            if type(i[j]) == int and type(i[j] == float):
                                b1.append(i[j])
                            if type(i[j]) == str:
                                b1.append(i[j])
                    elif type(i) == set:
                        c1 = list(i)
                        for j in range(0, len(i)):
                            b1.append(c1[j])
                    elif type(i) == dict:
                        n = tuple(i.keys())
                        b = tuple(i.values())
                        for j in n:
                            b1.append(j)
                        for o in b:
                            b1.append(o)
                for i in set(b1):
                    b = b1.count(i)
                    j=i, ":", b
                    h1.append(j)
                return h1
            except Exception as e:
                logging.error(e)
        def NumberKeys(self,v):
            '''Extract Keys from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                h1=[]
                for i in v:
                    if type(i) == dict:
                        c = list(i.keys())
                        j="No of Keys", ":", len(c)
                        h1.append(j)
                return h1
            except Exception as e:
                logging.error(e)
        def IsolateString(self,v):
            '''Extract String data from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                h1=[]
                for i in v:
                    if type(i) == list:
                        for j in range(0, len(i)):
                            if type(i[j]) == str:
                                h1.append(i[j])
                    elif type(i) == dict:
                        n = list(i.keys())
                        b = list(i.values())
                        for j in n:
                            if type(j) == str:
                                h1.append(j)
                        for o in b:
                            if type(o) == str:
                                h1.append(o)
                return h1
            except Exception as e:
                logging.error(e)
        def AlphaNumeric(self,v):
            '''To Check each item whether AlphaNumeric or not from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                b1 = []
                for i in v:
                    if type(i) == list or type(i) == tuple:
                        for j in range(0, len(i)):
                            if type(i[j]) == int and type(i[j] == float):
                                b1.append(i[j])
                            if type(i[j]) == str:
                                b1.append(i[j])
                    elif type(i) == set:
                        c1 = list(i)
                        for j in range(0, len(i)):
                            b1.append(c1[j])
                    elif type(i) == dict:
                        n = tuple(i.keys())
                        b = tuple(i.values())
                        for j in n:
                            b1.append(j)
                        for o in b:
                            b1.append(o)
                e = []
                f = []
                for i in b1:
                    c = str(i)
                    e.append(c)
                for j in range(0, len(e)):
                    x = e[j].isalnum()
                    g = e[j], ":", x
                    f.append(g)
                return f
            except Exception as e:
                logging.error(e)
        def MultiplicationIndividual(self,v):
            '''Extract Multiplication of each data from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                f = []
                k = []
                for i in v:
                    c = 1
                    if type(i) != set and type(i) != dict:
                        for j in i:
                            if type(j) == int or type(j) == float:
                                c = c * j
                        f.append(c)
                    elif type(i) == set:
                        for j in i:
                            if type(j) == int or type(j) == float:
                                c1 = list(i)
                                c = c * j
                        f.append(c)
                    elif type(i) == dict:
                        t = tuple(i.keys())
                        k = tuple(i.values())
                        for j in t:
                            if type(j) == int or type(j) == float:
                                c = c * j
                        f.append(c)
                        d = 1
                        c = 1
                        for h in k:
                            if type(h) == int or type(h) == float:
                                c = c * h
                        f.append(c)
                    r=str(i)
                    print("Multiplication of ",i, ":", c)
            except Exception as e:
                logging.error(e)
        def Unwrap(self,v):
            '''Unwrap each item from the given Input'''
            try:
                logging.info("Entered text is %s", v)
                b1 = []
                for i in v:
                    if type(i) == list or type(i) == tuple:
                        for j in range(0, len(i)):
                            if type(i[j]) == int and type(i[j] == float):
                                b1.append(i[j])
                            if type(i[j]) == str:
                                b1.append(i[j])
                    elif type(i) == set:
                        c1 = list(i)
                        for j in range(0, len(i)):
                            b1.append(c1[j])
                    elif type(i) == dict:
                        n = tuple(i.keys())
                        b = tuple(i.values())
                        for j in n:
                            b1.append(j)
                        for o in b:
                            b1.append(o)
                return b1
            except Exception as e:
                logging.error(e)

o=List()
print(o.Unwrap(l))


