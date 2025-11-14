# C++ Markdown 测试文章

这是一篇测试 Markdown 解析功能的文章。

## 代码高亮测试

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    
    for (const auto& num : nums) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## 数学公式测试

行内公式：$E = mc^2$

块级公式：

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$

## 列表测试

### 无序列表
- 第一项
- 第二项
  - 子项 1
  - 子项 2
- 第三项

### 有序列表
1. 第一步
2. 第二步
3. 第三步

## 表格测试

| 特性 | HTML | Markdown |
|------|------|----------|
| 易读性 | 低 | 高 |
| 编写速度 | 慢 | 快 |
| 功能性 | 强 | 中等 |

## 引用测试

> 这是一段引用文本。
> 可以包含多行内容。

## 强调测试

**粗体文本** 和 *斜体文本*

## 链接测试

访问 [GitHub](https://github.com) 获取更多信息。

---

这就是 Markdown 功能的完整演示！
