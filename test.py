# probe_api.py - 探测 MinerU 可用接口（修复版）
import magic_pdf
import inspect

print(f"MinerU 版本: {magic_pdf.__version__ if hasattr(magic_pdf, '__version__') else 'unknown'}")

print("\n=== magic_pdf 顶层属性 ===")
top_attrs = [x for x in dir(magic_pdf) if not x.startswith('_')]
print(top_attrs)

print("\n=== magic_pdf.libs 子模块 ===")
try:
    import magic_pdf.libs as libs
    lib_attrs = [x for x in dir(libs) if not x.startswith('_')]
    print(lib_attrs)
    
    # 遍历每个子模块，查找可调用函数
    for submodule_name in lib_attrs:
        if not submodule_name.startswith('_'):
            try:
                submodule = getattr(libs, submodule_name)
                if inspect.ismodule(submodule):
                    funcs = [x for x in dir(submodule) 
                            if not x.startswith('_') and callable(getattr(submodule, x, None))]
                    if funcs:
                        # 修复：先用列表推导式，再格式化
                        func_sample = ', '.join(funcs[:5])
                        print(f"\n  magic_pdf.libs.{submodule_name}: [{func_sample}]...")
            except Exception as e:
                print(f"  检查 {submodule_name} 时出错: {e}")
except Exception as e:
    print(f"错误: {e}")

print("\n=== 尝试直接导入常见函数 ===")
candidates = [
    ("magic_pdf.parse", "pdf_to_markdown"),
    ("magic_pdf.libs.convert", "convert_pdf_to_md"),
    ("magic_pdf.libs.convert", "convert"),
    ("magic_pdf.pdf_parse", "parse_pdf"),
    ("magic_pdf", "parse"),
    ("magic_pdf", "pdf_to_markdown"),
    ("magic_pdf.data.read_api", "read_local_file"),
    ("magic_pdf.utils", "pdf2md"),
]

for module_path, func_name in candidates:
    try:
        module = __import__(module_path, fromlist=[func_name])
        func = getattr(module, func_name)
        print(f"✓ 找到: {module_path}.{func_name}")
    except Exception as e:
        print(f"✗ 失败: {module_path}.{func_name} - {type(e).__name__}")

print("\n=== 尝试使用 CLI 命令 ===")
import subprocess
try:
    result = subprocess.run(["magic-pdf", "--help"], capture_output=True, text=True, timeout=10)
    if result.returncode == 0:
        print("✓ magic-pdf CLI 可用")
        # 提取关键参数
        lines = result.stdout.split('\n')
        for line in lines:
            if any(kw in line.lower() for kw in ['-p', '--path', '-o', '--output', '--mode']):
                print(f"  {line.strip()}")
    else:
        print(f"✗ CLI 帮助命令失败: {result.stderr[:100]}")
except FileNotFoundError:
    print("✗ magic-pdf 命令未找到，请确认已正确安装")
except Exception as e:
    print(f"✗ CLI 检查异常: {e}")