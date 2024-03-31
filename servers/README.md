## How to build the servers

#### Next.js front-end server

In `nextjs-cap-server` directory.

Create `.env.local` file with the following:
```
API_KEY=<your_api_secret>
API_URL=<your_api_url>
```

To run locally, 

- First install Node.js 18.17 or later
- Then `npm install` to install packages
- Then `npm run dev` to run the server
- Visit http://localhost:3000 to see the server running locally

To run with docker,

- First install Docker
- Then run `docker build -t nextjs-cap .` to build the docker image
- Then run `docker run -p 3000:3000 nextjs-cap` to run the server with docker
- Visit http://localhost:3000 to see the server running locally

#### Machine learning server

In `sdlora` directory.

First, create a Cloudinary account: https://cloudinary.com/ and create an API key.

Create `.env` file with the following:
```
API_KEY = <your_api_secret>
BASE_PATH = <your_server_path>
CL_CLOUD_NAME = <cloudinary_cloud_name>
CL_API_KEY = <cloudinary_api_key>
CL_API_SECRET = <cloudinary_api_secret>
```

To run locally,

- Run `pip install requirements.txt` to install required python packages 
- Run `pip install git+https://github.com/natsunoyuki/diffuser_tools` to install required package
- Create SSL credentials and store as `fullchain.pem` and `privkey.pem`
- Run `python main.py` to start the server
- Visit `https://localhost:8000` to see the server running locally