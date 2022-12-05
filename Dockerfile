FROM python
RUN mkdir proyecto
COPY . proyecto
WORKDIR proyecto 
RUN pip install flask
CMD ["flask","run","-h","0.0.0.0","-p","80"] 
