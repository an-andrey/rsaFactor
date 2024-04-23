import time
import math
import requests
import json
import random
from tqdm import tqdm
from sympy.ntheory.primetest import is_square
import mysql.connector


# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values
# loading variables from .env file
load_dotenv()


def insertDB(digits, time, N: str):
    cnx = mysql.connector.connect(
        user=os.getenv('DB_USER'), password=os.getenv("DB_PWD"), host='sql.freedb.tech', database='freedb_rsaFactor')

    cursor = cnx.cursor()
    cursor.execute(
        f"INSERT INTO trialErrorFactor(digits,times,number) VALUES ({digits}, {time},{N});")

    cnx.commit()
    cursor.close()
    cnx.close()


def rsaFactor(n):
    for i in tqdm(range(3, int(math.sqrt(n))+1, 2), desc='factoring...'):
        if n % i == 0:
            return True


def fermatFactor(n):
    a = math.ceil((n)**0.5)  # compute a
    b_sq = a ** 2 - n  # compute b sqaure

    while not is_square(b_sq):
        a += 1  # increasing a
        b_sq = a ** 2 - n  # recompute b sqaure


primes = []
minDigit = 5
for d in range(minDigit, 12):
    res = requests.get(
        f"https://big-primes.ue.r.appspot.com/primes?digits={d}&numPrimes=6")
    pList = json.loads(res.text)['Primes']
    for p in range(len(pList)):
        pList[p] = int(pList[p])
    primes.append(pList)

for digits in range(12, 13):
    for i in range(2):
        p1 = math.floor(digits/2)
        p2 = digits - p1
        pq = random.choice(primes[p1-minDigit]) * \
            random.choice(primes[p2-minDigit])
        digitLen = int(len(str(pq)))
        print('digits:', digitLen, "number:", pq)
        start = time.time()
        rsaFactor(pq)
        end = time.time()
        factorTime = end - start
        insertDB(digitLen, factorTime, str(pq))
        print('inserted into DB successfully')
