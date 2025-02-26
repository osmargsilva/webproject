import psycopg2 as psq

class Conn:
  def db_connect(self):
    conn = psq.connect(
      database = "railway",
      user = "postgres",
      host= 'hopper.proxy.rlwy.net',
      password = "ggPYRUBWzRtYpENoTiIgejysFXGVKORW",
      port = 46636
    )
    return conn