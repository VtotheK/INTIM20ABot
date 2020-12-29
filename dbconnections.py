import os 
from dotenv import load_dotenv

load_dotenv()

#user    =os.getenv("TEST_USER")
#password=os.getenv("TEST_PASSWORD")
#host    =os.getenv("TEST_HOST")
#db      =os.getenv("TEST_DB")

p_user= os.getenv("PROD_USER")
p_password = os.getenv("PROD_PASSWORD")
p_host= os.getenv("PROD_HOST")
p_db= os.getenv("PROD_DB")


