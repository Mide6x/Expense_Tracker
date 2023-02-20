from deta import Deta

DETA_KEY = "a0vy4sdci48_rGQywvgrvT5qMRYYkzikUmJBeQjThDWB"

deta = Deta(DETA_KEY)

# This how to connect to or create a database.
db = deta.Base("incomeTracker")

def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})

def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found, function will return None"""
    return db.get(period)