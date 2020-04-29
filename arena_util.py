# -*- coding: utf-8 -*-
import io
import os
import json
import distutils.dir_util
from collections import Counter

import numpy as np

# Json 파일 만드는데, 특정 directory 을 만들고 그 안에 넣는다.
def write_json(data, fname):
    def _conv(o):
        if isinstance(o, np.int64):
            return int(o)
        raise TypeError

    parent = os.path.dirname(fname)
    distutils.dir_util.mkpath("./arena_data/" + parent)
    with io.open("./arena_data/" + fname, "w", encoding="utf8") as f:
        json_str = json.dumps(data, ensure_ascii=False, default=_conv)
        f.write(json_str)

# json 파일 가져오기
def load_json(fname):
    with open(fname) as f:
        json_obj = json.load(f)

    return json_obj


def debug_json(r):
    print(json.dumps(r, ensure_ascii=False, indent=4))  # 한글로 나오게 False, 그리고 indent 는 json 읽기 편하라고 해주는 거


def remove_seen(seen, l):
    seen = set(seen)
    return [x for x in l if not (x in seen)]   # seen 에 없는 l 요소 뽑기 == 중복 제거


def most_popular(playlists, col, topk_count):
    c = Counter()

    for doc in playlists:
        c.update(doc[col]) # 추가된 리스트를 누적한다!

    topk = c.most_common(topk_count)  # 가장 많이 나온 결과 값을 topk_count 만큼 뽑는다. (갯수)
    return c, [k for k, v in topk] # 노래, 개수의 Counter 와 아마 노래가 리스트로 나올 것이다.
