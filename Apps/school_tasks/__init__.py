import os
app_name = "School tasks"
app_path = os.path.dirname(os.path.realpath(__file__))

import tornado
import template
import dataModel


def app_get(request):
	tasksTbl = dataModel.Table("School tasks")
	keyedTasks = {
		 'Organisation': []
		,'Homework': []
		,'Assessment task': []
		,'Study': []
	}
	for task in tasksTbl.dataset.rows:
		keyedTasks[str(task.cell("Type"))].append(task)
		
	code = tornado.template.Loader(app_path).load("view.html").generate(keyedTasks = keyedTasks)
	template.render(request, code)