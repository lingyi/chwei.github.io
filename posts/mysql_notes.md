# MySQL Notes

###1.How to storage file with binary mode?
with python:
> <prd><code>
>    import MySQL as mysql
>
>    data = open('myfile.bin', 'rb').read()
>    sql_cmd = 'insert into mydb.mytable (data_field) values(\'%s\')' %mysql.escape_string(data)
>    cursor.execute(sql_cmd)
></code></pre>

###2.How to concat list in mysql sql clause in python?
> 

