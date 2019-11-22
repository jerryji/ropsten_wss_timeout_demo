if (typeof process.env.PROJECT_ID === 'undefined' || process.env.PROJECT_ID == null) {
    console.log('Error: env variable PROJECT_ID not found');
    return process.exit(1);
}
const PROJECT_ID = process.env.PROJECT_ID;

const Web3 = require('web3');
const web3 = new Web3('wss://ropsten.infura.io/ws/v3/' + PROJECT_ID);
const contractJson = require('./ABI_Ropsten.json');
const ethwalldataContract = new web3.eth.Contract(contractJson.abi, contractJson.contractAddress);

let fromBlock = 6807400;
console.log('fromBlock = ' + fromBlock + '\n');

ethwalldataContract.getPastEvents('EthUpdate', { fromBlock: fromBlock, toBlock: 'latest' },
    (err, evts) => { evts.slice(0, 2).map(console.log); }
);

//ethwalldataContract.events.EthUpdate({ fromBlock: fromBlock },
//    (err, evts) => { evts.slice(0, 2).map(console.log); }
//);
