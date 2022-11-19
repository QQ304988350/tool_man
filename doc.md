docker run -itd -v /root/workspace/code/tool_man:/root/tool_man -v /root/.ssh:/root/.ssh -p 8080:8080 --name tool_man_dev registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

docker run -itd -v /root/workspace/code/tool_man:/root/tool_man -v /root/.ssh:/root/.ssh -p 8080:8080 --name tool_man_dev registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

docker commit tool_man_base registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest
docker push registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

```
cat << EOF > /etc/apt/sources.list
deb https://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ buster main non-free contrib
deb https://mirrors.aliyun.com/debian-security buster/updates main
deb-src https://mirrors.aliyun.com/debian-security buster/updates main
deb https://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb https://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
EOF
```
apt-get install locales
dpkg-reconfigure locales
486
apt-get install ttf-wqy-zenhei

apt-get install xfonts-intl-chinese wqy*

docker run -itd -v /root/workspace/code/tool_man:/root/tool_man -v /root/.ssh:/root/.ssh -p 8080:8080 --name tool_man_dev_ubuntu registry.cn-hangzhou.aliyuncs.com/304988350/ubuntu_dev:latest