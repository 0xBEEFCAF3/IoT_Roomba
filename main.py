from flask import Flask, request, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse, Message
from subprocess import call
import time
import roomba

app = Flask(__name__)

@app.route('/getImage')
def getImage():
    return send_from_directory('~/image.jpg')

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()

    command = message_body.strip().lower()

    if command == "start":
        resp.message('Starting your roomba boyo')
        roomba.clean()
    elif command == "halt":
        resp.message('Stopping your roomba boyo')
        roomba.power()
    elif command == "dock":
        resp.message('Time to dock')
        roomba.dock()
    elif command == "status":
        resp.message('Here are your stats boyo:')
        resp.message('jk')
    elif command == "photo":
        call(['bash', 'fswebcam ~/image.jpg'])
        time.sleep(3)
        msg = Message()\
                .body("Take a picture, it'll last longer ;)")\
                .Uri("128.197.251.71/getImage")
        resp.append(msg)
        
        
    elif command[:10] == "setdisplay":
        resp.message("Displaying your message, " + command[10:14])
        roomba.set_digits_string(command[10:14])
    else:
        print("What did you just send me??")
        resp.message('What did you just send me boyo?!')

    return str(resp)

if __name__ == '__main__':
    app.run()
