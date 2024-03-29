#!/usr/bin/env python
import os
from flask.ext.script import Manager, Shell

from app import create_app
from app import mongo, mail
from app.models import User, Permission, Role, Saying

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, User=User, Role=Role, Permission=Permission, 
    	        mongo=mongo, Saying=Saying)
manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
