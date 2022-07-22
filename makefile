all:
	
makeRunningContainer: 
	docker run -e DISCORD_TOKEN=[YOUR TOKEN] order-bot-server

makeImage:
	docker build -t order-bot-server .