FROM python

LABEL Maintainer="vaka.narasimha.reddy@gmail.com" \
      Name="mac-customer" Version="1.0.0"

RUN mkdir -p /usr/nvaka/bin && \
    pip install requests

COPY mac-customer.py /usr/nvaka/bin/

WORKDIR /usr/nvaka
