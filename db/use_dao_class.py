from db.dao import *

if __name__ == '__main__':
    dao = DAO()
    vo = input('id,name,url,img>> ')
    print(vo)
    dao.create(vo)