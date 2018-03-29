# SSH 简化配置指南

一般来说，ssh的命令是 ssh user@host -p <port>,
然后可能还需要再输入密码。这样非常繁琐，因此需要一种比较简单的方法来实现快速连接ssh

## 实现 ssh <name> 功能
创建/修改 ~/.ssh/config 文件，添加
```bash
Host <name>
    Hostname xxx.xxx.xxx.xxx
    Port     xxxxx
    User     username
```
其中 name 是你希望这个ssh连接的简化名字，Hostname是你的主机公网ip或者域名，username是你要连接的主机的用户账户，一般应当避免使用root账户连接

## SSH重连
如果你需要密码才能登录ssh，那么这个设置可以带来极大的简便  
以下设置可以做到重用连接，只有在第一次登录的时候会创建新的连接，后续的会话都可以重用这个已经存在的连接。
```
Host *
    ControlMaster auto
    ControlPath /tmp/ssh_mux_%h_%p_%r
    ControlPersist 600
```
注意这一段设置应当放在最前面，* 表示对下面的其它项都生效。
- ControlMaster auto 这个选项告诉 SSH 客户端尝试重用现有的连接（master connection）
- ControlPath 指定了这个连接的 socket 保存的路径，这里配置的是在 /tmp 目录，实际上可以在任何有读写权限的路径下。/tmp/ssh_mux_%h_%p_%r 配置了 socket 文件名，%h 表示远程主机名（host），%p 表示远程 SSH 服务器的端口（port），%r 表示登录的远程用户名（remote user name）。这些 socket 可以随时删掉（rm），删除后首次会话又会创建新的 master 连接。曾经遇到过这种情况，本地断网了，打开的几个远程终端都卡死，网络恢复后也一直这样，甚至打开新的终端也登录不上。这个时候只需要把之前的 socket 文件都删掉，重新登录就可以了
- ControlPersist 这个选项比较重要，表示在创建首个连接（master connection）的会话退出后，master 连接仍然在后台保留，以便其他复用该连接的会话不会出现问题。这个特性在使用 Git 的时候就非常有用，在频繁提交和拉代码的时候，每次 SSH 会话都是很短暂的，如果 master 连接能保持在后台，后续的操作就会如丝般顺滑。

## 密钥登录/免密码登录
网上文章很多了，主要就是密钥对的生成，然后添加到本地.ssh文件夹  
>tips:如果需要登录不同的主机，可以更改密钥的名字，然后在上面所说的config文件的每个Host项目中指定使用哪个密钥。应当避免使用同样的密钥。

[引用](http://liyangliang.me/posts/2015/03/reuse-ssh-connection/)

