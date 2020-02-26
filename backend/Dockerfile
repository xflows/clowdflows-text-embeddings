FROM xflows/clowdflows-backend:latest

# YAP prolog installation
RUN apt-get update && \
    apt-get install -y build-essential cmake && \
    cd .. && \
    git clone https://github.com/vscosta/yap-6.3.git && \
    cd yap-6.3 && \
    git submodule init && \
    git submodule update && \
    ./configure && \
    make && \
    make install

COPY packages /usr/src/app/packages
RUN pip install -r packages/requirements.txt



