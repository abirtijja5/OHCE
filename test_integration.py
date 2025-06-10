#!/usr/bin/env python3
"""
Tests ultra-simples pour OHCE
Juste 2 vérifications de base
"""

import subprocess
import sys

def test_ohce(inputs):
    """Lance OHCE avec des entrées et retourne la sortie"""
    try:
        result = subprocess.run(
            [sys.executable, 'ohce.py'],
            input='\n'.join(inputs) + '\n',
            text=True,
            capture_output=True,
            timeout=5
        )
        return result.stdout
    except:
        return ""

def main():
    print("🧪 Tests OHCE simples")
    print("-" * 30)
    
    # Test 1: Miroir basique
    print("Test 1: Effet miroir")
    output1 = test_ohce(['fr', 'hello', 'quit'])
    if 'olleh' in output1:
        print("  ✅ 'hello' → 'olleh'")
    else:
        print("  ❌ Miroir ne fonctionne pas")
        print(f"  Sortie: {output1}")
    
    # Test 2: Palindrome
    print("\nTest 2: Palindrome")
    output2 = test_ohce(['fr', 'radar', 'quit'])
    if 'radar' in output2 and 'Bien dit' in output2:
        print("  ✅ 'radar' détecté comme palindrome")
    else:
        print("  ❌ Palindrome pas détecté")
        print(f"  Sortie: {output2}")
    
    print("\n✨ Tests terminés!")

if __name__ == "__main__":
    main()