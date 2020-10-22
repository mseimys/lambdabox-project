FROM lambci/lambda:build-python3.8
COPY requirements.txt .
RUN pip install -r requirements.txt -t python/lib/python3.8/site-packages/
COPY . .
