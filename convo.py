import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading


# ================================
# LocalServer
# ================================
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"MR MANNI")


def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()


# ================================
# Main Processing Logic
# ================================
def send_messages():

    # Clear screen (Termux/PC)
    def cls():
        if system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    cls()

    print("\n===============================")
    print(" TOKEN FILE PATH REQUIRED")
    print("===============================")
    token_file = input("Enter token file path: ").strip()

    print("\n===============================")
    print(" MESSAGE FILE PATH REQUIRED")
    print("===============================")
    msg_file = input("Enter message file path: ").strip()

    print("\n===============================")
    print(" ENTER CONVERSATION ID")
    print("===============================")
    convo_id = input("Convo ID: ").strip()

    print("\n===============================")
    print(" ENTER PREFIX / NAME")
    print("===============================")
    prefix_name = input("Prefix Name: ").strip()

    print("\n===============================")
    print(" ENTER DELAY (SECONDS)")
    print("===============================")
    speed = int(input("Delay: ").strip())

    # =====================
    # Load file data
    # =====================
    with open(token_file, "r") as f:
        tokens = [x.strip() for x in f.readlines()]
    num_tokens = len(tokens)

    with open(msg_file, "r", encoding="utf-8") as f:
        messages = [x.strip() for x in f.readlines()]
    num_messages = len(messages)

    max_tokens = min(num_tokens, num_messages)

    print("\n[+] Loaded", num_tokens, "tokens")
    print("[+] Loaded", num_messages, "messages\n")

    print("[+] Starting Process...\n")

    # =====================
    # LOOP — SAFE PLACEHOLDER
    # =====================
    while True:
        try:
            for i in range(num_messages):

                token_index = i % max_tokens
                token = tokens[token_index]
                message = messages[i]

                # ===== SAFE PLACEHOLDER =====
                print("---------------------------------------")
                print(f"[INFO] Message #{i+1}")
                print(f"[INFO] Prefix: {prefix_name}")
                print(f"[INFO] Content: {message}")
                print(f"[INFO] Token Slot: #{token_index+1}")
                print(f"[INFO] Token Value: {token}")
                print("---------------------------------------\n")

                time.sleep(speed)

            print("\n[+] Loop Completed — Restarting...\n")

        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(2)


# ================================
# Entry Point
# ================================
def main():

    # Start local server
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    # Run message function
    send_messages()


if __name__ == "__main__":
    main()
