class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        # 返回一个“可执行”的字符串表示
        return f"Person(name={self.name!r}, age={self.age})"
    
    def __str__(self):
        # 返回一个“易读”的字符串表示
        return f"{self.name} ({self.age}岁)"

p = Person("Alice", 25)

# 调用 __repr__ 的场景
print(repr(p))  
# 输出：Person(name='Alice', age=25)

# 在交互式命令行直接输入 p
# >>> p
# Person(name='Alice', age=25)

# 调用 __str__ 的场景
print(p)        
# 输出：Alice (25 岁)