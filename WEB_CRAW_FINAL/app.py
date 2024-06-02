from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# 路徑到你的CSV文件
CSV_PATH = 'C:/Users/User/Downloads/templated-roadtrip/roadtrip/assets/merged.csv'

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_csv(query)
    return jsonify(results)

def search_csv(query):
    # 讀取CSV文件
    df = pd.read_csv(CSV_PATH)
    
    # 在所有列中搜索包含query的行
    mask = df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)
    results = df[mask]
    
    return results.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
