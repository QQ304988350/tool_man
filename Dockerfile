FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man:latest


RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
COPY ./ /app/tool_man
CMD cd /app/tool_man && nb run 