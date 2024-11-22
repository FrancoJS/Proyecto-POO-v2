from datetime import datetime
from rich.console import Console
from utils.messages_templates import show_confirmation


class EmpleoyeeData: 
    
    def __init__(self) -> None:
        self.console = Console()
    
    def get_data(self):
        experience = self.get_experience(self.console)
        hire_date = self.get_hire_date(self.console)
        salary = self.get_salary(self.console)
        return experience, hire_date, salary
    
    @staticmethod
    def get_experience(console, error:bool = False) -> int:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            try:
                experience = int(console.input("[bold cyan]Experiencia (en años): "))
                if experience < 0 or experience > 50:
                    console.print("[bold red]La experiencia debe ser un valor entre 0 y 50 años.")
                    error = True
                    continue
                
                return experience
            except ValueError:
                console.print("[bold red]Debe ingresar un número válido para la experiencia.")
                error = True
    
    @staticmethod
    def get_hire_date(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            hire_date = console.input("[bold cyan]Fecha inicio contrato (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(hire_date, "%Y-%m-%d")
                return hire_date
            except ValueError:
                console.print("[bold red]Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
                error = True
    
    @staticmethod
    def get_salary(console, error:bool = False) -> int:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            try:
                salary = int(console.input("[bold cyan]Salario (clp): $"))
                if salary < 500000 or salary > 300000000:
                    console.print("[bold red]Debe ingresar un salario valido entre $500.000 y $30.000.000")
                    error = True
                    continue
                return salary
            except ValueError:
                console.print("[bold red]Debe ingresar un número válido para el salario.")
                error = True
