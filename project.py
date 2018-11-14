import psycopg2

DBNAME = "news"


def query(query):
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query)
	re = c.fetchall()
	return re
	db.close()

q1 = "What are the most popular three articles of all time ?"
q2 = "Who are the most popular article authors of all time?"
q3 = "On which days did more than 1% of requests lead to errors?"

query1 = query("select * from three_articles")

def query_1(re):
    for i in range(len(re)):
        t = re[i][0]
        v = re[i][1]
        print("\t" + "\"%s\" - %d "% (t, v) + "views")
    print("\n")

query2 = query("select * from most_popular_article")

def query_2(re):
    for i in range(len(re)):
        n = re[i][0]
        v = re[i][1]
        print("\t" + "%s - %d "% (n, v) + "views")
    print("\n")


query3 = query("select day, err_r from err_r where err_r >1;")

def query_3(re):
    for i in range(len(re)):
        d = re[i][0]
        r = re[i][1]
        print("\t" + "%s - %.1f%%"% (d, r) + " errors")
    print("\n")

print(q1)
query_1(query1)

print(q2)
query_2(query2)

print(q3)
query_3(query3)

