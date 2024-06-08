# pySpaceTrader

pySpaceTrader is a Python-based SDK for the space trading game, '**SpaceTraders**' where you can trade goods, explore space, and manage resources. 
This project is designed to provide a convenient way to access the game's API to play the game.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chatterchats/pySpaceTrader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pySpaceTrader
   ```
3. Create a Virtual Environment
    ```bash
    python -m venv .venv
    ```

4. Activate Virtual Environment
    ```bash
    # Windows
    ./.venv/Scripts/activate
   # Linux & Mac
   source ./.venv/bin/activate
    ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run utilize the SDK:
```py
from pySpaceTraders.client import SpaceTradersApi
from pySpaceTraders.models import enums

client = SpaceTradersApi()
token = client.register(symbol="NEWUSER", faction=enums.FactionSymbol.COSMIC)
my_agent = client.my_agent()

>>> my_agent
MyAgent(symbol="NEWUSER", headquarters="AA-BBB-CC", credits=175000, startingFaction="COSMIC", shipCount=2, accountId="abcdefghijklmnopqrstuvwxy")

>>> my_agent.symbol
'NEWUSER'
```

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, open an issue!.