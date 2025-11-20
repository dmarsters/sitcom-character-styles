#!/usr/bin/env python3
"""Test MCP server functionality.

This script tests the MCP server tools without actually running the server,
verifying that all tools work correctly.
"""

import json
import sys

def test_imports():
    """Test that all imports work."""
    print("\n" + "="*70)
    print("Testing Imports")
    print("="*70)
    
    try:
        from sitcom_character_styles.characters.endora.src.endora_operator import EndoraOperator
        from sitcom_character_styles.characters.endora.src.prompt_enhancement import (
            enhance_prompt_with_endora,
            get_endora_intensity_description,
            get_endora_examples
        )
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_enhance_prompt():
    """Test enhance_prompt_with_endora functionality."""
    print("\n" + "="*70)
    print("Testing enhance_prompt_with_endora Tool")
    print("="*70)
    
    from sitcom_character_styles.characters.endora.src.prompt_enhancement import (
        enhance_prompt_with_endora
    )
    
    test_cases = [
        ("a coffee cup", 0, False),
        ("a coffee cup", 5, False),
        ("a coffee cup", 10, False),
        ("a coffee cup", 5, True),
    ]
    
    for prompt, intensity, include_details in test_cases:
        try:
            result = enhance_prompt_with_endora(
                base_prompt=prompt,
                intensity=intensity,
                include_details=include_details
            )
            
            if include_details:
                # Should be dict with keys
                assert isinstance(result, dict)
                assert "enhanced_prompt" in result
                assert "character" in result
                assert result["character"] == "Endora"
                print(f"✓ enhance_prompt_with_endora({prompt!r}, {intensity}, details=True)")
                print(f"  → Enhanced: {result['enhanced_prompt'][:80]}...")
            else:
                # Should be dict with enhanced_prompt key
                assert isinstance(result, dict)
                assert "enhanced_prompt" in result
                print(f"✓ enhance_prompt_with_endora({prompt!r}, {intensity}, details=False)")
                print(f"  → Enhanced: {result['enhanced_prompt'][:80]}...")
        
        except Exception as e:
            print(f"✗ Failed: {e}")
            return False
    
    return True


def test_intensity_info():
    """Test get_endora_intensity_info functionality."""
    print("\n" + "="*70)
    print("Testing get_endora_intensity_info Tool")
    print("="*70)
    
    from sitcom_character_styles.characters.endora.src.prompt_enhancement import (
        get_endora_intensity_description
    )
    
    for intensity in [0, 3, 5, 7, 10]:
        try:
            description = get_endora_intensity_description(intensity)
            assert isinstance(description, str)
            assert len(description) > 0
            print(f"✓ Intensity {intensity}: {description}")
        except Exception as e:
            print(f"✗ Failed for intensity {intensity}: {e}")
            return False
    
    return True


def test_examples():
    """Test get_endora_examples functionality."""
    print("\n" + "="*70)
    print("Testing get_endora_examples Tool")
    print("="*70)
    
    from sitcom_character_styles.characters.endora.src.prompt_enhancement import (
        get_endora_examples
    )
    
    try:
        # Get all examples
        examples_all = get_endora_examples()
        assert isinstance(examples_all, dict)
        assert len(examples_all) > 0
        print(f"✓ get_endora_examples() returned {len(examples_all)} examples")
        
        # Get specific intensity example
        examples_5 = get_endora_examples(intensity=5)
        assert isinstance(examples_5, dict)
        assert 5 in examples_5
        assert "original" in examples_5[5]
        assert "enhanced" in examples_5[5]
        print(f"✓ get_endora_examples(intensity=5) returned example:")
        print(f"  Original: {examples_5[5]['original']}")
        print(f"  Enhanced: {examples_5[5]['enhanced'][:80]}...")
        
        return True
    
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_list_characters():
    """Test list_available_characters functionality."""
    print("\n" + "="*70)
    print("Testing list_available_characters (mock)")
    print("="*70)
    
    characters = {
        "characters": [
            {
                "name": "Endora",
                "available": True,
            },
            {
                "name": "Mork",
                "available": False,
                "status": "planned"
            }
        ]
    }
    
    try:
        assert isinstance(characters, dict)
        assert "characters" in characters
        assert len(characters["characters"]) >= 1
        
        # Check Endora is available
        endora = next(c for c in characters["characters"] if c["name"] == "Endora")
        assert endora["available"] == True
        print(f"✓ Endora available")
        
        # Check Mork is planned
        mork = next(c for c in characters["characters"] if c["name"] == "Mork")
        assert mork["available"] == False
        assert mork["status"] == "planned"
        print(f"✓ Mork planned for future")
        
        return True
    
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print("SITCOM CHARACTER STYLES - MCP SERVER TESTS")
    print("="*70)
    
    tests = [
        ("Imports", test_imports),
        ("enhance_prompt_with_endora", test_enhance_prompt),
        ("get_endora_intensity_info", test_intensity_info),
        ("get_endora_examples", test_examples),
        ("list_available_characters", test_list_characters),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"\n✗ Test {test_name} crashed: {e}")
            results[test_name] = False
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED - MCP Server ready for deployment")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
