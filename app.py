from flask import Flask, request, render_template, redirect
import os
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')



@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/history/')
def history():
    pass

def get_ipv4_address():
    try:
        eth0_ip = os.getenv('IP_ETH0')
        print(eth0_ip)
        ip = '192.168.18.110'
        return ip
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    ip = get_ipv4_address()
    new_ip = '0.0.0.0'
    app.run(host=new_ip, port=5050, debug=True)
