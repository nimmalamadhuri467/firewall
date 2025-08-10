import json
from rich import print

class Firewall:
    def __init__(self, rules_file):
        self.rules_file = rules_file
        self.rules = self.load_rules()

    def load_rules(self):
        try:
            with open(self.rules_file, "r") as f:
                data = json.load(f)
                return [rule for rule in data if self.validate_rule(rule)]
        except Exception as e:
            print(f"[red]Error loading rules: {e}[/red]")
            return []

    def validate_rule(self, rule):
        required_keys = {"ip", "port", "protocol", "action"}
        if not required_keys.issubset(rule.keys()):
            print(f"[yellow]Invalid rule format: {rule}[/yellow]")
            return False
        if rule["action"] not in {"ALLOW", "DENY"}:
            print(f"[yellow]Invalid action: {rule['action']}[/yellow]")
            return False
        return True

    def show_rules(self):
        print("[bold cyan]Loaded Firewall Rules:[/bold cyan]")
        for idx, rule in enumerate(self.rules, start=1):
            print(f"{idx}. IP: {rule['ip']}, Port: {rule['port']}, Protocol: {rule['protocol']}, Action: {rule['action']}")
