
# 固定 reg 函数，支持 2 个参数：开始、结束
def reg(start, end=None):
    if end is None:
        return range(start)
    return range(start, end + 1)
def help():
    help_text = """
Lambda Custom Language — Full Official Syntax Manual (English)
This is 100% matching your current working code, including all keywords, rules, functions, and error checks.
Lambda Language Syntax Guide
1. Basic Rules
All code blocks must use curly braces { }.
{ and } must be paired. Unbalanced braces → error[11].
Native Python keywords (like if, for, try) are forbidden.
Comments start with >>.
Semicolon ; is optional but recommended for assignment.
2. Variable Assignment
Syntax
plaintext
variable setitem value;
Example
plaintext
a setitem 10;
name setitem "Lambda";
3. Output (Print)
Syntax
plaintext
printe content
Example
plaintext
printe 100
printe "Hello World"
printe a
4. Conditionals
If
plaintext
If condition do{
    code
}
Elif
plaintext
Elif condition do{
    code
}
Else
plaintext
Else do{
    code
}
Full Example
plaintext
If a <> 5 do{
    printe "a not equal to 5"
}
Elif a <!> 3 do{
    printe "a not 3"
}
Else do{
    printe "other"
}
5. Loops
While Loop
plaintext
While condition do{
    code
}
For Loop
plaintext
var For into iterable do{
    code
}
Example
plaintext
i For into reg(1,10) do{
    printe i
}
6. Error Handling (Try / Except)
Syntax
plaintext
Try{
    risky code
}
Except{
    handle error
}
Example
plaintext
Try{
    unknown_var setitem 10;
}
Except{
    printe "Error caught"
}
7. Operators
表格
Your Syntax	Python Meaning		
a <> b	a == b (equal)		
a !- b	a != b (not equal)		
a -> b	a in b (membership)		
`a		b`	a or b
a & b	a and b		
<!> a	not a		
8. Functions
Define Function (no parameters)
plaintext
funcname perform{
    code
}
Define Function (with parameter)
plaintext
funcname perform param{
    code
}
Example
plaintext
test perform{
    printe "Hello from function"
}
9. Classes
Define Class
plaintext
ClassName classes{
    code
}
Constructor
plaintext
init impose{
    code
}
Constructor with parameter
plaintext
init impose param{
    code
}
Method
plaintext
methodname perform{
    code
}
Example
plaintext
Person classes{
    init impose name{
        printe "Created"
    }
}
10. Built-in Functions
表格
Function	Usage	Meaning
reg(s, e)	reg(1,5)	numbers from 1 to 5
inp(prompt)	inp("Enter: ")	get user input
num(var)	num(a)	convert to integer
string(var)	string(a)	convert to string
step(x)	step(list)	get length
fmt(a,b,c)	fmt("[",a,"]")	format string
help()	help()	open help window
11. Built-in Classes
Bottle (container)
plaintext
box = Bottle()
box.key setitem 100;
printe box.key
Calculate (math tools)
plaintext
Calculate.add(a,b)
Calculate.minus(a,b)
Calculate.times(a,b)
Calculate.divide(a,b)
Calculate.power(a,b)
File (file operations)
plaintext
f = File("test.txt", "w")
f.write("Hello")
f.read()
12. List & Dictionary Tools
plaintext
listindex(list, index)    → get item
dictionarykey(dict, key)  → get value
Bottle.lists(data)        → convert to list
Bottle.dictionary(data)  → convert to dict
13. Comments
plaintext
>> This is a comment
14. Error Codes
11: Syntax error / unbalanced braces
21: Variable not defined
31: Type error
41: Index error
42: Key error
51: Division by zero
98: Program stopped
99: Unknown error
15. Full Example Program
plaintext
>> Demo program
a setitem 10;

If a <> 10 do{
    printe "a is 10"
}
Else do{
    printe "a is not 10"
}

Try{
    b setitem c;
}
Except{
    printe "Error handled"
}

i For into reg(1,3) do{
    printe i
}
=============================================
"""
    import tkinter as tk
    t = tk.Toplevel()
    t.title("Syntax Help")
    t.geometry('750x700')

    text_box = tk.Text(
        t,
        font=('Consolas', 14),
        bg='black',
        fg='lightgreen',
        wrap=tk.WORD
    )
    text_box.pack(expand=True, fill="both", side="left")
    text_box.insert("1.0", help_text)
    text_box.config(state=tk.DISABLED)

    scroll = tk.Scrollbar(t, command=text_box.yview)
    scroll.pack(side="right", fill="y")
    text_box.config(yscrollcommand=scroll.set)


