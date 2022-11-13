from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from main import app, db, ZBJdevice

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, ZBJdevice=ZBJdevice)

if __name__ == "__main__":
    manager.run()