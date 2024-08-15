from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import numpy as np
from scipy.stats import kstest


# 定义处理逻辑的函数
def calculate_diff_mean_and_variance(numbers):
    diff_list = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
    mean_diff = np.mean(diff_list)
    var_diff = np.var(diff_list)
    return diff_list, mean_diff, var_diff


def triangular_cdf(x, c):
    return np.where(x < 0, 0, np.where(x > c, 1, ((2 * x * c - x ** 2) / c ** 2)))


def perform_ks_test(diff_list, c=1000):
    result = kstest(diff_list, triangular_cdf, args=(c,))
    return {
        "KS statistic": result.statistic,
        "p-value": result.pvalue
    }


# 创建自定义的处理程序类
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 获取请求的内容长度
        content_length = int(self.headers['Content-Length'])
        # 读取并解析请求体
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        # 从接收到的数据中提取numbers和c
        numbers = data.get("numbers", [])
        c = data.get("c", 1000)  # 默认值为1000

        # 执行逻辑计算
        diff_list, mean_diff, var_diff = calculate_diff_mean_and_variance(numbers)
        ks_test_result = perform_ks_test(diff_list, c)

        # 生成响应内容
        response = {
            # "mean_diff": mean_diff,
            # "var_diff": var_diff,
            "ks_test_result": ks_test_result
        }

        # 将响应结果以JSON格式返回
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))


# 启动服务器
def run(server_class=HTTPServer, handler_class=RequestHandler, port=6001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
