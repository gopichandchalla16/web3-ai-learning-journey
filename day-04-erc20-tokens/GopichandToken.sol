// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// ============================================
// Day 04 - Gopichand Challa
// ERC-20 Token: GopichandToken ($GOPI)
// Web3 AI Learning Journey
// github.com/gopichandchalla16/web3-ai-learning-journey
// ============================================

contract GopichandToken {

    // Token Info
    string public name = "GopichandToken";
    string public symbol = "GOPI";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    address public owner;

    // Core storage - who owns how many tokens
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Events - permanently logged on blockchain
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Deploy: mint all tokens to deployer
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Send tokens to another address
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[msg.sender] >= _value, "Not enough tokens");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Allow someone else to spend your tokens
    function approve(address _spender, uint256 _value) public returns (bool) {
        allowance[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    // Spend approved tokens on behalf of someone
    function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid address");
        require(balanceOf[_from] >= _value, "Not enough tokens");
        require(allowance[_from][msg.sender] >= _value, "Not approved");
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Owner can create more tokens (mint)
    function mint(address _to, uint256 _value) public {
        require(msg.sender == owner, "Only owner can mint");
        totalSupply += _value;
        balanceOf[_to] += _value;
        emit Transfer(address(0), _to, _value);
    }

    // Burn (destroy) your own tokens
    function burn(uint256 _value) public {
        require(balanceOf[msg.sender] >= _value, "Not enough tokens");
        balanceOf[msg.sender] -= _value;
        totalSupply -= _value;
        emit Transfer(msg.sender, address(0), _value);
    }
}
