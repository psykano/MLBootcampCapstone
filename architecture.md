## Architecture

#### Web Application

The web application will run on AWS since it is the industry standard cloud solution. It will use Docker for containerization for scalability. A docker instance will run Next.js which is comprised of Node.js for the back-end and React for the front-end.

#### Machine Learning Server

The original plan was to use a cloud-based GPU server, however, upon further research there do not exist any cloud-based GPU solutions that bill by usage which makes this prohibitively expensive since you're billed based on how long the instance(s) are running.

So, it is using an M1 Macbook Pro on a local network which is running FastAPI, a Python web framework which supports multithreading and asynchronous functionality in a server.

#### Database

The data, which is solely comprised of images, will be stored on Cloudinary's image/video cloud-based CDN since it can easily scale based on usage.

#### Cost

Since the web application runs on AWS the cost will be able to scale based on usage. Initially, the cost will be the usage of a "Micro" instance. 

On the other hand, scalability is not currently planned for the Machine Learning Server due to GPU cost and availability. Should the machine learning server network need to be scaled then it would be possible to deploy multiple GPU servers running the FastAPI python application connected through a load balancer (which could be run on AWS).

For the database, its pricing can scale based on usage. Initially, it's usage will be in the "Free" tier.