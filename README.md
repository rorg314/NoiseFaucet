# NoiseFaucet

This repository contains the initial python prototype for generating a normalised noise value from a sha-256 hash.

It also contains models for a possible faucet website, where users send crypto and the site calculates a proportion of the amount to return (in the range say 0.9-1.1 of the recieved amount) using the noise value calculated from the transaction hash.

The system is highly speculative but does appear to be profitable given a large number of transactions, and iterations when calculating the noise value such that it averages to ~0.5.
