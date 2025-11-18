#!/usr/bin/env python3
import http.server
import ssl
import socket

# Configuration
PORT = 8444
CERTFILE = "cert.pem"
KEYFILE = "key.pem"

# Get local IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Try to get the actual network IP
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
except:
    pass

# Create server
server_address = ('0.0.0.0', PORT)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap with SSL using SSLContext (for Python 3.13+)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("=" * 60)
print("HTTPS Server Started!")
print("=" * 60)
print(f"\nOn this computer, open:")
print(f"  https://localhost:{PORT}")
print(f"\nOn your phone (same WiFi network), open:")
print(f"  https://{local_ip}:{PORT}")
print(f"\nYour phone will show a security warning.")
print(f"That's normal for self-signed certificates.")
print(f"Just click 'Advanced' and 'Proceed anyway'")
print("\nPress Ctrl+C to stop the server")
print("=" * 60)
print()

httpd.serve_forever()
