将本地内容写入到远程服务器中：`cat id_rsa.pub | ssh niu1 'cat - >> ~/.ssh/authorized_keys'`

在远程服务器执行命令时的变量使用：

```shell
ssh niu1 "B=3; echo $A; echo $B;"	# 只使用本地变量
ssh niu1 'B=3; echo $A; echo $B;'	# 只使用远程服务器变量
ssh niu1 "B=3; echo $A; echo \$B;"	# 同时使用本地变量和远程服务器变量
```

