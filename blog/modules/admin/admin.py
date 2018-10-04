from flask import render_template
from flask_admin import AdminIndexView, expose


class IndexView(AdminIndexView):
    @expose()
    def index(self):
        return render_template("admin/index.html")