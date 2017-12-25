# -*- coding=utf-8 -*-
from app import create_app, db
from app.models import Marks_record, User, Question
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)  # 注册migrate到flask


def make_shell_context():
    return dict(app=app, db=db, User=User, Question=Question, Marks_record=Marks_record)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)  # 在终端环境下添加一个db命令

if __name__ == '__main__':
    manager.run()
