from flask_script import Manager
from blog import create_app, db
from flask_migrate import Migrate, MigrateCommand
from blog.admin.register import Register

# 调用create_app创建app对象
app = create_app("development")
# 集成flask-script
manager = Manager(app)
# 创建数据库迁移命令
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)
manager.add_command('register', Register())


if __name__ == '__main__':
    manager.run()
