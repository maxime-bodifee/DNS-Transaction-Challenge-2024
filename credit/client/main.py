import page
import cherrypy
import user_cache as uc
import json


def get_user_transactions(user):
    uid, code, points = json.loads(uc.retrieve_user_data(user)).values()
    ret = f"<div><b>Account:</b> {user}</div><div><b>Points Balance:</b> {points}</div>"
    owed = 0.
    for i, transaction in enumerate(uc.retrieve_user_transactions(uid)):
        username, vendor, price, time = json.loads(transaction).values()
        date, _ = time.split()
        ret += f"<div><b>Vendor:</b> {vendor}, <b>Amount Paid:</b> ${float(price):.2f}, <b>Date:</b> {date}</div>"
        owed += float(price)
    return ret + f"<div><b>Total Owed:</b> ${owed:.2f}</div>"


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
        return page.trans_top + get_user_transactions(username) + page.trans_bot

    @cherrypy.expose
    def register(self, name, bank_id, bank_code):
      uc.store_user_data(name, json.dumps({"bank_id": bank_id, "bank_code": bank_code, "points": 0}))
      return "Registered"


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())