
import os
base_dir = os.path.join(os.getcwd(),)

with open("D:/Downloads/tmdb-movie-metadata/tmdb_5000_credits.csv") as f:
    lis = [line.split() for line in f]  # create a list of lists
    for i, x in enumerate(lis):  # print the list items
        print("line{0} = {1}".format(i, x))
# Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='12345',
#                              db='employee')
#
#
# cursor = connection.cursor()
# cols = "`,`".join([str(i) for i in df2.columns.tolist()])
#
# # Insert DataFrame recrds one by one.
# for i,row in df2.iterrows():
#     sql = "INSERT INTO `book_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
#     cursor.execute(sql, tuple(row))
#
#     # the connection is not autocommitted by default, so we must commit to save our changes
#     connection.commit()
#
# connection.close()
# # Create a new record
