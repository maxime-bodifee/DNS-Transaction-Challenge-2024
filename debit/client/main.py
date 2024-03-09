import page
import cherrypy
import user_cache as uc
import json

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
      return uc.retrieve_user_data(username)

    @cherrypy.expose
    def register(self, name, bank_id, bank_code):
      uc.store_user_data(name, json.dumps({"bank_id": bank_id, "bank_code": bank_code}))
      return "Registered"


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())