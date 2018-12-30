import sys
import os
from lxml import html
from glob import glob
from collections import Counter

import MeCab

class KnowledgeCreator():
    def __init__(self, input_dir):
        self.input_dir = input_dir

    def Create(self):
        tagger = MeCab.Tagger('')
        tagger.parse('')  # parseToNode() の不具合を回避するために必要。
        personsDict = {}
        status_count = 0

        # glob()でワイルドカードにマッチするファイルのリストを取得し、マッチしたすべてのファイルを処理する。
        for path in glob(os.path.join(self.input_dir, '*', 'wiki_*')):
            print('Processing {0}...'.format(path), file=sys.stderr)

            with open(path, encoding="utf-8") as file:  # ファイルを開く。
                for title, content in self.IterDocs(file):  # ファイル内の全記事について反復処理する。
                    if self.JudgePersonName(tagger, title):
                        tokens = self.GetTokens(tagger, content)  # ページから名詞のリストを取得する。

                        # 単語の頻度を格納するCounterオブジェクトを作成する。
                        # Counterクラスはdictを継承しており、値としてキーの出現回数を保持する。
                        # Counterのupdate()メソッドにリストなどの反復可能オブジェクトを指定すると、
                        # リストに含まれる値の出現回数を一度に増やせる。
                        frequency = Counter()
                        frequency.update(tokens)
                        personsDict[title] = frequency.most_common(5)

                        status_count += 1
                        if status_count % 100 == 0:
                            print(status_count, end=" ")
        
        return personsDict
        
    def PrintDict(self, personsDict):
        for key, value in personsDict.items():
            print("-----", key, "-----")
            for param, count in value:
                print(param, end=" ")
            print('\n')

    def IterDocs(self, file):
        """
        ファイルオブジェクトを読み込んで、記事の中身（開始タグ <doc ...> と終了タグ </doc> の間のテキスト）を
        順に返すジェネレーター関数。
        """

        for line in file:
            if line.startswith('<doc '):
                buffer = []  # 開始タグが見つかったらバッファを初期化する。
                title = self.GetTitleFromHtml(line)
            elif line.startswith('</doc>'):
                # 終了タグが見つかったらバッファの中身を結合してyieldする。
                content = ''.join(buffer)
                yield title, content
            else:
                buffer.append(line)  # 開始タグ・終了タグ以外の行はバッファに追加する。

    def GetTitleFromHtml(self, line):
        """
        HTMLタグからtitleに格納されているパラメータを取得する
        """
        tokens = html.fromstring(line)
        token = tokens.attrib['title']
        return token

    def JudgePersonName(self, tagger, name):
        """
        パースした結果、単語が人名かどうか判定する
        """
        node = tagger.parseToNode(name)
        while node:
            category1, category2, category3 = node.feature.split(',')[:3]
            if category1 == '名詞' and category2 == '固有名詞' and category3 == '人名':
                return True
            node = node.next
        return False

    def GetTokens(self, tagger, content):
        """
        文書内に出現した名詞のリストを取得する関数。
        """

        tokens = []  # この記事で出現した名詞を格納するリスト。

        node = tagger.parseToNode(content)
        while node:
            # node.featureはカンマで区切られた文字列なので、split()で分割して
            # 最初の2項目をcategoryとsub_categoryに代入する。
            category, sub_category = node.feature.split(',')[:2]
            # 固有名詞または一般名詞の場合のみtokensに追加する。
            if category == '名詞' and sub_category in ('固有名詞', '一般'):
                #macの環境だとsurfaceで取れる値が単語ではなく文字列になるので修正
                #tokens.append(node.surface)
                if not node.feature.split(',')[6] == '*':
                    tokens.append(node.feature.split(',')[6])
            node = node.next

        return tokens