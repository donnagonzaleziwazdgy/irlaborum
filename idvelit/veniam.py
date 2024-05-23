from rich.console import Console

console = Console()

def cprint(text, color):
    """Prints colored text to the console."""
    console.print(text, style=f"bold {color}")

cprint(f'\n>>> swap USDC | {address_wallet} | {error}', 'red')
