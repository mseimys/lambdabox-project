rm -rf lambdabox-dist*
docker build --tag lambdabox lambdabox-backend/
id=$(docker create lambdabox echo)
docker cp $id:/var/task/python/lib/python3.8/site-packages lambdabox-dist
docker rm -v $id
cp -R lambdabox-backend/* lambdabox-dist/
cd lambdabox-dist
zip -r9 ../lambdabox-dist.zip .
cd ..
### UPDATE LAMBDA
export AWS_PROFILE=sandbox
aws lambda update-function-code --function-name lambdabox-django --zip-file fileb://lambdabox-dist.zip
