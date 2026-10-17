"""Local preview only. Serves ../site; for .php pages (no PHP installed) it strips the PHP blocks so the layout can be viewed.
Run: python3 tools/preview_server.py 8765"""
import http.server, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
OPTIONS = ''.join(f'<option value="{k}">{v}</option>' for k, v in
                  [('treatment', '治療に関するお問い合わせ'), ('recruit', '採用に関するお問い合わせ'), ('other', 'その他')])

def strip_php(src):
    src = re.sub(r'^<\?php.*?\?>\n', '', src, count=1, flags=re.S)
    src = re.sub(r'<\?php if \(\$errors\):.*?<\?php endif; \?>', '', src, flags=re.S)
    src = re.sub(r'<\?php foreach \(\$PURPOSES.*?<\?php endforeach; \?>', OPTIONS, src, flags=re.S)
    src = re.sub(r'<\?=.*?\?>', '', src, flags=re.S)
    src = re.sub(r'<\?php.*?\?>', '', src, flags=re.S)
    return src

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def do_GET(self):
        path = self.path.split('?')[0]
        if path.endswith('.php'):
            f = os.path.join(ROOT, path.lstrip('/'))
            if os.path.exists(f):
                body = strip_php(open(f, encoding='utf-8').read()).encode('utf-8')
                self.send_response(200); self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(body))); self.end_headers(); self.wfile.write(body); return
        return super().do_GET()
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()

if __name__ == '__main__':
    http.server.ThreadingHTTPServer(('127.0.0.1', int(sys.argv[1]) if len(sys.argv) > 1 else 8765), H).serve_forever()
