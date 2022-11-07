## 基础30讲例题、习题

### [0、公式](基础30讲例题、习题/0、公式/0、公式.html)

### [1、高等数学预备知识](基础30讲例题、习题/1、高等数学预备知识/1、高等数学预备知识.html)

### [2、数列极限](基础30讲例题、习题/2、数列极限/2、数列极限.html)

### [3、函数极限与连续性](基础30讲例题、习题/3、函数极限与连续性/3、函数极限与连续性.html)

### [4、一元函数微分学的概念与计算](基础30讲例题、习题/4、一元函数微分学的概念与计算/4、一元函数微分学的概念与计算.html)

### [5、一元函数微分学的几何应用](基础30讲例题、习题/5、一元函数微分学的几何应用/5、一元函数微分学的几何应用.html)

### [6、中值定理](基础30讲例题、习题/6、中值定理/6、中值定理.html)

### [7、零点问题与微分不等式](基础30讲例题、习题/7、零点问题与微分不等式/7、零点问题与微分不等式.html)

### [8、一元函数积分学的概念与计算](基础30讲例题、习题/8、一元函数积分学的概念与计算/8、一元函数积分学的概念与计算.html)

### [9、一元函数积分学的几何应用](基础30讲例题、习题/9、一元函数积分学的几何应用/9、一元函数积分学的几何应用.html)

### [10、积分等式与积分不等式](基础30讲例题、习题/10、积分等式与积分不等式/10、积分等式与积分不等式.html)

### [11、多元函数微分学](基础30讲例题、习题/11、多元函数微分学/11、多元函数微分学.html)

### [12、二重积分](基础30讲例题、习题/12、二重积分/12、二重积分.html)

### [13、常微分方程（多元微积分的应用）](基础30讲例题、习题/13、常微分方程（多元微积分的应用）/13、常微分方程（多元微积分的应用）.html)

### [15、数一、数二专题内容](基础30讲例题、习题/15、数一、数二专题内容/15、数一、数二专题内容.html)





























翻译数据地址：` /mnt/server67/database/forged_sourcedata`











#### 疑问

变量 `m / mp` 前缀一般代表什么含义？

`readfile.h` 中 `CReadFile` 类，`read()` 方法中的 `while` 循环判断结尾不是 `\n` 是何意？

`tools.h` ： `82行` 全局变量何解？

```cpp
static void split_1(const wstring& str, vector<wstring>& tokens, wstring delimiter = L" ")
{
    wstring ss = str;
    tokens.clear();
    while(ss.find_first_of(delimiter) != wstring::npos)
    {
        int beg = ss.find_first_of(delimiter);
        int len = delimiter.length();
        wstring subss = ss.substr(0,beg);
        if(subss.length() > 0 )
        {
            tokens.push_back(subss);
            if(beg+len < ss.length()){ss = ss.substr(beg+len);}
            else{ss= L"";break;}
        }
        else
        {
            if(beg+len < ss.length()){ss = ss.substr(beg+len);}
            else{ss= L"";break;}
        }
    }
    if(tokens.size() > 0 && ss != L"")
    {
        tokens.push_back(ss);
    }
}
```











### 爬虫

```
https://www.b2bers.com/big5/language/spokenen/spokenen.html
與老外溝通的40招		已完成
https://www.poemlife.com/forum.php?mod=viewthread&tid=989053&extra=page%3D1&page=1
https://enclub.com/
https://chinese.despertandome.com/
```



```
https://www.dedyy.com/swyy/
http://kan.iask.sina.com.cn/area/North-America.html
https://china.legalbusinessonline.com/news-list	
```

















# 日语单语数据

[第一次清洗](#第一次清洗)

[第二次清洗](#第二次清洗)

[问题分析](#问题分析)

[第三次清洗](#第三次清洗)

[第四次清洗](#第四次清洗)





## 第一次清洗

#### 清洗对象：

源数据（`ja.deduped`）

#### 清洗结果：

清洗前数据：`ja.deduped`：`174G`

保留数据：`ja.deduped.out`：`158G`

丢弃数据：`ja.deduped.out.discard`：`16G`

***注***：清洗后数据所在位置为 `/mnt/server142/weigf/clean_data_1`

#### 筛掉的数据特征：

* 空行
* 没有日语的行
* 含有`"` `“` `《` `(` `（` `[` `«`的总个数，与含有 `"` `”` `》` `)` `）` `]` `»` 的总个数不相等的行

#### 留下的数据做了一点微小处理：

* 删除了行首和行尾的空格







## 第二次清洗

#### 清洗对象：

源数据（`ja.deduped`）

#### 清洗结果：

清洗前数据：`ja.deduped`：`174G`

保留数据：`ja.deduped.out`：`152G`

丢弃数据：`ja.deduped.out.discard`：`22G`

***注***：清洗后数据所在位置为 `/mnt/server142/weigf/clean_data_2`

#### 相对第一次做了微小修改：

* 主要针对第一次清洗的第 3 个条件，通过观察，扩大了成对符号的范围，扩大后的范围为：`"` `“` `《` `(` `（` `[` `«` `【` `「` `『` 和 `"` `”` `》` `)` `）` `]` `»` `】` `」` `』` 。






## 问题分析

上述筛掉数据的第 3 个条件我们是通过总个数来筛选的，这样的话有的数据是筛不掉的，如：

* `筛【数)据`；虽然 `左开` 的符号和 `右开` 的符号总数相等，但是左开和右开的符号并不能匹配
* `筛）数（据`；总数相等，符号匹配，但是符号的位置不匹配（出现顺序不匹配）
* 其它与第 3 个筛选条件无关的问题（待发现）


下次清洗数据就直接拿第二次清洗后的保留数据进行清洗了。






## 第三次清洗

#### 清洗对象：

第二次清洗后保留的数据（`ja.deduped.out`）

#### 清洗结果：

清洗前数据：`ja.deduped.out`：`152G`

保留数据：`ja.deduped.out.out`：`151G`

丢弃数据：`ja.deduped.out.out.discard`：`1.5G`

***注***：清洗后数据所在位置为 `/mnt/server142/weigf/clean_data_3`

#### 洗掉的数据特征：

* 针对上面提到的 3 个问题，主要解决了前两点等与前后匹配相关的问题


#### 解决方法：

通过栈模拟，逐句遍历，严格筛掉了前后不匹配的行





## 第四次清洗

#### 清洗对象：

第三次清洗后保留的数据（`ja.deduped.out.out`）

#### 清洗结果：

清洗前数据：`ja.deduped.out.out`：`151G`

保留数据：`ja.deduped.out.out.out`：`143G`

丢弃数据：`ja.deduped.out.out.out.discard`：`7.4G`

***注***：清洗后数据所在位置为 `/mnt/server142/weigf/clean_data_4`

#### 洗掉的数据特征：

* 以 `,` 或  `，` 或 `:` 或 `：` 或 `、` 结尾的行
* `<` 与 `>` 不匹配的行

