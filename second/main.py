import os
import webapp2
import urllib
import json
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__)+"/templates", 'index.html')
        # self.response.write(template.render(path, template_values))
        self.response.out.write(template.render(path, template_values))

    def post(self):
		username = self.request.get("username")
		url = "https://api.github.com/users/" + username
		data=urllib.urlopen(url).read()
		data=json.loads(data)
		if ("message" in data):
			template_values = {}
			path = os.path.join(os.path.dirname(__file__)+"/templates", 'error.html')
			self.response.out.write(template.render(path, template_values))
		else:
			template_values = {
				"name":data['name'],
				"avatar":data['avatar_url']
			}			
			path = os.path.join(os.path.dirname(__file__)+"/templates", 'output.html')
			self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)