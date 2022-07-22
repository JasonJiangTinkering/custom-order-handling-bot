all:
	
makeRunningContainer: 
	docker run order-bot-server

makeImage:
	docker build -t order-bot-server .