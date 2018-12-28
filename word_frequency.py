import sys
import os
from lxml import html
from glob import glob
from collections import Counter
from CreateKnowledge import CreateKnowledge

import MeCab


def main():
    """
    コマンドライン引数で指定したディレクトリ内のファイルを読み込んで、頻出単語を表示する。
    """

    input_dir = sys.argv[1]  # コマンドラインの第1引数で、WikiExtractorの出力先のディレクトリを指定する。

    knowledge = CreateKnowledge(input_dir)
    knowledge.Create()

if __name__ == '__main__':
    main()
