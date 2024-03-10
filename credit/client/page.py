home = """<html>
  <head></head>
  <body>
      <a href="signin"><button action="signin" type="submit">sign in</button></a>   
      <a href="signup"><button action="signup" type="submit">sign up</button></a>
  </body>
</html>"""

signin = """<html>
  <head></head>
  <body>
    <form method="get" action="authenticate">
      <input type="text" value="Username" name="username" />
      <button type="submit">Log In</button>
    </form>
  </body>
</html>"""

signup = """<html>
  <head></head>
  <body>
    <form method="get" action="register">
      <input type="text" value="Username" name="name" />
      <input type="text" value="Bank ID" name="bank_id" />
      <input type="password" value="bank security code?" name="bank_code" />
      <button type="submit">register</button>
    </form>
  </body>
</html>"""

redir = """<html>
  <head><meta http-equiv="refresh" content="delay_time; URL=new_website_url" /></head>
  <body>
    <a>Redirecting</a>
  </body>
</html>"""

trans_top = """<html>
  <head><meta http-equiv="refresh" content="delay_time; URL=new_website_url" /></head>
  <body>"""
trans_bot = """  </body>
</html>"""