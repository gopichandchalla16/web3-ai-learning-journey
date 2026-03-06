// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Day 03 - Gopichand's first Solidity smart contract
// Concept: State variables, constructor, functions, msg.sender

contract HelloWorld {
    // State variable - stored permanently ON-CHAIN
    string public message;
    address public owner;

    // Constructor runs ONCE when contract is deployed
    constructor(string memory _message) {
        message = _message;
        owner = msg.sender; // whoever deploys = owner
    }

    // Function to update the message (costs gas)
    function updateMessage(string memory _newMessage) public {
        message = _newMessage;
    }

    // View function - FREE to call (no gas)
    function getMessage() public view returns (string memory) {
        return message;
    }
}
