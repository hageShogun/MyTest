import pickle

class ILSVRCDict:
    def __init__(self):
        self.category2idx = {}
        self.idx2category = {}

    def generate(self, fname):
        with open(fname) as fin:
            i = 0
            buf = fin.readline()
            while buf:
                category = buf.rstrip().split(',')[0].replace(' ', '_')
                self.category2idx[category] = i
                self.idx2category[i] = category
                buf = fin.readline()
                i += 1

    def save(self, fname):
        with open(fname, 'wb') as fout:
            pickle.dump(self, fout)


if __name__ == '__main__':
    # Generaete
    dict_file = './ILSVRC2012_ClassList.txt'
    dict = ILSVRCDict()
    dict.generate(dict_file)
    dict.save('./ilsvrc_category_idx_dictionary.pkl')

    ''' Load example
    with open('./ilsvrc_category_idx_dictionary.pkl', 'rb') as fin:
        dict = pickle.load(fin)
    '''


