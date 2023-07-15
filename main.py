from imaplib2 import IMAP4_SSL
import argparse
import time
"""
Zimbra is a popular collaboration and email server software suite that provides email,
calendar, contacts, tasks, and other collaboration features. It offers both on-premises
and cloud-based solutions for businesses, service providers, and enterprises.
Zimbra has gained popularity due to its rich feature set, scalability, open-source heritage,
and flexibility in deployment options. It is used by organizations of all sizes, including small businesses,
educational institutions, government agencies, and enterprises, to enhance collaboration and communication within their environments.
"""

def version_detector(host:str,port=993):

    with IMAP4_SSL(host, port) as server:
        print("[X] ",server.welcome.decode('utf-8'))
        info = server.id()
        for item in server.capabilities:
            print("[X] ",item)
        for i in info[1]:
            print("[X] ",i.decode('utf-8').replace('"','').split(' ')[2],i.decode('utf-8').replace('"', '').split(' ')[3])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Command Line Program')
    parser.add_argument('-u', '--url', type=str, help='URL argument')
    parser.add_argument('-p', '--port', type=int, help='Port argument')
    args = parser.parse_args()

    if args.url and args.port:
        version_detector(host=args.url,port=args.port)
    else:
        print('Please provide both URL and Port arguments')
