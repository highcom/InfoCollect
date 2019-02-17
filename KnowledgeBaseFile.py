class KnowledgeBaseFile():
    def __init__(self, personsDict):
        self.personsDict = personsDict
    
    def CreateBaseFile(self):
        f = open('knowledge_data.tsv', 'w', encoding="utf-8")
        self.CreateHeader(f)
        self.CreateValue(f)
        f.close()
    
    def CreateHeader(self, f):
        f.write('Question	Answer	Source	Metadata\n')

    def CreateValue(self, f):
        for key, value in self.personsDict.items():
           for param, count in value:
               f.write('' + param + '	' + key + 'ですね' + '	' + 'Editional' + '	\n') 

    def SplitBaseFile(self):
        f = open('knowledge_data.tsv', 'r', encoding="utf-8")
        lines = f.readlines()

        fcount = 0
        linenum = 0
        sf = open('knowledgefile/knowledge_data_00.tsv', 'w', encoding="utf-8")

        for line in lines:
            linenum += 1
            #QnAMakerRegisterに食わせる時にファイルサイズを約1.5MB程度に抑える必要がある
            if not linenum % 30000:
                sf.close()
                fcount += 1
                sfname = 'knowledgefile/knowledge_data_' + str(fcount).zfill(2) + '.tsv'
                sf = open(sfname, 'w', encoding="utf-8")
                self.CreateHeader(sf)

            sf.write(line)

        sf.close()
