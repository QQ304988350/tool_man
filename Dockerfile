FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

COPY ./ /app/tool_man

#RUN pip install -r /app/tool_man/requirements.txt -i https://mirrors.aliyun.com/pypi/simple
ENV PATH="$PATH:/root/.local/bin"
WORKDIR /app/tool_man
RUN poetry install 
CMD poetry run nb run 