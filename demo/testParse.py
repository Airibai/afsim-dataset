import argparse

def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description="简单交互式程序")

    # 添加交互式模式参数
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="进入交互式模式"
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 根据参数决定模式
    if args.interactive:
        # 交互式模式
        print("=" * 40)
        print("交互式程序启动")
        print("=" * 40)
        print("输入 'exit' 退出程序")
        print("输入其他内容会打印出来")
        print("-" * 40)

        while True:
            # 获取用户输入
            user_input = input("请输入: ").strip()

            # 检查退出命令
            if user_input.lower() in ['exit', 'quit']:
                print("程序已退出。")
                break

            # 打印输入内容
            print(f"你输入了: {user_input}")

    else:
        # 非交互式模式
        print("非交互式模式")
        print("使用 --interactive 或 -i 参数进入交互式模式")

if __name__ == "__main__":
    main()
