## Installing and running an API through `ngrok`

1. Install `ngrok`
- MacOS
```sh
brew install ngrok
```

- Windows
```sh
choco install ngrok
```

- Linux
```sh
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
	| sudo tee /etc/apt/sources.list.d/ngrok.list \
	&& sudo apt update \
	&& sudo apt install ngrok
```

2. Add Token Configuration
```sh
ngrok config add-authtoken <your_token>
```

3. Deploying online
```sh
ngrok http http://localhost:8080
```
> [!NOTE]  
> Assuming 8080 is the local port where you're running your application. Change it for your own data.