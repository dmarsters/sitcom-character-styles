"""Endora prompt enhancement module.

Provides high-level interface for enhancing prompts with Endora's sensory logic.
Used by MCP server to transform user prompts.
"""

from typing import Dict, Any, Optional
from .endora_operator import EndoraOperator, TransformedPrompt


def enhance_prompt_with_endora(
    base_prompt: str,
    intensity: int = 5,
    include_details: bool = False
) -> Dict[str, Any]:
    """
    Enhance a prompt with Endora's sensory logic.
    
    Args:
        base_prompt: The original prompt to transform
        intensity: Intensity level 0-10 (default 5 for balanced)
        include_details: Whether to include transformation details
    
    Returns:
        Dictionary with enhanced prompt and optional transformation details
    """
    # Validate intensity
    if not isinstance(intensity, int) or intensity < 0 or intensity > 10:
        raise ValueError(f"Intensity must be integer 0-10, got {intensity}")
    
    # Create and apply operator
    operator = EndoraOperator(intensity=intensity)
    result: TransformedPrompt = operator.apply(base_prompt)
    
    # Build response
    response = {
        "enhanced_prompt": result.enhanced_prompt,
        "original_prompt": base_prompt,
        "character": "Endora",
        "intensity": result.intensity_applied,
        "success": True
    }
    
    # Add transformation details if requested
    if include_details:
        response["transformation_details"] = result.transformation_details
    
    return response


def get_endora_intensity_description(intensity: int) -> str:
    """Get a human-readable description of what a given intensity means."""
    descriptions = {
        0: "No transformation - original prompt unchanged",
        1: "Whisper - barely perceptible aristocratic presence",
        2: "Subtle - character sensibility just barely visible",
        3: "Light touch - character influence present but not dominant",
        4: "Moderate-light - clear Endora sensibility but respecting original",
        5: "Balanced - Endora operator and original prompt in clear conversation",
        6: "Moderate-strong - Endora's logic becoming dominant",
        7: "Strong - Endora's sensibility clearly dominant, original secondary",
        8: "Very strong - Endora's logic saturating nearly everything",
        9: "Overwhelming - original prompt barely visible through Endora's presence",
        10: "Complete saturation - Endora's sensory logic is the primary reality"
    }
    
    if intensity < 0 or intensity > 10:
        return "Invalid intensity"
    
    return descriptions.get(intensity, "Unknown intensity")


def validate_endora_coherence(result: TransformedPrompt) -> Dict[str, Any]:
    """
    Validate that an Endora transformation is coherent.
    
    Returns validation results.
    """
    validation = {
        "is_coherent": True,
        "checks_passed": [],
        "checks_failed": [],
        "warnings": []
    }
    
    # Check 1: All dimensions present
    if "dimensions_applied" in result.transformation_details:
        dimensions = result.transformation_details["dimensions_applied"]
        expected_dimensions = ["material", "spatial", "temporal", "chromatic", "emotional"]
        
        if set(dimensions) == set(expected_dimensions):
            validation["checks_passed"].append("All five transformation dimensions applied")
        else:
            missing = set(expected_dimensions) - set(dimensions)
            validation["checks_failed"].append(f"Missing dimensions: {missing}")
            validation["is_coherent"] = False
    
    # Check 2: Original subject recognizable
    original = result.transformation_details.get("original_components", {}).get("subject", "")
    if original:
        # Subject should still be roughly recognizable in enhanced prompt
        if original.lower() in result.enhanced_prompt.lower() or \
           any(word.lower() in result.enhanced_prompt.lower() for word in original.split()):
            validation["checks_passed"].append("Original subject recognizable")
        else:
            validation["warnings"].append("Original subject may not be easily recognizable (high intensity?)")
    
    # Check 3: Unified sensibility (heuristic)
    transformed = result.transformation_details.get("transformed_components", {})
    if sum(1 for v in transformed.values() if v) >= 3:  # At least 3 dimensions transformed
        validation["checks_passed"].append("Unified sensibility detected (multiple dimensions transformed)")
    
    # Check 4: Intensity appropriate
    intensity = result.intensity_applied
    if 0 <= intensity <= 10:
        validation["checks_passed"].append(f"Intensity valid: {intensity}/10")
    else:
        validation["checks_failed"].append(f"Intensity out of range: {intensity}")
        validation["is_coherent"] = False
    
    return validation


def format_enhanced_prompt_for_generation(
    enhanced_prompt: str,
    intensity: int,
    include_metadata: bool = False
) -> str:
    """
    Format enhanced prompt for use with image generation models.
    
    Can optionally include metadata as comments.
    """
    if include_metadata:
        metadata = f"[Endora operator, intensity {intensity}/10]"
        return f"{enhanced_prompt}\n{metadata}"
    else:
        return enhanced_prompt


def get_endora_examples(intensity: Optional[int] = None) -> Dict[str, Dict[str, str]]:
    """
    Get example transformations at different intensities.
    
    Args:
        intensity: Specific intensity to get example for, or None for all
    
    Returns:
        Dictionary of examples
    """
    examples = {
        2: {
            "original": "a coffee cup",
            "enhanced": "a coffee cup with subtle presence and material intention",
            "description": "Barely perceptible Endora influence"
        },
        5: {
            "original": "a coffee cup on a table",
            "enhanced": "a coffee cup rendered with material precision and intention, on a table organized with subtle hierarchy, with undertones of aristocratic knowing and gentle contempt",
            "description": "Balanced blend of character and original prompt"
        },
        8: {
            "original": "a coffee cup on a table in a kitchen",
            "enhanced": "exquisitely crafted coffee cup, materially significant with visible texture and presence, placed on a table dramatically reorganized into clear spatial tiers, in a kitchen completely reorganized - foreground precious and clear, background diminished. Motion is deliberate, weighted, and significant. Colors rendered with jewel-tone composition. Feeling of being evaluated by aristocratic judgment and supernatural knowing",
            "description": "Strong Endora dominance"
        }
    }
    
    if intensity is not None:
        if intensity in examples:
            return {intensity: examples[intensity]}
        else:
            return {}
    
    return examples
