import argparse
from flask import Flask, jsonify
from src.app.routes import RouteApp
from src.app.queues import QueuesApp
import argparse

if __name__ == "__main__":
 
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", action="store", default="8000")
    parser.add_argument("-m", "--mode", action="store", default="rest")
    parser.add_argument("-q", "--queue", action="store", default="")

    args = parser.parse_args()
    print('Args', args)

    port = int(args.port)

    if args.mode == 'rest':
        app = RouteApp.create_app()
        app.run(host="0.0.0.0", port=port)

    elif args.mode == 'queue':
        queues_app = QueuesApp()
        queues_app.create_app(args.queue)

    else:
        print('Arg wrong | rest or queue')



