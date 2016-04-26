# -*- coding: utf-8 -*-

# this is the sq.py
# this file is used to process the sql sentences

# here we could only support mysql
# if you want to use other database to store the
# data,please change the word by yourself
import MySQLdb
import ha


# Database connect
def dbstart(db):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='zhao',
        passwd='6327742',
        db=db,
        charset='utf8'
    )
    return conn


# sql execute
def cursor(dbcn):
    cur = dbcn.cursor()
    return cur


def insert_comment_user(dbcn, cur, user_hash, comment, label, sentiment):
    try:
        sqlw = 'insert into student values(%s,%s,%s,%s)'
        cur.execute(sqlw, (user_hash, comment, label, sentiment))
        dbcn.commit()
    except Exception, e:
        return -1
    return 0


def insert_sentiment_word(dbcn, cur, table, name, attr, sent, comment):
    if (name == ''):
        return -1
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (name, attr, sent, comment))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def insert_unknown_word(dbcn, cur, table, name, attr):
    if (name == ''):
        return -1
    sqlw = 'insert into ' + table + ' values(%s,%s,0.0,\'\')'
    try:
        cur.execute(sqlw, (name, attr))
    except Exception, e:
        return -1

    dbcn.commit()
    return 0


def get_sentiment_word(dbcn, cur, table, name):
    sqlw = 'select * from ' + table + ' where name = \'' + name + '\''
    try:
        num = cur.execute(sqlw)
    except Exception, e:
        return None

    if (num == 1):
        rl = cur.fetchmany(num)
        r = rl[0]
        rname = r[0].encode('utf-8')
        rattr = r[1].encode('utf-8')
        rsent = r[2]
        rcom = r[3].encode('utf-8')
        return (rname, rattr, rsent, rcom)
    if (num == 0):
        return None
    print 'error,database'


def get_sentiment_word_attr(dbcn, cur, table, attr):
    sqlw = 'select * from ' + table + ' where attr = \'' + attr + '\''
    try:
        num = cur.execute(sqlw)
    except Exception, e:
        return None

    print num
    if (num > 1):
        rl = cur.fetchmany(num)
        rs = []
        for line in rl:
            rname = line[0].encode('utf-8')
            rattr = line[1].encode('utf-8')
            rsent = line[2]
            rcom = line[3].encode('utf-8')
            rs.append([rname, rattr, rsent, rcom])
        return rs
    if (num == 0):
        return None
    print 'error,database'


def insert_user_data(dbcn, cur, table, user_hash, item, label, sentiment):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s)'
    if (len(user_hash) > 15):
        user_hash = user_hash[0:15]
    try:
        cur.execute(sqlw, (user_hash, item, label, sentiment))
    except Exception, e:
        return -1

    dbcn.commit()
    return 0


def get_user_data(dbcn, cur, table, item):
    sqlw = 'select * from ' + table + ' where item = \'' + item + '\''
    result = []

    n = 0
    try:
        n = cur.execute(sqlw)
    except Exception, e:
        return -1

    if (n != 0):
        t = cur.fetchmany(n)
        for line in t:
            if (line != None):
                result.append(line)
        return result
    return None


def insert_item(dbcn, cur, table, name, label, pos, neg, comment):
    if (name == ''):
        return -1
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (name, label, pos, neg, comment))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def get_item(dbcn, cur, table, item):
    sqlw = 'select * from ' + table
    if (item == 'all' or item == 'ALL'):
        pass
    else:
        sqlw += ' where name = \'' + item + '\''
    result = []
    try:
        n = cur.execute(sqlw)
    except Exception, e:
        return -1

    if (n != 0):
        t = cur.fetchmany(n)
        for line in t:
            if (line != None):
                result.append(line)
        return result
    return None


