---
title: "启用 Google BBR 拥塞控制算法"
date: 2018-08-08T00:08:00
slug: enable-google-bbr-for-linux
categories: ["uncategorized"]
tags: ["algorithm", "Google", "Linux", "network"]
---

Google BBR (Bottleneck Bandwidth and RTT) 是一种新的拥塞控制算法，可以显著提升网络吞吐量和降低延迟。

## 前置要求

### 检查内核版本

BBR 需要 Linux 内核版本 4.9 或更高。

```bash
uname -r
```

如果输出的版本号大于等于 4.9，则可以继续。

## 启用 BBR

### 修改系统参数

编辑系统配置文件，添加 BBR 相关参数：

```bash
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
```

### 使配置生效

```bash
sysctl -p
```

## 验证配置

检查 BBR 是否已成功启用：

```bash
# 查看可用的拥塞控制算法
sysctl net.ipv4.tcp_available_congestion_control

# 查看当前使用的拥塞控制算法
sysctl net.ipv4.tcp_congestion_control
```

如果输出包含 `bbr`，说明配置成功。

## 参考资料

- [GitHub - google/bbr](https://github.com/google/bbr)
- [Google Cloud Blog - TCP BBR Congestion Control](https://cloud.google.com/blog/products/gcp/tcp-bbr-congestion-control-comes-to-gcp-your-internet-just-got-faster)
- [Google AI Research Publication](https://ai.google/research/pubs/pub45646)
