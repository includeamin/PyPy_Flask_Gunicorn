from flask import Flask ,send_from_directory,send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<div>includeamin</div><div>aminjamal10@gmail.com</div>"

@app.route("/users/balance/change")
def get_index():
    pass

from mysql import connector
def test():
    data = connector.connect(host='www.upsketchup.ir',port=3306, database='upsketch_app', user='upsketch', password='Aq9JC6Um9Fb3F3a',
                             db="upsketch_app")
    print(data)
    print("hello")
    #94.130.15.195



if __name__ == '__main__':
    test()
    #app.run(port=8080)
    #app.run(ssl_context=('cert.pem', 'key.pem'),port=8080)
