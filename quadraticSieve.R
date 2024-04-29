library(gmp)
library(RcppBigIntAlgos)
library(xlsx)
library(RMySQL)
library(dotenv)

mysqlconnection <- dbConnect(RMySQL::MySQL(),
    dbname = "freedb_rsaFactor",
    host = "sql.freedb.tech",
    port = 3306,
    user = DB_USER,
    password = DB_PWD
)

for (x in 1:3) {
    primes <- nextprime(urand.bigz(2, 1000, sample(1:200, 1)))
    N <- prod(primes)
    print(primes)
    start <- Sys.time()
    quadraticSieve(N)
    end <- Sys.time()
    time <- as.numeric(difftime(end, start, units = "secs"))
    digits <- nchar(as.character(N))
    if (digits > 60) {
        N <- substr(N, 1, 60)
    }
    command <- paste("INSERT INTO quadraticSieve(digits,times,number) VALUES (", digits, ",", time, ",", N, ");")
    dbSendQuery(mysqlconnection, command)
    print("done factoring")
    print(N)
}

dbDisconnect(mysqlconnection)
