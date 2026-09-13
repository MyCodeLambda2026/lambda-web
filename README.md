# Lambda Language VSCode Extension

自研 Lambda Custom Language 插件。

功能：
1. `.lmd` 文件语法高亮
2. 命令面板运行：`Lambda: Run current .lambda file`

## 使用前准备
1. 前往项目官网下载对应操作系统的 Lambda 解释器二进制程序
2. VSCode 设置 → 搜索 `lambda-customlang.interpreterPath`
3. 设置项填入你的 `lambda` / `lambda.exe` 完整路径

## 如何运行
- 打开后缀为 `.lmd` 的源码文件
- 右键菜单 → `Lambda: Run current .lambda file`

## 示例代码
```lambda
a setitem 10;
If a <> 10 do{
    printe "ok"
}
