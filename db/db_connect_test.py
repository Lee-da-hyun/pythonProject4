import pymysql

try:
    conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password= '9031',
    db = 'big',
    charset= 'utf8'
)

    print('연결 성공', conn.host_info)
# except Exception as e:
#     print('Error')
#     print('에러 정보..', e)
    #연결된 통로로 sql보내기
    #2. 연결된 통로를 지정해 커서 객체 획득
    cur = conn.cursor()

    #3. sql문 보내기
    sql = "insert into book values('5', 'hi', 'http://himedia.com', '')"

    #커서로 sql문 보내기
    result = cur.execute(sql)
    print('sql분 전송 결과>>', result)

    conn.commit()
    conn.close()
except Exception as e:
    print('ad연결 중 에러발생')
    print('에러정보>>', e)
