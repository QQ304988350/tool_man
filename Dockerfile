FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

COPY ./ /app/tool_man

RUN pip3 install -r /app/tool_man/requirements.txt

WORKDIR /app/tool_man
CMD nb run 