def change_sent_word(dbcn, cur, table, word, com, value):
    sqlw = 'select * from ' + table + ' where name = \'' + word + '\''
    try:
        n = cur.execute(sqlw)
    except Exception, e:
        return -1

    if (n == 0):
        return -1
    sqlw = 'update ' + table + ' set '
    if (com == 'name'):
        sqlw = sqlw + ' name=' + value
    elif (com == 'attr'):
        sqlw = sqlw + ' attr=' + value
    elif (com == 'sent'):
        sqlw = sqlw + ' sent=' + value
    elif (com == 'comment'):
        sqlw = sqlw + ' comment=' + value
    else:
        return -1

    sqlw += " where name = \'" + word + '\''

    r = cur.execute(sqlw)
    dbcn.commit()

    return 0


def change_user(dbcn, cur, table, name, com, value):
    sqlw = 'select * from ' + table + ' where name = \'' + word + '\''
    try:
        n = cur.execute(sqlw)
    except Exception, e:
        return -1

    if (n == 0):
        return -1
    sqlw = 'update ' + table + ' set '
    if (com == 'name'):
        sqlw = sqlw + ' name=' + value
    elif (com == 'label'):
        sqlw = sqlw + ' label=' + value
    elif (com == 'positive'):
        sqlw = sqlw + ' positive=' + value
    elif (com == 'negative'):
        sqlw = sqlw + ' negative=' + value
    elif (com == 'comment'):
        sqlw = sqlw + ' comment=' + value
    else:
        return -1

    sqlw += " where name = \'" + word + '\''

    r = cur.execute(sqlw)
    dbcn.commit()

    return 0


def change_item(dbcn, cur, table, name, com, value):
    sqlw = 'select * from ' + table + ' where name = \'' + word + '\''
    try:
        n = cur.execute(sqlw)
    except Exception, e:
        return -1

    if (n == 0):
        return -1
    sqlw = 'update ' + table + ' set '
    if (com == 'name'):
        sqlw = sqlw + ' name=' + value
    elif (com == 'attr'):
        sqlw = sqlw + ' attr=' + value
    elif (com == 'sent'):
        sqlw = sqlw + ' attr=' + value
    elif (com == 'comment'):
        sqlw = sqlw + ' comment=' + value
    else:
        return -1

    sqlw += " where name = \'" + word + '\''
    try:
        r = cur.execute(sqlw)
    except Exception, e:
        return -1
    dbcn.commit()

    return 0


# the connection must be closed after usage
def dbstop(dbcn, dbcur):
    dbcur.close()
    dbcn.close()


def insert_item_comment(dbcn, cur, table, uid, item, com):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s)'
    try:
        cur.execute(sqlw, (uid, item, com))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0

def insert_item_comment_2(dbcn, cur, table, uid, item, com_1, com_2):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (uid, item, com_1,com_2))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0

def insert_attr(dbcn, cur, table, attribute_id, name):
    sqlw = 'insert into ' + table + ' values(%s,%s)'
    try:
        cur.execute(sqlw, (attribute_id, name))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def insert_attr_index(dbcn, cur, table, _id, attribute_id, uid, num, sent):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (_id, attribute_id, uid, num, sent))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def clear_table(dbcn, cur, table):
    sqlw = 'truncate ' + table
    try:
        cur.execute(sqlw)
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def insert_comment_attr(dbcn, cur, table,_id, attribute_name, uid, num, _bool):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (_id,attribute_name, uid, num, _bool))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0


def get_sent_word(dbcn, cur, table):
    sqlw = 'select * from ' + table
    try:
        n = cur.execute(sqlw)
        if(n != 0):
            t = cur.fetchmany(n)
    except Exception, e:
        return None
    return t

def insert_item_comment_2(dbcn, cur, table, uid, item, com,com_1, com_2):
    sqlw = 'insert into ' + table + ' values(%s,%s,%s,%s,%s)'
    try:
        cur.execute(sqlw, (uid, item, com,com_1,com_2))
    except Exception, e:
        return -1
    dbcn.commit()
    return 0