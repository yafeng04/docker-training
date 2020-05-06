FROM python:3.7

########## REQUIRED DEPENDENCIES ################
RUN mkdir ~/.pip && \
    cd ~/.pip/  && \
    echo "[global] \ntrusted-host =  pypi.douban.com \nindex-url = http://pypi.douban.com/simple" >  pip.conf

COPY src/ /opt/src
WORKDIR /opt/src

RUN pip install -r requirements.txt
CMD ["python", "app.py"]