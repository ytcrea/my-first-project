from flask import Flask, request, render_template_string
import requests, os
app = Flask(__name__)
HTML = '''<!DOCTYPE html><html dir="rtl"><meta charset="UTF-8"><body style="text-align:center;padding:50px;background:#0f172a;color:#fff;font-family:sans-serif"><h1>🔍 فاحص المواقع</h1><form method=post><input name=url placeholder="https://example.com" style="padding:12px;width:80%;max-width:400px;border:0;border-radius:8px"><button style="padding:12px 20px;background:#38bdf8;border:0;border-radius:8px;color:#000;font-weight:bold">فحص</button></form>{% if result %}<div style="margin-top:30px;padding:20px;background:#1e293b;border-radius:12px;display:inline-block"><h2>{{result}}</h2></div>{% endif %}</body></html>'''
@app.route('/', methods=['GET','POST'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        try: r = requests.get(url if url.startswith('http') else 'https://'+url, timeout=7); result = f"✅ الموقع شغال | كود {r.status_code}"
        except: result = "❌ الموقع لا يعمل او الرابط غلط"
    return render_template_string(HTML, result=result)
if __name__ == '__main__': app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
