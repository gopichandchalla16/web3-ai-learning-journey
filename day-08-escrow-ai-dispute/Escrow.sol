// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title Escrow with AI Arbiter
/// @author Gopichand Challa
/// @notice Holds ETH between depositor and beneficiary.
///         An arbiter (human or AI) decides who gets paid.
contract Escrow {

    // ─── State ────────────────────────────────────────────
    address public depositor;
    address public beneficiary;
    address public arbiter;

    uint256 public amount;
    string  public disputeReason;

    bool public isDeposited;
    bool public isResolved;

    // ─── Events ───────────────────────────────────────────
    event Deposited(address indexed depositor, uint256 amount);
    event Released(address indexed beneficiary, uint256 amount);
    event Refunded(address indexed depositor, uint256 amount);
    event DisputeRaised(address indexed raisedBy, string reason);

    // ─── Constructor ──────────────────────────────────────
    constructor(address _beneficiary, address _arbiter) {
        require(_beneficiary != address(0), "Invalid beneficiary");
        require(_arbiter != address(0), "Invalid arbiter");
        depositor   = msg.sender;
        beneficiary = _beneficiary;
        arbiter     = _arbiter;
    }

    // ─── Functions ────────────────────────────────────────

    /// @notice Depositor locks ETH into escrow
    function deposit() external payable {
        require(msg.sender == depositor, "Only depositor can deposit");
        require(!isDeposited, "Already deposited");
        require(msg.value > 0, "Must send ETH > 0");
        amount      = msg.value;
        isDeposited = true;
        emit Deposited(msg.sender, msg.value);
    }

    /// @notice Either party can raise a dispute with a reason
    function raiseDispute(string calldata reason) external {
        require(
            msg.sender == depositor || msg.sender == beneficiary,
            "Only parties can raise dispute"
        );
        require(isDeposited,  "Nothing is deposited");
        require(!isResolved,  "Already resolved");
        require(bytes(reason).length > 0, "Reason cannot be empty");
        disputeReason = reason;
        emit DisputeRaised(msg.sender, reason);
    }

    /// @notice Arbiter releases ETH to beneficiary (work done)
    function release() external {
        require(msg.sender == arbiter, "Only arbiter");
        require(isDeposited && !isResolved, "Invalid state");
        isResolved = true;
        payable(beneficiary).transfer(amount);
        emit Released(beneficiary, amount);
    }

    /// @notice Arbiter refunds ETH to depositor (work not done)
    function refund() external {
        require(msg.sender == arbiter, "Only arbiter");
        require(isDeposited && !isResolved, "Invalid state");
        isResolved = true;
        payable(depositor).transfer(amount);
        emit Refunded(depositor, amount);
    }

    /// @notice View current escrow balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
