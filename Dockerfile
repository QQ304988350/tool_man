FROM registry.cn-hangzhou.aliyuncs.com/304988350/tool_man_base:latest

COPY ./ /app/tool_man

#RUN pip install -r /app/tool_man/requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN source /root/.bashrc
RUN poetry install 
CMD cd /app/tool_man && poetry run nb run 