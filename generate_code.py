import os

# ── Structure: { "folder_name": { "display_name": str, "topics": [(slug, title)] } }
MODULES = {
    "00_introduction": {
        "display": "00 · Introduction",
        "topics": [
            ("what-is-cybersecurity",           "What is Cybersecurity"),
            ("types-of-hackers",                "Types of Hackers"),
            ("attacker-mindset",                "Attacker Mindset"),
            ("vulnerability-vs-threat-vs-risk", "Vulnerability vs Threat vs Risk"),
            ("attack-types-overview",           "Attack Types Overview"),
            ("cia-triad",                       "CIA Triad"),
            ("security-principles",             "Security Principles"),
            ("threat-modeling",                 "Threat Modeling"),
            ("defense-in-depth",                "Defense in Depth"),
            ("zero-trust",                      "Zero Trust"),
            ("security-domains-overview",       "Security Domains Overview"),
            ("how-to-use-this-repo",            "How to Use This Repo"),
        ],
    },
    "01_security-foundations": {
        "display": "01 · Security Foundations",
        "topics": [
            ("operating-systems",   "Operating Systems"),
            ("linux-security",      "Linux Security"),
            ("windows-security",    "Windows Security"),
            ("authentication",      "Authentication"),
            ("authorization",       "Authorization"),
            ("identity-management", "Identity Management"),
        ],
    },
    "02_network-security": {
        "display": "02 · Network Security",
        "topics": [
            ("osi-model",       "OSI Model"),
            ("tcp-ip",          "TCP/IP"),
            ("dns",             "DNS"),
            ("http-https",      "HTTP & HTTPS"),
            ("tls-ssl",         "TLS & SSL"),
            ("firewalls",       "Firewalls"),
            ("vpns",            "VPNs"),
            ("proxies",         "Proxies"),
            ("network-attacks", "Network Attacks"),
        ],
    },
    "03_cryptography": {
        "display": "03 · Cryptography",
        "topics": [
            ("symmetric-encryption",  "Symmetric Encryption"),
            ("asymmetric-encryption", "Asymmetric Encryption"),
            ("hashing",               "Hashing"),
            ("digital-signatures",    "Digital Signatures"),
            ("certificates",          "Certificates"),
            ("pki",                   "PKI"),
            ("key-management",        "Key Management"),
        ],
    },
    "04_web-security": {
        "display": "04 · Web Security",
        "topics": [
            ("browser-security",      "Browser Security"),
            ("cookies",               "Cookies"),
            ("sessions",              "Sessions"),
            ("cors",                  "CORS"),
            ("csrf",                  "CSRF"),
            ("xss",                   "XSS"),
            ("sql-injection",         "SQL Injection"),
            ("ssrf",                  "SSRF"),
            ("rce",                   "RCE"),
            ("authentication-attacks","Authentication Attacks"),
        ],
    },
    "05_application-security": {
        "display": "05 · Application Security",
        "topics": [
            ("secure-coding",       "Secure Coding"),
            ("code-review",         "Code Review"),
            ("static-analysis",     "Static Analysis"),
            ("dynamic-analysis",    "Dynamic Analysis"),
            ("dependency-security", "Dependency Security"),
            ("secrets-management",  "Secrets Management"),
            ("secure-sdlc",         "Secure SDLC"),
        ],
    },
    "06_offensive-security": {
        "display": "06 · Offensive Security",
        "topics": [
            ("reconnaissance",      "Reconnaissance"),
            ("enumeration",         "Enumeration"),
            ("exploitation",        "Exploitation"),
            ("privilege-escalation","Privilege Escalation"),
            ("lateral-movement",    "Lateral Movement"),
            ("persistence",         "Persistence"),
            ("post-exploitation",   "Post-Exploitation"),
        ],
    },
    "07_pentesting": {
        "display": "07 · Pentesting",
        "topics": [
            ("web-pentesting",      "Web Pentesting"),
            ("network-pentesting",  "Network Pentesting"),
            ("wireless-pentesting", "Wireless Pentesting"),
            ("active-directory",    "Active Directory"),
            ("cloud-pentesting",    "Cloud Pentesting"),
            ("reporting",           "Reporting"),
        ],
    },
    "08_defensive-security": {
        "display": "08 · Defensive Security",
        "topics": [
            ("security-monitoring", "Security Monitoring"),
            ("threat-detection",    "Threat Detection"),
            ("alerting",            "Alerting"),
            ("threat-hunting",      "Threat Hunting"),
            ("log-analysis",        "Log Analysis"),
            ("incident-triage",     "Incident Triage"),
        ],
    },
    "09_malware-analysis": {
        "display": "09 · Malware Analysis",
        "topics": [
            ("malware-types",       "Malware Types"),
            ("static-analysis",     "Static Analysis"),
            ("dynamic-analysis",    "Dynamic Analysis"),
            ("unpacking",           "Unpacking"),
            ("sandbox-evasion",     "Sandbox Evasion"),
            ("reverse-engineering", "Reverse Engineering"),
        ],
    },
    "10_dfir": {
        "display": "10 · DFIR",
        "topics": [
            ("disk-forensics",    "Disk Forensics"),
            ("memory-forensics",  "Memory Forensics"),
            ("evidence-collection","Evidence Collection"),
            ("timeline-analysis", "Timeline Analysis"),
            ("incident-response", "Incident Response"),
        ],
    },
    "11_cloud-security": {
        "display": "11 · Cloud Security",
        "topics": [
            ("iam",                    "IAM"),
            ("cloud-misconfigurations","Cloud Misconfigurations"),
            ("container-security",     "Container Security"),
            ("kubernetes-security",    "Kubernetes Security"),
            ("serverless-security",    "Serverless Security"),
            ("secrets-management",     "Secrets Management"),
        ],
    },
    "12_identity-and-access": {
        "display": "12 · Identity & Access",
        "topics": [
            ("passwords",       "Passwords"),
            ("mfa",             "MFA"),
            ("sso",             "SSO"),
            ("oauth",           "OAuth"),
            ("openid-connect",  "OpenID Connect"),
            ("ldap",            "LDAP"),
            ("kerberos",        "Kerberos"),
        ],
    },
    "13_endpoint-security": {
        "display": "13 · Endpoint Security",
        "topics": [
            ("antivirus",        "Antivirus"),
            ("edr",              "EDR"),
            ("process-monitoring","Process Monitoring"),
            ("kernel-security",  "Kernel Security"),
            ("device-control",   "Device Control"),
        ],
    },
    "14_mobile-security": {
        "display": "14 · Mobile Security",
        "topics": [
            ("android-security",  "Android Security"),
            ("ios-security",      "iOS Security"),
            ("apk-analysis",      "APK Analysis"),
            ("mobile-pentesting", "Mobile Pentesting"),
        ],
    },
    "15_wireless-security": {
        "display": "15 · Wireless Security",
        "topics": [
            ("wifi-security",      "WiFi Security"),
            ("bluetooth-security", "Bluetooth Security"),
            ("nfc-security",       "NFC Security"),
            ("rogue-access-points","Rogue Access Points"),
        ],
    },
    "16_iot-and-embedded-security": {
        "display": "16 · IoT & Embedded",
        "topics": [
            ("firmware-analysis",    "Firmware Analysis"),
            ("uart",                 "UART"),
            ("jtag",                 "JTAG"),
            ("hardware-debugging",   "Hardware Debugging"),
            ("embedded-exploitation","Embedded Exploitation"),
        ],
    },
    "17_threat-intelligence": {
        "display": "17 · Threat Intelligence",
        "topics": [
            ("iocs",          "IOCs"),
            ("ttps",          "TTPs"),
            ("threat-actors", "Threat Actors"),
            ("campaigns",     "Campaigns"),
            ("mitre-attack",  "MITRE ATT&CK"),
        ],
    },
    "18_grc": {
        "display": "18 · GRC",
        "topics": [
            ("risk-assessment",  "Risk Assessment"),
            ("security-policies","Security Policies"),
            ("compliance",       "Compliance"),
            ("auditing",         "Auditing"),
            ("security-controls","Security Controls"),
        ],
    },
    "19_privacy-and-data-protection": {
        "display": "19 · Privacy & Data Protection",
        "topics": [
            ("data-classification", "Data Classification"),
            ("privacy-engineering", "Privacy Engineering"),
            ("consent-management",  "Consent Management"),
            ("data-retention",      "Data Retention"),
        ],
    },
    "20_security-automation": {
        "display": "20 · Security Automation",
        "topics": [
            ("python-automation",    "Python Automation"),
            ("bash-automation",      "Bash Automation"),
            ("powershell-automation","PowerShell Automation"),
            ("soar",                 "SOAR"),
            ("detection-engineering","Detection Engineering"),
        ],
    },
    "21_vulnerability-research": {
        "display": "21 · Vulnerability Research",
        "topics": [
            ("fuzzing",            "Fuzzing"),
            ("exploit-development","Exploit Development"),
            ("binary-exploitation","Binary Exploitation"),
            ("memory-corruption",  "Memory Corruption"),
        ],
    },
    "22_human-security": {
        "display": "22 · Human Security",
        "topics": [
            ("phishing",           "Phishing"),
            ("social-engineering", "Social Engineering"),
            ("insider-threats",    "Insider Threats"),
            ("security-awareness", "Security Awareness"),
        ],
    },
    "23_career-and-industry": {
        "display": "23 · Career & Industry",
        "topics": [
            ("certifications", "Certifications"),
            ("labs",           "Labs"),
            ("bug-bounties",   "Bug Bounties"),
            ("research-papers","Research Papers"),
            ("career-paths",   "Career Paths"),
        ],
    },
    "24_resources": {
        "display": "24 · Resources",
        "topics": [
            ("tools",        "Tools"),
            ("labs",         "Labs"),
            ("cheat-sheets", "Cheat Sheets"),
            ("glossaries",   "Glossaries"),
            ("references",   "References"),
        ],
    },
}


