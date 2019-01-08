import sys
from KnowledgeCreator import KnowledgeCreator
from KnowledgeBaseFile import KnowledgeBaseFile

import MeCab


def main():
    """
    コマンドライン引数で指定したディレクトリ内のファイルを読み込んで、頻出単語を表示する。
    """

    input_dir = sys.argv[1]  # コマンドラインの第1引数で、WikiExtractorの出力先のディレクトリを指定する。

    #Wikipediaの情報からナレッジベースの作成
    knowledge = KnowledgeCreator(input_dir)
    personsDict = knowledge.Create()
    #QnA Makerに食わせる用のtsvファイルを作成
    #knowledge.PrintDict(personsDict)
    basefile = KnowledgeBaseFile(personsDict)
    basefile.CreateBaseFile()

if __name__ == '__main__':
    main()
