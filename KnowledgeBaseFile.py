class KnowledgeBaseFile():
    def __init__(self, personsDict):
        self.personsDict = personsDict
    
    def CreateBaseFile(self):
        f = open('knowledge_data.tsv', 'w')
        self.CreateHeader(f)
        self.CreateValue(f)
        f.close()
    
    def CreateHeader(self, f):
        f.writelines('Question	Answer	Source	Metadata\n')

    def CreateValue(self, f):
        for key, value in self.personsDict.items():
           for param, count in value:
               f.writelines('' + param + '	' + key + '	' + 'Editional\n') 
