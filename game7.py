from Flask import flask, render_templete_string, request 
‎
‎app = Flask(__name__)
‎
‎# إعداد واجهة المستخدم - تم تحسين الكود ليعمل على كافة المتصفحات بدون أخطاء
‎HTML_CONTENT = """
‎<!DOCTYPE html>
‎<html dir="rtl" lang="ar">
‎<head>
‎    <meta charset="UTF-8">
‎    <meta name="viewport" content="width=device-width, initial-scale=1.0">
‎    <title>الطيارة الملكية</title>
‎    <style>
‎        body { font-family: sans-serif; background-color: #0b0e11; color: white; text-align: center; margin: 0; }
‎        .top-bar { background: #1f2630; padding: 15px; color: #f0b90b; font-weight: bold; cursor: pointer; font-size: 20px; }
‎        .main-card { background: #161a1e; margin: 20px auto; padding: 20px; border-radius: 12px; max-width: 450px; border: 1px solid #2b3139; }
‎        .mult-text { font-size: 60px; color: #f0b90b; font-weight: bold; margin: 20px 0; }
‎        .balance { background: #2b3139; padding: 8px 15px; border-radius: 5px; display: inline-block; margin-bottom: 15px; border: 1px solid #f0b90b; }
‎        input { width: 85%; padding: 12px; margin: 10px 0; border-radius: 5px; border: 1px solid #474d57; background: #1e2329; color: white; }
‎        .btn { width: 90%; padding: 15px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 16px; }
‎        .btn-play { background: #f0b90b; color: black; }
‎        .btn-cash { background: #27ae60; color: white; display: none; }
‎        .deposit-box { background: #161a1e; max-width: 450px; margin: 20px auto; padding: 20px; border-radius: 12px; border: 1px solid #27ae60; }
‎        .secret-panel { display: none; background: #3
