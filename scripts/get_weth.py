from scripts.helpful_scripts import get_account
from brownie import interface, network, config


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH.

    To achieve that we need to interact with the WETH contract. For that we need,

    ABI
    Contract Address

    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])

    # can certainly use get_contract function, but since we are not using any mocks, we will be using the contracts from the mainnet-fork.
    # it is a good practice to use the get_contract function.
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    tx.wait(1)
    print("Received 0.1 Weth tokens")

    return tx
