import tornado
import template

class route(tornado.web.RequestHandler):
	def get(self):
		template.render(self, '<h1>Welcome</h1>')