#!/usr/bin/env python
from flask import Flask
import xmlrunner
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Why Hello %s!\n' % username

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    ###########################################
    unittest.main()
    app.run(host='0.0.0.0')     # open for everyone
