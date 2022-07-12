import json
from dotenv import load_dotenv
load_dotenv()
import os
import mysql.connector as MySQL
# import MySQLdb


__all__ = ['PlanetScaleRepository']

class PlanetScaleRepository:
    def __init__(self) -> None:
        pass

    def _connection_db(self, query: str):
        connection = MySQL.connect(
            host= os.environ['HOST'],
            user= os.environ['USERNAME'],
            passwd= os.environ['PASSWORD'],
            db= os.environ['DATABASE']
        )
        db_cursor = connection.cursor()
        db_cursor.execute(query)

        tuple_response = db_cursor.fetchall()
        response = json.dumps(tuple_response)

        if response:
            return {'status': True, 'data':json.loads(response)}

        return {'status': False, 'data':response}

    def retrieve_products(self):
        return self._connection_db("SELECT * FROM products")

    def retrieve_advertisements(self):
        return self._connection_db("SELECT * FROM advertisements")

    def retrieve_recommendations(self):
        return self._connection_db("SELECT * FROM products WHERE is_recommendations= 'yes'")
    
    def retrieve_orders_by_mail(self, email:str):
        return self._connection_db("SELECT * FROM orders WHERE user_email = '" + email + "'")

    def create_pay(self, list_data):
        values = 'VALUES ('
        for data in list_data:
            if type(data) == str:
                values += '"' + data + '", '
            else:
                values += data + ', '
        values = values[0:-2]
        values += ')'
        insert_query = 'INSERT INTO orders (total, order_at, delivered_at, product_id, product_name, product_amount, product_total, user_name, user_last_name, user_email, user_phone_number, delivery_address, delivery_complementary_address, delivery_city, delivery_state, delivery_zip, payment_card_number, payment_name, payment_mm, payment_yy, payment_cvv)'
        query = insert_query + values
        return query