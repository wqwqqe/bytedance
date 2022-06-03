import pickle
import random
import time

from regex import B

fr = open("./data/data.pickle", 'rb')
DATA = pickle.load(fr)
fr.close()
SEED = 123456
random.seed(SEED)

AUTHOR_LIMIT = 2
TAG_LIMIT = 3
BGM_LIMIT = 1
ITEM_LIST_LENGTH = 20
WINDOW_SIZE = 8
NUM_AUTHOR = 1000
NUM_TAG = 30
NUM_BGM = 100
LIST_LENGTH = 20


def check(item_list: list) -> int:
    """
    检查生成的列表是否符合要求
    """
    author = {}
    tag = {}
    bgm = {}
    for i in range(WINDOW_SIZE):
        author[item_list[i][0]] = author.get(item_list[i][0], 0)+1
        if author[item_list[i][0]] > AUTHOR_LIMIT:
            return 1
        tag[item_list[i][1]] = tag.get(item_list[i][1], 0)+1
        if tag[item_list[i][1]] > TAG_LIMIT:
            return 2
        bgm[item_list[i][2]] = bgm.get(item_list[i][2], 0)+1
        if bgm[item_list[i][2]] > BGM_LIMIT:
            return 3
    for i in range(WINDOW_SIZE, ITEM_LIST_LENGTH):
        author[item_list[i-WINDOW_SIZE][0]] -= 1
        tag[item_list[i-WINDOW_SIZE][1]] -= 1
        bgm[item_list[i-WINDOW_SIZE][2]] -= 1
        author[item_list[i][0]] = author.get(item_list[i][0], 0)+1
        if author[item_list[i][0]] > AUTHOR_LIMIT:
            return 1
        tag[item_list[i][1]] = tag.get(item_list[i][1], 0)+1
        if tag[item_list[i][1]] > TAG_LIMIT:
            return 2
        bgm[item_list[i][2]] = bgm.get(item_list[i][2], 0)+1
        if bgm[item_list[i][2]] > BGM_LIMIT:
            return 3
    return 4


def random_generate(epoch=10000):
    cnt = 0
    author_fail = 0
    tag_fail = 0
    bgm_fail = 0
    for i in range(epoch):
        item_list = random.sample(DATA, LIST_LENGTH)
        status = check(item_list)
        if status == 4:
            cnt += 1
        elif status == 1:
            author_fail += 1
        elif status == 2:
            tag_fail += 1
        elif status == 3:
            bgm_fail += 1
    print(cnt/epoch)
    print(1-author_fail/epoch)
    print(1-tag_fail/epoch)
    print(1-bgm_fail/epoch)


def limit_bgm(epoch=10000):
    bgm_to_id = []
    cnt = 0
    author_fail = 0
    tag_fail = 0
    bgm_fail = 0

    for i in range(NUM_BGM):
        bgm_to_id.append([])
    for i in range(len(DATA)):
        bgm_to_id[DATA[i][2]].append(i)
    for i in range(epoch):
        bgm = list(range(0, NUM_BGM))
        bgm_list = random.sample(range(0, NUM_BGM), WINDOW_SIZE)
        for num in bgm_list:
            bgm.remove(num)
        for j in range(WINDOW_SIZE, LIST_LENGTH):
            bgm.append(bgm_list[j-WINDOW_SIZE])
            random_index = random.randint(0, len(bgm)-1)
            bgm_list.append(bgm[random_index])
            del bgm[random_index]
        item_list = []
        visit = set()
        for num in bgm_list:
            item_id = bgm_to_id[num][random.randint(0, len(bgm_to_id[num])-1)]
            while item_id in visit:
                item_id = bgm_to_id[random.randint(0, len(bgm_to_id[num])-1)]
                visit.add(item_id)
            item_list.append(DATA[item_id])
        status = check(item_list)
        if status == 4:
            cnt += 1
        elif status == 1:
            author_fail += 1
        elif status == 2:
            tag_fail += 1
        elif status == 3:
            # print(bgm)
            bgm_fail += 1
    print(cnt/epoch)
    print(1-author_fail/epoch)
    print(1-tag_fail/epoch)
    print(1-bgm_fail/epoch)


if __name__ == '__main__':
    now = time.time()
    limit_bgm()
    print(time.time()-now)