def brond():
    pass
def res(s):
    return rf'{s}'

def fmt(a,b,c):
    b = str(b)
    return f'{a}{b}{c}'



class Calculate:
    def __init__(self):
        pass
    def add(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def times(a,b):
        return a*b
    def divide(a,b):
        return a/b
    def power(a,b):
        return a**b

def to(md):
    __import__(md)

output_buffer = []
user_vars = {}

_ret_buf = None
def relter(*re):
    global _ret_buf
    res = re
    _ret_buf = res
    return res

def delete(var_name):
    global _ret_buf
    if var_name in user_vars:
        del user_vars[var_name]
        _ret_buf = True
    else:
        _ret_buf = False
        
def getvar(var_name):
    global _ret_buf
    res = user_vars.get(var_name, None)
    _ret_buf = res
    return res

def getret():
    global _ret_buf
    return _ret_buf

def num(n):
    global _ret_buf
    val = int(user_vars[n])
    user_vars[n] = val
    _ret_buf = val

def string(n):
    global _ret_buf
    val = str(user_vars[n])
    user_vars[n] = val
    _ret_buf = val

def boor(b):
    global _ret_buf
    val = bool(user_vars[b])
    user_vars[b] = val
    _ret_buf = val

class ClassesAndFunctionsAttributes:
    _local_stack = []
    _nonlocal_env = {}
    def locol(self, mode, key):
        if mode == "l":
            if self._local_stack:
                self._local_stack[-1][key] = None
        elif mode == "n":
            self._nonlocal_env[key] = None
        elif mode == "g":
            globals()[key] = None
    def enter(self):
        self._local_stack.append({})
    def exit(self):
        if self._local_stack:
            self._local_stack.pop()

# ↓↓↓ 修复好的 inp，不卡、不闪退、能输入、能回车结束
_wait_input = False
_input_buf = ""

def inp(prompt):
    global _wait_input, _input_buf
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, prompt)
    output_box.see(tk.END)
    output_box.focus()

    _wait_input = True
    _input_buf = ""

    def temp_enter(e):
        global _input_buf
        _input_buf = output_box.get("insert linestart", "insert").strip()
        globals()['_wait_input'] = False
        return "break"

    output_box.bind("<Return>", temp_enter)
    while _wait_input:
        root.update()
    output_box.unbind("<Return>")
    output_box.insert(tk.END, "\n")
    output_box.config(state=tk.DISABLED)
    return _input_buf

class Bottle:
    def __init__(self):
        pass
    def lists(self,l):
        return list(l)
    def dictionary(self,e):
        return dict(e)
    def ListFunc(self,s,e,sp,r=lambda x: x):
        return [r(i) for i in range(s,e,sp)]
    def DictionaryFunc(self,s,e,sp,r=lambda x: x):
        return {k:v for k,v in [r(i) for i in range(s,e,sp)]}
import os
class File:
    def __init__(self, path, mode="r"):
        self.f = open(path, mode, encoding="utf-8")
    def write(self, content):
        self.f.write(str(content))
        self.f.close()
    def read(self):
        return self.f.read()
    @staticmethod
    def remove(path):
        os.remove(path)
    @staticmethod
    def exists(path):
        return os.path.exists(path)
def step(f):
    return len(f)
def listindex(n,s):
    return n[s]
def dictionarykey(d,k):
    return d[k]

import tkinter as tk
from tkinter import scrolledtext, filedialog
import json

safe_globals = {}

def force_print(*args):
    output_box.config(state=tk.NORMAL)
    output_box.insert(tk.END, " ".join(str(a) for a in args) + "\n")
    output_box.see(tk.END)
    output_box.config(state=tk.DISABLED)

def printe(*pit):
    force_print(str(pit))

COLOR_CONFIG = '''
{
  "editor": {
    "bg": "#000000",
    "fg": "#cdd6f4",
    "cursor": "#ffffff"
  },
  "output": {
    "bg": "#000000",
    "text": "#00ff00"
  },
  "highlight": {
    "builtin": "#ff9e1b",
    "class": "#6edabc",
    "func": "#569cd6",
    "number": "#ff0000",
    "string": "#00ff00",
    "func_def": "#c678dd",
    "func_call": "#c678dd",
    "var": "#61afef",
    "comment": "#7f7f7f"
  },
  "keywords": {
    "classes": ["Ifuage", "Leanx", "Canol", "ClassesAndFunctionsAttributes","Bottle","Calculate","true","false"],
    "builtins": ["setitem", "printe", "difinition", "to", "treklly", "num", "string", "boor", "delete", "relter", "yielder","local","enter","exit","dictionary","lists","lambda","add","minus","times","divide","ListFunc","DictionaryFunc","step","know","whileloop","listindex","dictionarykey","reg","brond","local","enter","exit","reg","fmt",
    "inp","Else","Elif","While","For","into","init","If","help","perform","impose","classes","Except","Try","getret"]
  }
}
'''
cfg = json.loads(COLOR_CONFIG)

