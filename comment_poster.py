import requests
import time
import os
import sys

BANNER = """
=============================================
      FACEBOOK AUTO COMMENTER (TERMUX)
      CREATED BY RAAJVEER BOSS
=============================================
"""

def send_comment(token, post_id, comment):
    url = f"https://graph.facebook.com/{post_id}/comments"
    payload = {"message": comment, "access_token": token}

    try:
        response = requests.post(url, data=payload)
    except Exception as e:
        print(f"❌ Network Error: {e}")
        return False

    if response.status_code == 200:
        print(f"✔️ Sent: {comment}")
        return True
    else:
        print(f"❌ Failed: {comment}")
        print("Response:", response.text)
        return False


def main():
    print(BANNER)

    # Token file
    token_path = input("📌 Enter token file path: ").strip()
    if not os.path.exists(token_path):
        print("❌ ERROR: Token file not found!")
        sys.exit()

    with open(token_path, "r") as f:
        token = f.read().strip()

    # Facebook Post ID
    post_id = input("📌 Enter Facebook Post ID: ").strip()

    # Comments file
    comments_path = input("📌 Enter comments file path: ").strip()
    if not os.path.exists(comments_path):
        print("❌ ERROR: Comments file not found!")
        sys.exit()

    with open(comments_path, "r", encoding="utf-8") as f:
        comments = [c.strip() for c in f if c.strip()]

    # Delay
    delay = int(input("⏱  Enter delay between comments (seconds): ").strip())

    print("\n=============================================")
    print(f" Total Comments Loaded : {len(comments)}")
    print(" Starting in 3 seconds…")
    print("=============================================\n")
    time.sleep(3)

    # Start sending comments
    for i, comment in enumerate(comments, 1):
        print(f"➡️  Sending comment {i}/{len(comments)} ...")
        send_comment(token, post_id, comment)
        time.sleep(delay)

    print("\n=============================================")
    print(" ✔️ PROCESS COMPLETED SUCCESSFULLY!")
    print("=============================================\n")


if __name__ == "__main__":
    main()
