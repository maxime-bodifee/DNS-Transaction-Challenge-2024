import page
import cherrypy
import user_cache as uc
import json
import pandas as pd


def get_user_transactions(user):
    uid, code, points = json.loads(uc.retrieve_user_data(user)).values()
    df = pd.DataFrame(columns=["Username", "Vendor", "Price", "Time"])
    for i, transaction in enumerate(uc.retrieve_user_transactions(uid)):
        username, vendor, price, time = json.loads(transaction).values()
        df.loc[i] = [username, vendor, float(price), time]
    return df


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
      return page.home

    @cherrypy.expose
    def signin(self):
      return page.signin

    @cherrypy.expose
    def signup(self):
      print("HI")
      return page.signup

    @cherrypy.expose
    def authenticate(self, username):
        return uc.retrieve_user_data(username) + "\n" + get_user_transactions(username).to_string()

    @cherrypy.expose
    def register(self, name, bank_id, bank_code):
      uc.store_user_data(name, json.dumps({"bank_id": bank_id, "bank_code": bank_code, "points": 0}))
      return "Registered"


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())