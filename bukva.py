class bukva():
    def __init__(self,tname):
        self.number=ord(tname)-1072
        self.cloud=''
        self.setcloud=set()
        pass

    def un(self, cl):#прибавляем эту букву
        self.cl=str(cl)
        self.cloud+=self.cl
        self.setcloud = set(self.cloud)
        #print(cl+' '+self.cloud)
        pass
    def delet(self, let):#отнимаем эту букву
        if len(self.cloud)>1:
            self.cloud=0
            self.setcloud = set(self.cloud).difference(set(let))
            for s in self.setcloud:
                self.cloud+=s

        pass
    def len(self):
        return len(self.cloud)
    def cloud(self):
        return self.cloud