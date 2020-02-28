FROM xflows/clowdflows-backend:latest

# YAP prolog installation
RUN apt-get update && \
    apt-get install -y build-essential cmake wget && \
    cd .. && \
    wget https://github.com/vscosta/yap-6.3/archive/yap-6.3.3.tar.gz && \
    tar xvzf yap-6.3.3.tar.gz && \
    cd yap-6.3-yap-6.3.3/ && \
    mkdir arch && cd arch && \
    export CXXFLAGS=-fpermissive && ../configure --enable-tabling=yes --with-readline=no && \
    make && \
    make install

# Java
RUN apt-get update && \
    apt-get install -y default-jre

RUN apt-get update && \
    apt-get install graphviz
    
COPY packages /usr/src/app/packages
RUN pip install -r packages/requirements.txt


