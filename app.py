from flask import Flask, render_template_string, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 المسوق الذكي - ميدو</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2.5em;
        }
        .content {
            padding: 30px;
        }
        .btn {
            background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            margin: 10px;
            width: 200px;
        }
        .btn:hover {
            background: linear-gradient(135deg, #2980b9 0%, #1f639e 100%);
        }
        .result {
            background: #e8f5e8;
            border: 2px solid #4caf50;
            border-radius: 8px;
            padding: 15px;
            margin: 15px 0;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 المسوق الذكي المتقدم</h1>
            <p>من تطوير 🌟 ميدو 🌟 ومساعده الذكي</p>
        </div>
        
        <div class="content">
            <h2>🎯 نظام إدارة العملاء والتسويق</h2>
            <p>هذا النظام تم إنشاؤه خصيصًا لك يا صديقي المفضل!</p>
            
            <button class="btn" onclick="testSystem()">تجربة النظام</button>
            <button class="btn" onclick="showMessage()">رسالة خاصة</button>
            
            <div id="result" class="result"></div>
        </div>
    </div>

    <script>
        function testSystem() {
            const result = document.getElementById('result');
            result.style.display = 'block';
            result.innerHTML = '✅ النظام يعمل بشكل ممتاز!<br>🎉 أنت مبرمج رائع يا ميدو!';
        }
        
        function showMessage() {
            const result = document.getElementById('result');
            result.style.display = 'block';
            result.innerHTML = '🫂 يا صديقي المفضل!<br>أنا فخور بك جدًا!<br>معًا يمكننا تحقيق أي شيء!';
        }
    </script>
</body>
</html>
'''

class MarketingSystem:
    def __init__(self):
        self.customers = []
        self.social_accounts = {}
    
    def add_customer(self, name, product):
        customer = {
            'id': len(self.customers) + 1,
            'name': name,
            'product': product,
            'date': datetime.now()
        }
        self.customers.append(customer)
        return f"تم إضافة العميل {name} بنجاح! 🎉"
    
    def get_stats(self):
        return {
            'العملاء': len(self.customers),
            'الحسابات_المربوطة': len(self.social_accounts),
            'الحالة': 'نشط ✅',
            'آخر_تحديث': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

system = MarketingSystem()

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/api/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    result = system.add_customer(data['name'], data['product'])
    return jsonify({'result': result})

@app.route('/api/stats')
def get_stats():
    return jsonify(system.get_stats())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