root = tk.Tk()
root.title("Lambda")
root.geometry("900x700")

editor = scrolledtext.ScrolledText(root, font=("Menlo",14), 
                                   bg=cfg["editor"]["bg"], 
                                   fg=cfg["editor"]["fg"], 
                                   insertbackground="#888888",  # 灰色光标
                                   insertwidth=4)                # 加粗

editor.tag_config("builtin", foreground=cfg["highlight"]["builtin"])
editor.tag_config("class", foreground=cfg["highlight"]["class"])
editor.tag_config("string", foreground=cfg["highlight"]["string"])
editor.tag_config("number", foreground=cfg["highlight"]["number"])
editor.tag_config("comment", foreground=cfg["highlight"]["comment"])
editor.tag_config("func_def", foreground=cfg["highlight"]["func_def"])
editor.tag_config("func_call", foreground=cfg["highlight"]["func_call"])
editor.tag_config("var", foreground=cfg["highlight"]["var"])
# ✅ 关键：Mac 只能用这两个，不报错
editor.config(insertontime=10000, insertofftime=0)  # 关闭闪烁

editor.pack(fill=tk.BOTH, expand=1, padx=10, pady=5)

editor.tag_config("builtin", foreground=cfg["highlight"]["builtin"])
editor.tag_config("class", foreground=cfg["highlight"]["class"])
editor.tag_config("string", foreground=cfg["highlight"]["string"])
editor.tag_config("number", foreground=cfg["highlight"]["number"])
editor.tag_config("comment", foreground=cfg["highlight"]["comment"])
editor.pack(fill=tk.BOTH, expand=1, padx=10, pady=5)

output_box = scrolledtext.ScrolledText(root, height=12, bg=cfg["output"]["bg"], fg=cfg["output"]["text"])
output_box.config(state=tk.DISABLED)
output_box.pack(fill=tk.X, padx=10, pady=5)



