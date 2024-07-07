import json
import time
import sys
import os
import http.server
import socketserver
import threading
import requests  # Import requests explicitly

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"SERVER RUNNING => XMARTY AYUSH K1NG")

def execute_server():
    PORT = 4000

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

def post_comments():
    try:
        with open('password.txt', 'r') as file:
            password = file.read().strip()

        with open('tokennum.txt', 'r') as file:
            tokens = file.readlines()
        num_tokens = len(tokens)

        with open('post_url.txt', 'r') as file:
            post_url = file.read().strip()

        with open('comments.txt', 'r') as file:
            comments = file.readlines()
        num_comments = len(comments)

        with open('hatersname.txt', 'r') as file:
            haters_name = file.read().strip()

        with open('time.txt', 'r') as file:
            speed = int(file.read().strip())

        access_tokens = [token.strip() for token in tokens]
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'referer': 'www.google.com'
        }

        while True:
            for comment_index in range(num_comments):
                token_index = comment_index % num_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': f"{haters_name} {comment}"}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print(f"[+] Comment No. {comment_index + 1} Post Id {post_url} Token No. {token_index + 1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                else:
                    print(f"[x] Failed to send Comment No. {comment_index + 1} Post Id {post_url} Token No. {token_index + 1}: {haters_name} {comment}")
                    print(f"  - Time: {current_time}")
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")

    except Exception as e:
        print(f"[!] An error occurred: {e}")

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    post_comments()

if __name__ == '__main__':
    main()
    
