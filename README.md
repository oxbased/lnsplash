

Welcome to the LnSplash wiki!

LnSplash is a splash page for your lightning node.


## Install 
1. `git clone git@github.com:wroscoe/oxbase_lnsplash.git`
2. Create your own `lnd.conf` and edit its variables to match your node setup. `cp ./lnd/example.lnd.conf ./lnd/lnd.conf`
3. Create your own `.env` and edit it to match your setup. `cp ./example.env ./.env`
4. Start your node `make prod`.



## Tutorials

### Edit the splash page. 
1. Edit the `./content/index.md` 


## TODO
- [ ] create web app that shows your public sats for the node
- [ ] allow a markdown to be shown along with node stats
- [ ] allow services to be exposed for your node (channel open, pay to contact)




## More Resources
* https://github.com/ruimarinho/docker-bitcoin-core
* lncm https://github.com/lncm/docker-lnd
* lnd instructions: https://docs.lightning.engineering/lightning-network-tools/lnd/get-started-with-lnd
* LND GRPC API: https://api.lightning.community/?python#lnd-grpc-api-reference
* Connect to lndrpc with python: https://github.com/lightningnetwork/lnd/blob/master/docs/grpc/python.md
* dockerized lndnode lightning-power-users https://github.com/lightning-power-users/bitcoin-lightning-docker
