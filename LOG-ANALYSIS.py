#! /usr/bin/env python3
import psycopg2

article_query_title = ("1. The most popular three articles of all time:")
article_query = "select title,views from arview limit 3"

author_query_title = ("2. The most popular article authors of all time:")
author_query = "select * from auview"

error_query_title = ("3. More than 1% of requests lead to errors:")
error_query = "select to_char(date,'Mon DD,YYYY') as date,err_prc from "
" err_percentages where err_prc>1.0"


def connect(dbname="news"):
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        return db

    except:
        print("Error in connecting the database!!")


def article(query):
    db = connect()
    c = db.cursor()
    c.execute(query)
    res = c.fetchall()
    db.close()
    print("\n"+article_query_title+"\n")
    for i in range(0, len(res), 1):
        print("%s --> %d" % (res[i][0], res[i][1]))
    print("\n")


def author(query):
    db = connect()
    c = db.cursor()
    c.execute(query)
    res = c.fetchall()
    db.close()
    print("\n"+author_query_title+"\n")
    for i in range(0, len(res), 1):
        print("%s --> %d" % (res[i][0], res[i][1]))
        print("\n")


def error(query):
    db = connect()
    c = db.cursor()
    c.execute(query)
    res = c.fetchall()
    db.close()
    print("\n"+error_query_title+"\n")
    for i in range(0, len(res), 1):
        print("%s --> %.1f %%" % (res[i][0], res[i][1]))
        print("\n")

if __name__ == "__main__":
    article(article_query)
    author(author_query)
    error(error_query)
