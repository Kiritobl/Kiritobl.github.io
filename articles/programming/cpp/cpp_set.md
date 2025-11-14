# SET
维持元素唯一、**有序**集合
### 初始化

```c++
#include <set>

// 1. 空集合（默认按升序排序）
set<int> s1;

// 2. 初始化列表（C++11及以上）
set<int> s2 = {3, 1, 4, 1, 5};  // 自动去重并排序，结果：{1, 3, 4, 5}

// 3. 复制构造 (深copy，和vector一样，= 为浅copy) 
set<int> s3(s2);  // s3 是 s2 的副本

// 4. 自定义排序（降序）
set<int, greater<int>> s4 = {3, 1, 4};  // 结果：{4, 3, 1}

```

### 增删改查

```c++
set<int> s;
s.insert(5);       // 插入单个元素
s.insert({2, 8});  // 插入初始化列表（C++11）
s.insert(s2.begin(), s2.end());  // 插入另一个容器的区间
// 注意：插入重复元素会被忽略
s.insert(5);  // 无效果，因为 5 已存在


```
```c++
// ① 删除指定值的元素（返回删除的个数，set 中只能是 0 或 1）
set<int> s = {1, 2, 3, 4, 5};
s.erase(3);  

// ② 删除迭代器指向的元素
auto it = s.find(2);

 ···········⭐begin()是头位置，end()是尾后一位，和python中的前闭后开一致，find没找到会返回s.end()而不是错误注意！！····························

if (it != s.end()) {  
    s.erase(it);      
}

s.erase(s.begin(), s.end());  // 清空集合

```
```c++
set<int> s = {1, 3, 5};

s.empty();      // 判断是否为空（返回 bool）
s.size();       // 返回元素个数（当前为 3）
s.clear();      // 清空所有元素
s.count(3);     // 统计元素出现的次数（set 中只能是 0 或 1）

// 迭代器遍历（正序）
for (auto it = s.begin(); it != s.end(); ++it) {
    cout << *it << " ";
}

// 反向遍历（需要 rbegin()/rend()）
for (auto it = s.rbegin(); it != s.rend(); ++it) {
    cout << *it << " ";
}
```

# unordered_set
```c++
unordered_set<int> us = {1, 2, 3, 4, 5}; 
// 无序set，用hash表实现，查找O(1)，对应python中的set
// set的查找复杂度为(log n)，用红黑树实现，对应python第三方库里的SortedSet
```

