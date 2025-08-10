import argparse
from firewall import Firewall

def main():
    parser = argparse.ArgumentParser(description="FireGuardCLI - Basic Firewall Simulation Tool")
    parser.add_argument("--show-rules", action="store_true", help="Display all firewall rules")
    args = parser.parse_args()

    fw = Firewall("rules.json")
    if args.show_rules:
        fw.show_rules()

if __name__ == "__main__":
    main()
