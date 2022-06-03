import random
import pickle

NUM_AUTHOR = 1000
NUM_TAG = 30
NUM_BGM = 100
SEED = 123456


def generate_data(total=10000):
    random.seed(SEED)
    data = []
    for i in range(total):
        author = random.randint(0, NUM_AUTHOR-1)
        tag = random.randint(0, NUM_TAG-1)
        bgm = random.randint(0, NUM_BGM-1)
        data.append([author, tag, bgm])
    fw = open("./data/data.pickle", 'wb')
    pickle.dump(data, fw)
    fw.close()


if __name__ == '__main__':
    generate_data()
