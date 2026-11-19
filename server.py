"""
Chianda Senior School - Student Voting System Server
Launches local HTTP server and opens web browser automatically.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

DEFAULT_PORT = 8000

def get_free_port(start_port):
    import socket
    port = start_port
    while port < start_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            res = sock.connect_ex(('127.0.0.1', port))
            if res != 0:
                return port
        port += 1
    return start_port

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = get_free_port(DEFAULT_PORT)
    handler = http.server.SimpleHTTPRequestHandler
    
    # Enable range requests and clean MIME types
    handler.extensions_map.update({
        '.js': 'application/javascript',
        '.css': 'text/css',
        '.html': 'text/html',
        '.json': 'application/json',
        '.svg': 'image/svg+xml'
    })

    url = f"http://localhost:{port}"

    print("=" * 70)
    print("   CHIANDA SENIOR SCHOOL - STUDENT COUNCIL ELECTIONS 2026/2027")
    print("   Independent Electoral Commission (CSSEC) System")
    print("=" * 70)
    print(f"[*] Local Web Server running at: {url}")
    print("[*] Opening system browser automatically...")
    print("\n[DEMO CREDENTIALS]")
    print("  • Student Voter (Ready to vote):  CHS-2023-0104  | PIN: 2024")
    print("  • Student Voter (Already voted):  CHS-2022-0042  | PIN: 1122")
    print("  • Chief Returning Officer:        COMMISSIONER-01| PIN: 8899")
    print("=" * 70)
    print("Press Ctrl+C to stop the server.\n")

    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Note: Could not auto-launch browser ({e}). Please open {url} manually.")

    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down Chianda Senior School voting server. Goodbye!")

if __name__ == '__main__':
    main()
