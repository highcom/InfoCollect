from config import config

class KnowledgeBaseFile():
    def __init__(self, personsDict=None):
        self.personsDict = personsDict
    
    def CreateBaseFile(self, fname):
        f = open(fname, 'w', encoding="utf-8")
        self.CreateHeader(f)
        self.CreateValue(f)
        f.close()
    
    def CreateHeader(self, f):
        f.write('Question	Answer	Source	Metadata\n')

    def CreateValue(self, f):
        for key, value in self.personsDict.items():
           for param, count in value:
               f.write('' + param + '	' + key + 'ですね' + '	' + 'Editional' + '	\n') 

    def SplitBaseFile(self, fname):
        f = open(fname, 'r', encoding="utf-8")
        lines = f.readlines()
        f.close()

        fcount = 0
        sf = open(self.GetSplitFileName(fcount), 'w', encoding="utf-8")

        linenum = 0
        for line in lines:
            linenum += 1
            #QnAMakerRegisterに食わせる時にファイルサイズを約1.5MB程度に抑える必要がある
            if not linenum % 30000:
                sf.close()
                fcount += 1
                sf = open(self.GetSplitFileName(fcount), 'w', encoding="utf-8")
                self.CreateHeader(sf)

            sf.write(line)

        sf.close()

    def GetSplitFileName(self, count):
        return config['dirname'] + '/' + config['basename'] + '_' + str(count).zfill(2) + config['format']
