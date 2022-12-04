FROM amazonlinux:2

# Install Python
RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all

# Set up PIP and Venv
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install virtualenv
RUN python3.7 -m venv base
RUN source base/bin/activate

# # Update machine
# RUN yum update -y

# Install required libraries
# RUN yum install -y curl which zip
# RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel wget
# RUN yum install -y tar
# RUN cd /opt && wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
# RUN yum install -y gzip make
# RUN cd /opt && ls && pwd && tar zxvf /opt/Python-3.9.6.tgz
# RUN cd /opt/Python-3.9.6 \
#     && ./configure --enable-optimizations \
#     && make altinstall \
#     && rm -f /opt/Python-3.9.6.tgz

# RUN python3.9 -m pip install --upgrade pip

# RUN python3.9 -m pip install virtualenv
# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt -t ./python

# Zip it up for deployment.
RUN zip -r layer.zip ./python/
ENTRYPOINT ["/bin/bash", "-l"]