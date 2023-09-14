import sys

from getpass import getpass


from src.banner import DisplayBanner
from src.login import Login
from src.login import Register
from src.entry.entry import EntryManager
from src.vault.vault import VaultManager
from rich import print as printC
from rich.console import Console
console = Console()

if len(sys.argv) <= 1:
    sys.exit(0)

argument = sys.argv[1]

DisplayBanner()

if argument == "--add" or argument == '--a':
    (name, encryptionKey, phrase)= Login()

    EntryManager().AddNewEntry(encryptionKey=encryptionKey, phrase=phrase)


elif argument == "--get" or argument == '--g':
    (name, encryptionKey, phrase) = Login()

    EntryManager().RetrieveEntry(encryptionKey=encryptionKey, phrase=phrase)

elif argument == "--init" or argument == "--i":
    (name, masterPassword) = Register()

    VaultManager().ConfigureVault(name, masterPassword)
