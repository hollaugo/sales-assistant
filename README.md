# sales-assistant
The Sales assistant is a Langchain Agent that can assist Sales representatives and Sales engineers and other Sales folks to get access to Salesforce via a natural language. The agent can do the following 
- Access Salesforce Knowledge Articles 
- Access Salesforce Opportunities 
- Answer questions about an Account by accessing an Account's related records 
- Create a case record when a request is made

The Sales agent is a combination of Langchain and Slack running on FastAPI server based on the Langserve library. 

## Installation 

### Setup Salesforce Developer Edition 
- Sign up for Salesforce Developer Edition by clicking [here](https://developer.salesforce.com/signup)
- Setup your Knowledge Management by going to Setup > Service Setup > Knowledge Setup
- Add Articles to your knowledgebase for test 
- Get the Salesforce username, password and instance, store in a .env file

### Setup Slack 
- Create a new Slack app by visiting [Slack Developer Site](https://api.slack.com/apps) > Click on "Create App"
- Select Manifest option and use the slack-app-manifest.json as your app manifest
- Install app into your workspace, get your Slack bot token from the Oauth section and the signing secret from the Basic Information section of your app page

#### Load environment variables
- Change the .env.example to .env and add your variables



### Install Dependencies 
```bash
pip install -U langchain-cli
pip install python-dotenv
pip install simple-salesforce
pip install slack_bolt
```


## Adding langchain packages
```bash
# adding packages from 
# https://github.com/langchain-ai/langchain/tree/master/templates
langchain app add $PROJECT_NAME

# adding custom GitHub repo packages
langchain app add --repo $OWNER/$REPO
# or with whole git string (supports other git providers):
# langchain app add git+https://github.com/hwchase17/chain-of-verification

# with a custom api mount point (defaults to `/{package_name}`)
langchain app add $PROJECT_NAME --api_path=/my/custom/path/rag
```

Note: you remove packages by their api path

```bash
langchain app remove my/custom/path/rag
```


## Setup LangSmith (Optional)
LangSmith will help us trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

## Launch Application

```bash
langchain serve
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your LangServe app.

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-langserve-app
```

If you tag your image with something other than `my-langserve-app`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `OPENAI_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 my-langserve-app
```
