-- Lists all privilleges of the MySQL users user_0d_1 and user_0d_2 on server
SELECT * FROM mysql.user WHERE user IN (`user_0d_1`, `user_0d_2`)\G
