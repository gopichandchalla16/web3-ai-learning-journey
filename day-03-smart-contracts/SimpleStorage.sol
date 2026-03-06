// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Day 03 - SimpleStorage contract
// Concept: uint, set/get pattern, mappings

contract SimpleStorage {
    // State variables
    uint256 public storedNumber;
    address public owner;
    mapping(address => uint256) public userNumbers;

    constructor() {
        owner = msg.sender;
        storedNumber = 0;
    }

    // Set a number - changes state = costs gas
    function setNumber(uint256 _number) public {
        storedNumber = _number;
        userNumbers[msg.sender] = _number; // store per wallet
    }

    // Get number - free (view function)
    function getNumber() public view returns (uint256) {
        return storedNumber;
    }

    // Get number for a specific wallet
    function getMyNumber() public view returns (uint256) {
        return userNumbers[msg.sender];
    }
}
