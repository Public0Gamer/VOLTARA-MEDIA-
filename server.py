import os
import mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AgentReadyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Global CORS for all agent discovery and API endpoints
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split('?')[0].rstrip('/')
        accept_header = self.headers.get('Accept', '')

        # 1. Content Negotiation for Markdown (RFC / Cloudflare Markdown for Agents)
        if clean_path in ['', '/index.html']:
            if 'text/markdown' in accept_header or 'format=markdown' in self.path:
                md_path = os.path.join(BASE_DIR, 'index.md')
                if os.path.exists(md_path):
                    with open(md_path, 'rb') as f:
                        content = f.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/markdown; charset=utf-8')
                    self.send_header('x-markdown-tokens', str(len(content.split())))
                    self.send_header('Content-Length', str(len(content)))
                    self.send_header(
                        'Link',
                        '</.well-known/api-catalog>; rel="api-catalog", </docs/api>; rel="service-doc", </.well-known/ai-catalog.json>; rel="ai-catalog"'
                    )
                    self.end_headers()
                    self.wfile.write(content)
                    return

            # Default HTML response for root/homepage with RFC 8288 Link Headers
            html_path = os.path.join(BASE_DIR, 'index.html')
            if os.path.exists(html_path):
                with open(html_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                # RFC 8288 Link headers for agent discovery
                self.send_header(
                    'Link',
                    '</.well-known/api-catalog>; rel="api-catalog", </docs/api>; rel="service-doc", </.well-known/ai-catalog.json>; rel="ai-catalog", </.well-known/mcp/server-card.json>; rel="mcp-server-card", </.well-known/agent-skills/index.json>; rel="agent-skills", </auth.md>; rel="author-md", </index.md>; rel="alternate"; type="text/markdown"'
                )
                self.end_headers()
                self.wfile.write(content)
                return

        # 2. robots.txt
        if clean_path == '/robots.txt':
            robots_path = os.path.join(BASE_DIR, 'robots.txt')
            if os.path.exists(robots_path):
                with open(robots_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 3. sitemap.xml
        if clean_path == '/sitemap.xml':
            sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
            if os.path.exists(sitemap_path):
                with open(sitemap_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/xml; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 4. RFC 9727 API Catalog
        if clean_path in ['/.well-known/api-catalog', '/.well-known/api-catalog.json']:
            cat_path = os.path.join(BASE_DIR, '.well-known', 'api-catalog')
            if not os.path.exists(cat_path):
                cat_path = os.path.join(BASE_DIR, '.well-known', 'api-catalog.json')
            if os.path.exists(cat_path):
                with open(cat_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/linkset+json; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 5. /docs/api route
        if clean_path == '/docs/api':
            doc_path = os.path.join(BASE_DIR, 'docs', 'api.html')
            if os.path.exists(doc_path):
                with open(doc_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 6. OAuth / OIDC Discovery Endpoints
        oauth_json_endpoints = {
            '/.well-known/openid-configuration': os.path.join(BASE_DIR, '.well-known', 'openid-configuration'),
            '/.well-known/oauth-authorization-server': os.path.join(BASE_DIR, '.well-known', 'oauth-authorization-server'),
            '/.well-known/oauth-protected-resource': os.path.join(BASE_DIR, '.well-known', 'oauth-protected-resource'),
            '/.well-known/mcp/server-card.json': os.path.join(BASE_DIR, '.well-known', 'mcp', 'server-card.json'),
            '/.well-known/agent-skills/index.json': os.path.join(BASE_DIR, '.well-known', 'agent-skills', 'index.json'),
            '/.well-known/ai-catalog.json': os.path.join(BASE_DIR, '.well-known', 'ai-catalog.json')
        }

        if clean_path in oauth_json_endpoints:
            target_path = oauth_json_endpoints[clean_path]
            if os.path.exists(target_path):
                with open(target_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 7. auth.md (WorkOS specification)
        if clean_path == '/auth.md':
            auth_path = os.path.join(BASE_DIR, 'auth.md')
            if os.path.exists(auth_path):
                with open(auth_path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/markdown; charset=utf-8')
                self.send_header('Content-Length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 8. Favicon silence
        if clean_path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return

        # Fallback to standard handler
        return super().do_GET()

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, AgentReadyHTTPRequestHandler)
    print(f"[*] Voltara Agent-Ready Server running at http://localhost:{port}/")
    print(f"   - robots.txt:        http://localhost:{port}/robots.txt")
    print(f"   - sitemap.xml:       http://localhost:{port}/sitemap.xml")
    print(f"   - Link Headers:      RFC 8288 active on /")
    print(f"   - Markdown for AI:   Accept: text/markdown -> /index.md")
    print(f"   - API Catalog:       http://localhost:{port}/.well-known/api-catalog")
    print(f"   - MCP Server Card:   http://localhost:{port}/.well-known/mcp/server-card.json")
    print(f"   - ARD Manifest:      http://localhost:{port}/.well-known/ai-catalog.json")
    print(f"   - WebMCP In-Browser: navigator.modelContext on /")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
