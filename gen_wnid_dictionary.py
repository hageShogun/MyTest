import pickle

class WnidDict:
    def __init__(self):
        self.wnid2category = {}
        self.category2wnid = {}        

    def generate(self, fname):
        with open(fname) as fin:
            buf = fin.readline()
            while buf:
                buf = buf.rstrip().split('\t')
                wnid = buf[0]
                category = buf[1].split(',')[0].replace(' ', '_')
                self.wnid2category[wnid] = category
                self.category2wnid[category] = wnid
                buf = fin.readline()

    def save(self, fname):
        with open(fname, 'wb') as fout:
            pickle.dump(self, fout)

            
if __name__ == '__main__':
    # Generaete
    dict_file = './wnid_vs_category.dat'
    dict = WnidDict()
    dict.generate(dict_file)
    dict.save('./wnid_vs_category.pkl')
 
    ''' Load example
    with open('./wnid_vs_category.pkl', 'rb') as fin:
        dict = pickle.load(fin)
    '''


