FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man:latest

RUN chmod +x start.sh

COPY ./ /app/tool_man
