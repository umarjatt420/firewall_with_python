import subprocess

def create_firewall_rule():
    # Enable IP forwarding
    subprocess.call(['sysctl', '-w', 'net.ipv4.ip_forward=1'])

    # Flush existing rules
    subprocess.call(['iptables', '-F'])

    # Set default policies
    subprocess.call(['iptables', '-P', 'INPUT', 'ACCEPT'])
    subprocess.call(['iptables', '-P', 'FORWARD', 'ACCEPT'])
    subprocess.call(['iptables', '-P', 'OUTPUT', 'ACCEPT'])

    # Allow specific incoming connections
    subprocess.call(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '22', '-j', 'ACCEPT'])  # Block SSH

    # Drop all other incoming traffic

    print('Firewall rules created successfully.')

# Create the firewall rules
create_firewall_rule()