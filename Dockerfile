FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man:latest

RUN ls

COPY ./ /app/tool_man

RUN pip install -r /app/tool_man/requirements.txt -i https://mirrors.aliyun.com/pypi/simple
CMD cd /app/tool_man && nb run 