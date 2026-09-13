const vscode = require('vscode');

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

    // -------- 运行命令 --------
    const runLambda = vscode.commands.registerCommand('lambda-customlang.runLambda', async function () {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage("没有打开编辑器");
            return;
        }
        const doc = editor.document;
        if (doc.languageId !== "lambda") {
            vscode.window.showErrorMessage("当前不是 .lmd(Lambda) 文件");
            return;
        }
        const filePath = doc.fileName;
        const config = vscode.workspace.getConfiguration("lambda-customlang");
        const binPath = config.get("interpreterPath");

        if (!binPath || binPath.trim() === "") {
            vscode.window.showErrorMessage("请在扩展设置填写 Lambda解释器 可执行文件完整路径\n示例：/xxx/Lambda.app/Contents/MacOS/Lambda");
            return;
        }

        let terminal = vscode.window.activeTerminal;
        if (!terminal) {
            terminal = vscode.window.createTerminal("Lambda");
        }
        terminal.show();
        terminal.sendText(`"${binPath}" "${filePath}"`);
    });

    context.subscriptions.push(runLambda);


    // -------- Hover悬浮文档 --------
    const hoverMap = {
        "Calculate": "**Calculate**\n内置计算工具类\n```\nCalculate.add(a,b)\nCalculate.minus(a,b)\nCalculate.times(a,b)\nCalculate.divide(a,b)\nCalculate.power(a,b)\n```",
        "Bottle": "**Bottle**\n容器工具，list / dict转换\n```\nBottle.lists(data)\nBottle.dictionary(data)\n```",
        "File": "**File**\n文件操作类\n```\nf setitem File(\"test.txt\",\"w\");\nf.write(\"hi\");\n```",
        "reg": "**reg(start,end)**\n生成数字序列，等价range",
        "step": "**step(x)**\n获取长度",
        "listindex": "**listindex(list,idx)**\n取列表元素",
        "dictionarykey": "**dictionarykey(dict,key)**\n取字典值",
        "num": "**num(var)**\n转为整数",
        "string": "**string(var)**\n转为字符串",
        "boor": "**boor(var)**\n转为布尔",
        "inp": "**inp(prompt)**\n读取用户输入",
        "delete": "**delete(var_name)**\n删除变量",
        "getret": "**getret()**\n获取函数返回值",
        "relter": "**relter(val)**\n设置返回值",
        "fmt": "**fmt(a,b,c)**\n拼接字符串",
        "ListFunc": "**ListFunc(start,end,step,r)**\n生成列表",
        "DictionaryFunc": "**DictionaryFunc(start,end,step,r)**\n生成字典",
        "printe": "**printe content**\n输出打印内容",
        "help": "**help()**\n打开语法帮助文档",
        "to": "**to**\n范围运算符",
        "If": "**If condition do{ ... }**\n条件判断",
        "Elif": "**Elif condition do{ ... }**\n否则如果",
        "Else": "**Else do{ ... }**\n否则分支",
        "While": "**While condition do{ ... }**\nwhile循环",
        "For": "**For var into iter do{ ... }**\nfor循环",
        "Try": "**Try do{ ... } Except do{ ... }**\n异常捕获",
        "Except": "异常捕获分支",
        "setitem": "**var setitem value;**\n变量赋值",
        "true": "布尔真值",
        "false": "布尔假值"
    };

    const hoverProvider = vscode.languages.registerHoverProvider('lambda', {
        provideHover(document, position) {
            const word = document.getText(document.getWordRangeAtPosition(position));
            if (hoverMap[word]) {
                return new vscode.Hover(hoverMap[word]);
            }
            return undefined;
        }
    });
    context.subscriptions.push(hoverProvider);


    // -------- 自动补全列表 --------
    const completionProvider = vscode.languages.registerCompletionItemProvider('lambda', {
        provideCompletionItems() {
            const items = [];

            // 关键字
            items.push(new vscode.CompletionItem("If", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("Elif", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("Else", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("While", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("For", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("into", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("perform", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("Try", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("Except", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("setitem", vscode.CompletionItemKind.Keyword));
            items.push(new vscode.CompletionItem("true", vscode.CompletionItemKind.Constant));
            items.push(new vscode.CompletionItem("false", vscode.CompletionItemKind.Constant));

            // 内置类
            items.push(new vscode.CompletionItem("Calculate", vscode.CompletionItemKind.Class));
            items.push(new vscode.CompletionItem("Bottle", vscode.CompletionItemKind.Class));
            items.push(new vscode.CompletionItem("File", vscode.CompletionItemKind.Class));
            items.push(new vscode.CompletionItem("ClassesAndFunctionsAttributes", vscode.CompletionItemKind.Class));

            // 内置函数
            items.push(new vscode.CompletionItem("reg", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("fmt", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("num", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("string", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("boor", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("delete", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("getret", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("relter", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("step", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("listindex", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("dictionarykey", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("printe", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("inp", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("help", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("to", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("ListFunc", vscode.CompletionItemKind.Function));
            items.push(new vscode.CompletionItem("DictionaryFunc", vscode.CompletionItemKind.Function));

            return items;
        }
    });
    context.subscriptions.push(completionProvider);

}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
