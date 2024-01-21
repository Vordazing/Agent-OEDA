import psycopg2

connection = psycopg2.connect(
        user="lord",
        password="123456789",
        host="80.87.110.141",
        port="5432",
        database="umc"
    )