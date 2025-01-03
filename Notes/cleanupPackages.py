import pkg_resources
import subprocess
import sys
from datetime import datetime
import logging
from collections import defaultdict

def setup_logging():
    """Configure logging to both console and file"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(f'package_removal_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        ]
    )

def get_essential_packages():
    """Define packages that should never be removed"""
    return {
        'pip', 'setuptools', 'wheel', 'distlib', 'virtualenv',
        'packaging', 'six', 'appdirs', 'pyparsing'
    }

def analyze_dependencies():
    """Build dependency graph of installed packages"""
    dependency_graph = defaultdict(set)
    reverse_deps = defaultdict(set)
    
    for package in pkg_resources.working_set:
        for req in package.requires():
            dependency_graph[package.key].add(req.key)
            reverse_deps[req.key].add(package.key)
    
    return dependency_graph, reverse_deps

def create_backup():
    """Create backup of current package list"""
    backup_file = f'packages_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    try:
        subprocess.run(
            [sys.executable, '-m', 'pip', 'freeze'],
            stdout=open(backup_file, 'w'),
            check=True
        )
        logging.info(f"Backup created: {backup_file}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        sys.exit(1)

def get_removable_packages():
    """Identify packages that can be safely removed"""
    essential = get_essential_packages()
    dependency_graph, reverse_deps = analyze_dependencies()
    
    # Get all installed packages
    installed = {pkg.key for pkg in pkg_resources.working_set}
    
    # Find packages that are safe to remove
    removable = set()
    for package in installed:
        # Skip essential packages
        if package.lower() in essential:
            continue
        
        # Skip if it's a dependency of an essential package
        is_essential_dep = False
        for ess in essential:
            if package in dependency_graph.get(ess, set()):
                is_essential_dep = True
                break
        
        if not is_essential_dep:
            removable.add(package)
    
    return removable

def remove_packages(packages):
    """Remove specified packages with error handling"""
    failed = []
    successful = []
    
    for package in packages:
        try:
            logging.info(f"Removing {package}...")
            subprocess.run(
                [sys.executable, '-m', 'pip', 'uninstall', '-y', package],
                check=True,
                capture_output=True,
                text=True
            )
            successful.append(package)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to remove {package}: {e.stderr}")
            failed.append(package)
    
    return successful, failed

def main():
    # Initialize logging
    setup_logging()
    logging.info("Starting package removal process...")
    
    # Create backup first
    create_backup()
    
    # Get removable packages
    removable = get_removable_packages()
    
    if not removable:
        logging.info("No non-essential packages found to remove.")
        return
    
    # Show packages to be removed
    print("\nPackages that will be removed:")
    for pkg in sorted(removable):
        print(f"- {pkg}")
    
    # Get confirmation
    confirm = input("\nProceed with removal? (yes/no): ").lower()
    if confirm != 'yes':
        logging.info("Operation cancelled by user.")
        return
    
    # Remove packages
    successful, failed = remove_packages(removable)
    
    # Final report
    print("\nRemoval process completed!")
    print(f"Successfully removed: {len(successful)} packages")
    if failed:
        print(f"Failed to remove: {len(failed)} packages")
        print("\nFailed packages:")
        for pkg in failed:
            print(f"- {pkg}")
    
    logging.info("Package removal process completed")

if __name__ == "__main__":
    main()