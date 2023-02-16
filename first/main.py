import webapp2

class MainPage(webapp2.RequestHandler) :
	def get(self):
		self.response.write("Hello World, I'm Sumit")
	
app = webapp2.WSGIApplication(
	[("/", MainPage)],
	debug=True
)
