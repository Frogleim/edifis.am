from flask import Flask, request, render_template, redirect
import os
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(host=ip, debug=True)
