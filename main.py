from colorama import Fore, Style, init
from detector import run_detection
from narrator import narrate_all
from reporter import generate_report

init(autoreset=True)

def main():
    print(Fore.CYAN + "="*60)
    print(Fore.CYAN + "   LEDGER DISCREPANCY NARRATOR")
    print(Fore.CYAN + "   Financial Reconciliation Tool | 2026")
    print(Fore.CYAN + "="*60)

    print(Fore.YELLOW + "\n[1/3] Running discrepancy detection...")
    issues = run_detection()
    
    if not issues:
        print(Fore.GREEN + "No discrepancies found!")
        return

    print(Fore.RED + f"\nFound {len(issues)} discrepancies:")
    for issue in issues:
        print(Fore.RED + f"  → [{issue['type']}] {issue['transaction_id']}: {issue['detail']}")

    print(Fore.YELLOW + "\n[2/3] Generating AI narratives...")
    narratives = narrate_all(issues)

    print(Fore.YELLOW + "\n[3/3] Generating report...")
    filename = generate_report(narratives)

    print(Fore.GREEN + "\n" + "="*60)
    print(Fore.GREEN + "✓ Done! Report generated successfully!")
    print(Fore.GREEN + f"✓ Check your reports/ folder: {filename}")
    print(Fore.GREEN + "="*60)

if __name__ == "__main__":
    main()