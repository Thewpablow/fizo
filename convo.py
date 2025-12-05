import os
import time
import requests
import threading

# Static headers for HTTP requests
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
}

# Global flag to stop the loop
stop_flag = False

# File paths (change these paths as needed in Termux)
token_file_path = '/path/to/tokens.txt'  # Path to your token file
message_file_path = '/path/to/messages.txt'  # Path to your message file
thread_id = 'your_thread_id'  # Facebook thread ID where comments are posted
hater_name = 'Prefix'  # Name/Prefix to add before the message
speed = 5  # Delay in seconds between messages

def send_messages(thread_id, hater_name, time_interval, messages, tokens):
    global stop_flag
    post_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'

    msg_index = 0
    while not stop_flag:  # Infinite loop until stop_flag = True
        message = messages[msg_index % len(messages)]
        token = tokens[msg_index % len(tokens)]

        data = {'access_token': token, 'message': f"{hater_name} {message}"}
        response = requests.post(post_url, json=data, headers=headers)

        if response.ok:
            print(f"[SUCCESS] Sent: {message}")
        else:
            print(f"[FAILURE] Failed to send: {message} | {response.text}")

        msg_index += 1
        time.sleep(time_interval)

def main():
    global stop_flag

    # Read messages from file
    if not os.path.exists(message_file_path):
        print(f"❌ ERROR: Message file not found at {message_file_path}")
        return

    with open(message_file_path, 'r', encoding='utf-8') as f:
        messages = [line.strip() for line in f if line.strip()]

    # Read tokens from file
    if not os.path.exists(token_file_path):
        print(f"❌ ERROR: Token file not found at {token_file_path}")
        return

    with open(token_file_path, 'r', encoding='utf-8') as f:
        tokens = [line.strip() for line in f if line.strip()]

    # Start sending messages in background thread
    print(f"Starting message sending process for thread {thread_id}...")
    threading.Thread(target=send_messages, args=(thread_id, hater_name, speed, messages, tokens), daemon=True).start()

    try:
        while True:
            # Let the user stop the process gracefully
            user_input = input("\nPress 'q' to stop the process at any time: ").strip().lower()
            if user_input == 'q':
                stop_flag = True
                print("Stopping message sending process...")
                break
    except KeyboardInterrupt:
        stop_flag = True
        print("\nProcess interrupted by user. Stopping...")


if __name__ == '__main__':
    main()
