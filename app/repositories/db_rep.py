from .repository import Repo
from domains import Post
import logging


class DB(Repo):

    def last_post(self, source):
        logging.debug(f'DB: get last post from {source}')
        cur = self.connect.cursor()
        for row in cur.execute(f"SELECT * FROM posts where source = '{source}' order by id DESC Limit 1"):
            print(row)
            return Post(id_post=row[0], data=row[1], source=row[2], channel_source=row[3])

        return None

    def create(self, post):
        logging.debug(f'DB: create post for {post.source}')
        cur = self.connect.cursor()
        cur.execute("INSERT INTO posts VALUES ({id_post},{data},'{source}','{channel_source}')"
                    .format(id_post=post.id_post, data=post.data, source=post.source, channel_source=post.channel_source))
        self.connect.commit()
