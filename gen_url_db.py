import pickle
import sqlite3
from contextlib import closing

from gen_wnid_dictionary import WnidDict


if __name__ == '__main__':
    dbname = 'imagenet_url.db'

    # load wnid dictionary
    with open('./wnid_vs_category.pkl', 'rb') as fin:
        wnid_dict = pickle.load(fin)
        
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = '''create table image_urls (wnid varchar(16), category varchar(32), no varchar(8), url varchar(256))'''
        c.execute(create_table)

        sql = 'insert into image_urls (wnid, category, no, url) values (?,?,?,?)'
        urls = []
        with open('./fall11_urls.txt') as fin:
            buf = fin.readline()
            while buf:
                buf = buf.rstrip().split('\t')
                wnid, no = buf[0].split('_')
                url = buf[1]
                category = wnid_dict.wnid2category[wnid]
                urls.append((wnid, category, no, url))
                buf = fin.readline()

        c.executemany(sql, urls)
        conn.commit()
