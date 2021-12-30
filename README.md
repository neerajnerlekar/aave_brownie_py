1. Swap our ETH for WETH
2. Deposit some ETH (WETH) into Aave
3. Borrow some asset with the ETH collateral
   1. Sell that borrowed asset. (Short selling)
4. Repay everything back

Testing:

Integration test: Kovan
Unit tests: Mainnet-fork

      if you are not dealing with oracles, then you can fork mainnet to do the unit test. If dealing with oracles, it is easier to mock the responses of oracles on development environment.
