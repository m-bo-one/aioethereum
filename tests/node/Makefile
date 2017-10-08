NODE=geth
DATADIR1=./testnet
KEYSTORE1=$(DATADIR1)/keystore
LOG_FILE1=$(DATADIR1)/info.log
IPC_FILE1=$(DATADIR1)/geth.ipc
PID_FILE1=$(DATADIR1)/run.pid
PSWD_FILE=./pswd.txt
PSWD=$(shell cat $(PSWD_FILE))
AMOUNT=1

NODE_PORT = 30305
HOST = 'localhost'
RPC_PORT = 8545
WS_PORT = 8546
APIS = 'eth,web3,net,personal,db,shh,txpool,miner,admin'

BASE_ARGS=--dev \
	--nodiscover \
	--networkid=15 \
	--maxpeers=10 \
	--verbosity=3 \
	--datadir=$(DATADIR1)

ARGS1=$(BASE_ARGS) \
	--port=$(NODE_PORT) \
	--rpc \
	--rpcaddr=$(HOST) \
	--rpcport=$(RPC_PORT) \
	--rpcapi=$(APIS) \
	--rpccorsdomain="*" \
	--ws \
	--wsaddr=$(HOST) \
	--wsport=$(WS_PORT) \
	--wsapi=$(APIS) \
	--wsorigins="*" \
	--mine \
	--minerthreads=1

console:
	$(NODE) $(BASE_ARGS) attach $(IPC_FILE1)

sendfrom:
	$(NODE) $(BASE_ARGS) --exec 'personal.unlockAccount(eth.coinbase, "$(PSWD)", 2); quickSend(eth.coinbase, "$(ADDRESS)", $(AMOUNT));' attach $(IPC_FILE1)

account:
	$(NODE) $(BASE_ARGS) --password=$(PSWD_FILE) account new

waitmoney:
	@if [ "$(shell ls -A $(KEYSTORE1))" = "" ]; then\
		$(MAKE) account;\
	fi
	$(NODE) $(BASE_ARGS) --exec 'hasMoney = false; while (!hasMoney) {var balance = eth.getBalance(eth.coinbase); if (balance > 0) {hasMoney = true; break;}; admin.sleep(1)}; hasMoney;' attach $(IPC_FILE1)

coinbase:
	@if [ "$(shell ls -A $(KEYSTORE1))" = "" ]; then\
		$(MAKE) account;\
	fi
	$(NODE) $(BASE_ARGS) --exec 'eth.coinbase;' attach $(IPC_FILE1)

start:
	mkdir -p $(DATADIR1)
	@if [ "$(shell ls -A $(KEYSTORE1))" = "" ]; then\
		$(MAKE) account;\
	fi
	nohup $(NODE) $(ARGS1) ${} > $(LOG_FILE1) 2>&1 & echo $$! > $(PID_FILE1)

stop: $(PID_FILE1)
	-kill -9 `cat $<` && `rm $<`

clean:
	find $(DATADIR1)/* -not -name 'keystore' -delete

destroy:
	rm -rf $(DATADIR1)