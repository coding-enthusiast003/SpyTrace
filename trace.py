import requests
import time
import os
from rich.console import Console  # For rich console output
from rich.text import Text # For rich text formatting
from pyfiglet import Figlet # For creating ASCII art text
from options import phone,ip_trace  # Import the phone function from options.py


console= Console()





def banner1():
    """
    Displays a colorful UI using Rich and PyFiglet.
    """
    

    # Create a Figlet instance with a specific font
    fig = Figlet(font='slant')  # Try 'standard', 'slant', 'big', etc.

    # Create colored segments
    py_text = Text(fig.renderText("Spytrace"), style="bold green")
    # Print them together
    console.print(py_text)
    

    console.print("[bold green]!!! Welcome to SpyTrace !!![/bold green]")

    console.print("[bold green][ + ] Code by Subham Das (Coding-enthusiast003) [ + ] [/bold green]")
            
    console.print("\n" + "-" * 50)  # Divider line

 
def banner2():
    banner = r'''
             .-""""""-.
           .'  \_    \_  '.                       ------------------------------------------------------
          /    (o)  (o)    \                       
         |        __        |                       [ + ] Code by Subham Das  [ + ]
          \      '----'     / 
           '.              .'                     -------------------------------------------------------       
             '-..........-'

     [ watching · searching · correlating ]
    '''

    console.print(banner, style="bold green")

def main():
    time.sleep(0.5)
    banner1()
    while True:
        choice = console.input("[bold blue]Select an key to continue (or q to exit): [/bold blue]")
        if choice == "q":
            console.print("[!] Exiting.", style="bold red")
            time.sleep(2)
            break
        else:
            console.print("[ 1 ] Phone Number : ", style="bold green")
            console.print("[ 2 ] IP Address : " , style="bold green")
            choice = console.input("[bold green]Enter the options to trace: [/bold green]")
            time.sleep(1)


            if choice == "1":
                banner2()
                phone()
                print()
                console.input("[bold blue]Select an option to continue (or any other key to exit): [/bold blue]")

            elif choice == "2":
                banner2()
                ip_trace()
                print()
                
            
            else:
                pass




if __name__ == "__main__":
    main()

