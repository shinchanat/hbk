# Hyperlink-bilang-kit (hbk)
Hyperlink-bilang-kit python frontend framework.


# Example :

     from hbk.screen import Screen
     from hbk.button import Button
     from hbk.input import Input
     from hbk.htmltemplate import Html
     
     loginpage = Screen()
     loginpage.addComponent([
           Input('Username :'),
           Input('Password :'),
           Button('Login'),
     ])
     
     Html('testinghbk.html',loginpage).save()
