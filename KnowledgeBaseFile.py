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
