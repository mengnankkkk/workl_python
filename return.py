def convert_to_url(file_name):
    # 定义固定的 URL 部分
    base_url = "http://mengnankk.top:9000/img/"
    
    # 构建新的 URL
    return f"{base_url}{file_name}"

def main():
    print("请输入文件名（例如：102368084_p0_square1200.jpg），输入 'exit' 退出程序。")
    
    while True:
        # 提示用户输入文件名
        file_name = input("请输入文件名：")
        
        # 允许用户输入 'exit' 以退出程序
        if file_name.lower() == 'exit':
            print("程序退出。")
            break
        
        # 调用方法生成 URL
        url = convert_to_url(file_name)
        
        # 输出结果
        print("转换后的 URL 是：")
        print(url)

if __name__ == "__main__":
    main()
