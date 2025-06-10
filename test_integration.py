#!/usr/bin/env python3
"""
Tests essentiels pour OHCE - Version simplifiée
2 tests principaux pour valider le fonctionnement
"""

import subprocess
import sys
import os

def run_ohce_session(inputs, timeout=10):
    """Lance une session OHCE avec les entrées données"""
    try:
        process = subprocess.Popen(
            [sys.executable, 'ohce.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        input_string = '\n'.join(inputs) + '\n'
        stdout, stderr = process.communicate(input=input_string, timeout=timeout)
        
        return {
            'stdout': stdout,
            'stderr': stderr,
            'success': process.returncode == 0
        }
    except Exception as e:
        return {
            'stdout': '',
            'stderr': str(e),
            'success': False
        }

def test_1_basic_functionality():
    """
    TEST 1: Fonctionnalités de base
    - Effet miroir
    - Détection palindrome
    - Langue française
    """
    print("🧪 TEST 1: Fonctionnalités de base")
    print("-" * 40)
    
    inputs = [
        'fr',      # Français
        'hello',   # Mot normal → doit afficher 'olleh'
        'radar',   # Palindrome → doit afficher 'radar' + 'Bien dit !'
        'quit'     # Sortie
    ]
    
    result = run_ohce_session(inputs)
    
    if not result['success']:
        print("❌ ÉCHEC - L'application ne démarre pas")
        print(f"   Erreur: {result['stderr']}")
        return False
    
    output = result['stdout']
    print(f"📄 Sortie complète:\n{output}")
    
    # Vérifications
    checks = [
        ('olleh' in output, "Miroir de 'hello' → 'olleh'"),
        ('radar' in output, "Miroir de 'radar' → 'radar'"),
        ('Bien dit' in output, "Détection palindrome → 'Bien dit !'"),
        ('Bonjour' in output or 'Bonsoir' in output or 'Bon après-midi' in output, "Salutation française")
    ]
    
    all_passed = True
    for check, description in checks:
        if check:
            print(f"  ✅ {description}")
        else:
            print(f"  ❌ {description}")
            all_passed = False
    
    print(f"\n🎯 Résultat TEST 1: {'✅ RÉUSSI' if all_passed else '❌ ÉCHEC'}")
    return all_passed

def test_2_multilingual_palindromes():
    """
    TEST 2: Multilingue et palindromes complexes
    - Langue anglaise
    - Palindromes avec espaces et casse
    """
    print("\n🧪 TEST 2: Multilingue et palindromes complexes")
    print("-" * 50)
    
    inputs = [
        'en',              # Anglais
        'world',           # Mot normal → 'dlrow'
        'Level',           # Palindrome avec casse → 'leveL' + 'Well said!'
        'A man a plan',    # Palindrome avec espaces → miroir + 'Well said!'
        'exit'             # Sortie
    ]
    
    result = run_ohce_session(inputs)
    
    if not result['success']:
        print("❌ ÉCHEC - L'application ne démarre pas")
        return False
    
    output = result['stdout']
    print(f"📄 Sortie complète:\n{output}")
    
    # Vérifications
    checks = [
        ('dlrow' in output, "Miroir de 'world' → 'dlrow'"),
        ('leveL' in output, "Miroir de 'Level' → 'leveL'"),
        ('nalp a nam A' in output, "Miroir de 'A man a plan' → 'nalp a nam A'"),
        ('Well said' in output, "Détection palindromes en anglais"),
        ('Good morning' in output or 'Good evening' in output or 'Good afternoon' in output, "Salutation anglaise")
    ]
    
    # Compter les "Well said"
    well_said_count = output.count('Well said')
    expected_palindromes = 2  # Level + A man a plan
    
    all_passed = True
    for check, description in checks:
        if check:
            print(f"  ✅ {description}")
        else:
            print(f"  ❌ {description}")
            all_passed = False
    
    # Vérification spéciale pour le nombre de palindromes
    if well_said_count == expected_palindromes:
        print(f"  ✅ Nombre correct de palindromes: {well_said_count}")
    else:
        print(f"  ❌ Palindromes détectés: {well_said_count}, attendu: {expected_palindromes}")
        all_passed = False
    
    print(f"\n🎯 Résultat TEST 2: {'✅ RÉUSSI' if all_passed else '❌ ÉCHEC'}")
    return all_passed

def main():
    """Exécution des 2 tests essentiels"""
    print("🚀 TESTS ESSENTIELS OHCE")
    print("=" * 50)
    
    # Vérifier que ohce.py existe
    if not os.path.exists('ohce.py'):
        print("❌ Fichier ohce.py non trouvé!")
        print("   Créez d'abord le fichier ohce.py avec votre code")
        return False
    
    # Exécuter les 2 tests
    test1_result = test_1_basic_functionality()
    test2_result = test_2_multilingual_palindromes()
    
    # Résumé final
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ FINAL")
    print("=" * 50)
    
    passed_tests = sum([test1_result, test2_result])
    total_tests = 2
    
    print(f"Tests réussis: {passed_tests}/{total_tests}")
    
    if passed_tests == total_tests:
        print("🎉 TOUS LES TESTS ESSENTIELS RÉUSSIS!")
        print("   Votre application OHCE fonctionne correctement")
    else:
        print("⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
        print("   Vérifiez les détails ci-dessus pour corriger")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)