def topic_page(title: str, module_display: str) -> str:
    return f"""# {title}

> **Module:** {module_display}

---

## Overview

<!-- What is this topic? Write 2–3 sentences. -->

---

## How It Works

<!-- Explain the core mechanics or concepts. -->

---

## Why It Matters in Security

<!-- What's the security implication? Attack surface? Defensive value? -->

---

## Key Concepts

<!-- Bullet list of must-know terms or ideas for this topic. -->

---

## Common Attacks / Techniques

<!-- If offensive: list techniques. If defensive: list what you're watching for. -->

---

## Tools

<!-- Relevant tools, commands, or frameworks. -->

---

## Lab / Practice

<!-- CTF challenges, TryHackMe rooms, HackTheBox machines, or hands-on exercises. -->

---

## Further Reading

<!-- Links to docs, papers, blog posts, or books. -->
"""


def module_index(folder: str, module: dict) -> str:
    display = module["display"]
    topics  = module["topics"]

    rows = "\n".join(
        f"| {i+1} | [{title}]({slug}.md) | <!-- one-liner --> |"
        for i, (slug, title) in enumerate(topics)
    )

    return f"""# {display}

<!-- One paragraph describing what this module covers and why it matters. -->

---

## Topics

| # | Topic | What You'll Learn |
|---|-------|-------------------|
{rows}

---

## Prerequisites

<!-- List any modules or concepts the reader should know before starting this one. -->

---

## Learning Order

Work through the topics top to bottom. Each one builds on the last.

---

!!! note "Time estimate"
    <!-- Add an estimated time to complete this module. -->
"""


def create_docs(base: str = "docs") -> None:
    created_files  = 0
    skipped_files  = 0
    created_dirs   = 0

    for folder, module in MODULES.items():
        dir_path = os.path.join(base, folder)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            created_dirs += 1
            print(f"  [DIR]  {dir_path}")

        # index.md
        index_path = os.path.join(dir_path, "index.md")
        if not os.path.exists(index_path):
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(module_index(folder, module))
            created_files += 1
            print(f"  [NEW]  {index_path}")
        else:
            skipped_files += 1
            print(f"  [SKIP] {index_path}")

        # one file per topic
        for slug, title in module["topics"]:
            topic_path = os.path.join(dir_path, f"{slug}.md")
            if not os.path.exists(topic_path):
                with open(topic_path, "w", encoding="utf-8") as f:
                    f.write(topic_page(title, module["display"]))
                created_files += 1
                print(f"  [NEW]  {topic_path}")
            else:
                skipped_files += 1
                print(f"  [SKIP] {topic_path}")

    print()
    print(f"Done. {created_dirs} dirs created | {created_files} files created | {skipped_files} files skipped.")


if __name__ == "__main__":
    create_docs(base="docs")