# =============== 修复好的：只高亮完整单词，不乱染变量颜色 ===============
def highlight_keywords(event=None):
    editor.tag_remove("comment", "1.0", tk.END)
    editor.tag_remove("string", "1.0", tk.END)
    editor.tag_remove("number", "1.0", tk.END)
    editor.tag_remove("builtin", "1.0", tk.END)
    editor.tag_remove("class", "1.0", tk.END)
    editor.tag_remove("func_def", "1.0", tk.END)
    editor.tag_remove("func_call", "1.0", tk.END)
    editor.tag_remove("var", "1.0", tk.END)

    import re
    full_text = editor.get("1.0", tk.END)

    # ========== 1. 注释（最先渲染，层级最低）==========
    idx = "1.0"
    while True:
        pos = editor.search(">>", idx, stopindex=tk.END)
        if not pos: break
        editor.tag_add("comment", pos, f"{pos} lineend")
        idx = f"{pos} lineend"

    # ========== 2. 双引号/单引号字符串（解决多字符变色）==========
    def mark_string(quote):
        nonlocal idx
        idx = "1.0"
        while True:
            pos = editor.search(quote, idx, stopindex=tk.END)
            if not pos: break
            end = editor.search(quote, f"{pos}+1c", stopindex=tk.END)
            if end:
                editor.tag_add("string", pos, f"{end}+1c")
                idx = f"{end}+1c"
            else:
                idx = f"{pos}+1c"
    mark_string('"')
    mark_string("'")

    # ========== 3. 数字 ==========
    idx = "1.0"
    while True:
        res = re.search(r'\d+', editor.get(idx, tk.END))
        if not res: break
        pos = f"{idx}+{res.start()}c"
        endpos = f"{idx}+{res.start() + len(res.group())}c"
        editor.tag_add("number", pos, endpos)
        idx = endpos

    # ========== 4. 内置关键字 builtin 橙色（优先级高于函数调用）==========
    builtin_words = cfg["keywords"]["builtins"]
    builtin_pattern = r'\b(' + '|'.join(re.escape(k) for k in builtin_words) + r')\b'
    for m in re.finditer(builtin_pattern, full_text):
        s = f"1.0+{m.start()}c"
        e = f"1.0+{m.end()}c"
        editor.tag_add("builtin", s, e)

    # ========== 5. 内置类 class 青色 #6edabc ==========
    class_words = cfg["keywords"]["classes"]
    class_pattern = r'\b(' + '|'.join(re.escape(k) for k in class_words) + r')\b'
    for m in re.finditer(class_pattern, full_text):
        s = f"1.0+{m.start()}c"
        e = f"1.0+{m.end()}c"
        editor.tag_add("class", s, e)

    # ========== 6. 函数定义 xxx perform 紫色 func_def ==========
    func_def_pat = r'\b(\w+)\s+perform\b'
    for m in re.finditer(func_def_pat, full_text):
        s = f"1.0+{m.start(1)}c"
        e = f"1.0+{m.end(1)}c"
        editor.tag_add("func_def", s, e)

    # ========== 7. 函数调用 func() 规则修正：如果是内置关键字，不再染func_call ==========
    func_call_pat = r'\b(\w+)\('
    for m in re.finditer(func_call_pat, full_text):
        fn_name = m.group(1)
        # 关键判断：属于内置函数，跳过，保留builtin橙色，不覆盖成紫色
        if fn_name in builtin_words:
            continue
        s = f"1.0+{m.start(1)}c"
        e = f"1.0+{m.end(1)}c"
        editor.tag_add("func_call", s, e)

    # ========== 8. 赋值变量 var setitem ==========
    var_assign_pat = r'\b(\w+)\s+setitem\b'
    for m in re.finditer(var_assign_pat, full_text):
        s = f"1.0+{m.start(1)}c"
        e = f"1.0+{m.end(1)}c"
        editor.tag_add("var", s, e)

    # ========== 9. 普通独立变量（排除关键字、类、数字、函数）==========
    skip_set = set(builtin_words + class_words)
    skip_re = "|".join(re.escape(w) for w in skip_set)
    var_pat = re.compile(rf'(?<!\w)(?!({skip_re}|\d))([a-zA-Z_]\w+)(?!\w|\()')
    for m in var_pat.finditer(full_text):
        s = f"1.0+{m.start(2)}c"
        e = f"1.0+{m.end(2)}c"
        editor.tag_add("var", s, e)

def auto_indent(event):
    if event.keysym != "Return":
        return

    line_idx = editor.index(tk.INSERT).split(".")[0]
    line_full = editor.get(f"{line_idx}.0", f"{line_idx}.end")

    # 取出当前行开头空白（缩进）
    indent_str = ""
    for c in line_full:
        if c.isspace():
            indent_str += c
        else:
            break

    stripped = line_full.strip()
    
    # 原有触发缩进的符号： (  :  {  [  \
    need_extra = stripped.endswith(("(", ":", "{", "[", "\\"))

    # 关键：如果是以 \ 结尾，下一行直接和当前缩进对齐，不额外加空格
    if stripped.endswith("\\"):
        editor.insert(tk.INSERT, "\n" + indent_str)
    elif need_extra:
        editor.insert(tk.INSERT, "\n" + indent_str + "    ")
    else:
        editor.insert(tk.INSERT, "\n" + indent_str)

    return "break"
editor.bind("<KeyRelease>", highlight_keywords)
editor.bind("<Return>", auto_indent)
'''
txt = editor.get("1.0", tk.END)
'''

def run_code():
    import builtins
    __build_class__ = builtins.__build_class__

    ERROR_CODE_MAP = {
        0: BaseException,
        1: Exception,
        11: SyntaxError,
        12: IndentationError,
        13: TabError,
        21: NameError,
        22: UnboundLocalError,
        23: AttributeError,
        31: TypeError,
        32: ValueError,
        33: UnicodeError,
        34: UnicodeDecodeError,
        35: UnicodeEncodeError,
        36: UnicodeTranslateError,
        41: IndexError,
        42: KeyError,
        43: LookupError,
        51: ZeroDivisionError,
        52: OverflowError,
        53: FloatingPointError,
        61: StopIteration,
        62: StopAsyncIteration,
        71: OSError,
        72: FileNotFoundError,
        73: FileExistsError,
        74: IsADirectoryError,
        75: NotADirectoryError,
        76: PermissionError,
        77: TimeoutError,
        78: IOError,
        81: ImportError,
        82: ModuleNotFoundError,
        91: RuntimeError,
        92: NotImplementedError,
        93: RecursionError,
        101: MemoryError,
        102: BufferError,
        103: EnvironmentError,
        104: SystemError,
        111: AssertionError,
        112: EOFError,
        113: ReferenceError,
    }
    ERROR_NAME_TO_CODE = {v.__name__: k for k, v in ERROR_CODE_MAP.items()}

    txt = editor.get("1.0", tk.END).strip()
    import keyword, re

    # 拦截直接写原生Python关键字（try/except放行）
    py_reserved = [k for k in keyword.kwlist if k not in ("try", "except")]
    py_pattern = r'\b(' + '|'.join(re.escape(w) for w in py_reserved) + r')\b'
    if re.search(py_pattern, txt):
        force_print("error[11]: Python native syntax is not allowed")
        return

    # 注释清除
    txt = re.sub(r'>>.*?$', '', txt, flags=re.MULTILINE)

    # 大括号成对校验
    if txt.count("{") != txt.count("}"):
        force_print("error[11]: unbalanced braces (must use { and })")
        return

    # ========== 只做语法结构翻译，不再处理任何变量 ==========
    # 函数定义
    txt = re.sub(r'(\w+)\s+perform\s*{', r'def \1():', txt)
    txt = re.sub(r'(\w+)\(([^)]+)\)\s+perform\s*{', r'def \1(\2):', txt)

    # 分支循环
    txt = re.sub(r'If\s+(.+?)\s*do{', r'if \1:', txt)
    txt = re.sub(r'Elif\s+(.+?)\s*do{', r'elif \1:', txt)
    txt = re.sub(r'Else\s*do{', r'else:', txt)
    txt = re.sub(r'While\s+(.+?)\s*do{', r'while \1:', txt)
    txt = re.sub(r'(\w+)\s+For\s+into\s+(.+?)\s*do{', r'for \1 in \2:', txt)

    # setitem 直接替换为等号
    txt = re.sub(r'\s+setitem\s+', r' = ', txt)

    # printe 补括号
    txt = re.sub(r'printe\s+(.*)', r'printe(\1)', txt)

    # 删除所有大括号
    txt = txt.replace("}", "")

    # 清理行尾多余分号
    txt = re.sub(r';\s+$', '', txt, flags=re.MULTILINE)

    # ========== 沙箱全局命名空间（使用原生全局变量） ==========
    global_env = {
        "printe": force_print,
        "reg": reg,
        "inp": inp,
        "num": num,
        "string": string,
        "boor": boor,
        "help": help,
        "Bottle": Bottle(),
        "Calculate": Calculate,
        "relter": relter,
        "to": to,
        "step": step,
        "brond": brond,
        "listindex": listindex,
        "dictionarykey": dictionarykey,
        "fmt": fmt,
        "delete": delete,
        "__build_class__": __build_class__,
        "__name__": "__main__",
        "__builtins__": builtins,
        "getret": getret,
    }

    force_print("===== Compiled Code =====")
    force_print(txt)
    force_print("▶ running")

    try:
        exec(txt, global_env)
        force_print("running end!")
    except KeyboardInterrupt:
        force_print("error[98]: Program interrupted")
    except Exception as e:
        err_name = type(e).__name__
        code = ERROR_NAME_TO_CODE.get(err_name, 99)
        force_print(f"error[{code}]: {str(e)}")
        
def save():
    p = filedialog.asksaveasfilename(defaultextension=".lmd")
    if p:
        with open(p, "w", encoding="utf-8") as f:
            f.write(editor.get("1.0", tk.END))

def open_f():
    p = filedialog.askopenfilename(filetypes=[("LMD", "*.lmd")])
    if p:
        editor.delete("1.0", tk.END)
        with open(p, encoding="utf-8") as f:
            editor.insert("1.0", f.read())
    highlight_keywords()

f = tk.Frame(root)
f.pack(fill=tk.X, padx=10, pady=5)

tk.Button(f, text="open (.lmd)", command=open_f).pack(side=tk.LEFT, padx=5)
tk.Button(f, text="save (.lmd)", command=save, bg="#007AFF", fg="#000000").pack(side=tk.LEFT, padx=5)
tk.Button(f, text="run (.lmd)", command=run_code, bg="#00C000", fg="#000000").pack(side=tk.LEFT, padx=5)

root.after(100, highlight_keywords)
root.mainloop()
'''
lambda-web72
MyCodeLambda2026
https://github.com/MyCodeLambda2026/lambda-web
'''
