"""FastMCP server for sitcom character styles - Flat structure for cloud compatibility."""

import json
from typing import Optional, List, Dict, Any
from fastmcp import FastMCP

# Initialize FastMCP server
server = FastMCP("sitcom-character-styles")

# ============================================================================
# ENDORA OPERATOR (Embedded for FastMCP Cloud compatibility)
# ============================================================================

class EndoraOperator:
    """Endora's continuous deformation operator - embedded version."""
    
    def __init__(self, intensity: int = 5):
        self.intensity = max(0, min(10, intensity))
        self.intensity_factor = self.intensity / 10.0
    
    def apply(self, prompt: str) -> Dict[str, Any]:
        """Apply Endora operator to a prompt."""
        # Simple prompt enhancement
        enhanced = self._enhance_prompt(prompt)
        
        return {
            "enhanced_prompt": enhanced,
            "transformation_details": {
                "character": "Endora",
                "intensity": self.intensity,
                "intensity_factor": self.intensity_factor
            },
            "intensity_applied": self.intensity
        }
    
    def _enhance_prompt(self, prompt: str) -> str:
        """Enhance prompt with Endora's sensory logic."""
        if self.intensity_factor < 0.2:
            return prompt
        elif self.intensity_factor < 0.4:
            return f"{prompt} with subtle aristocratic presence"
        elif self.intensity_factor < 0.6:
            return f"{prompt} rendered with material precision, organized by significance, with undertones of aristocratic knowing"
        elif self.intensity_factor < 0.8:
            return f"{prompt} exquisitely crafted and materially significant, dramatically reorganized with clear spatial hierarchy, with aristocratic judgment and supernatural knowing"
        else:
            return f"{prompt}, completely saturated by Endora's presence - exquisitely rendered with jewel tones, materially precious, spatially hierarchical, feeling of being evaluated by superior knowledge"

# ============================================================================
# MCP TOOLS
# ============================================================================

@server.tool()
def enhance_prompt_with_endora_impl(
    prompt: str,
    intensity: int = 5,
    include_details: bool = False
) -> str:
    """Enhance an image generation prompt with Endora's sensory logic."""
    try:
        operator = EndoraOperator(intensity=intensity)
        result = operator.apply(prompt)
        
        if include_details:
            return json.dumps(result, indent=2)
        else:
            return result['enhanced_prompt']
    
    except Exception as e:
        return f"Error: {str(e)}"


@server.tool()
def get_endora_intensity_info(intensity: int) -> str:
    """Get a description of what a specific intensity level means for Endora."""
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


@server.tool()
def get_endora_examples(intensity: Optional[int] = None) -> str:
    """Get example transformations at different intensities."""
    examples = {
        2: {
            "original": "a coffee cup",
            "enhanced": "a coffee cup with subtle aristocratic presence",
            "description": "Barely perceptible Endora influence"
        },
        5: {
            "original": "a coffee cup on a table",
            "enhanced": "a coffee cup rendered with material precision, on a table organized by significance, with undertones of aristocratic knowing",
            "description": "Balanced blend of character and original prompt"
        },
        8: {
            "original": "a rustic wooden chair",
            "enhanced": "exquisitely crafted rustic wooden chair, materially significant with deep sapphire, emerald, and amethyst tones with gold accents, mood: completely saturated by Endora's presence",
            "description": "Strong Endora dominance"
        }
    }
    
    if intensity is not None:
        if intensity in examples:
            return json.dumps({intensity: examples[intensity]}, indent=2)
        else:
            return json.dumps({}, indent=2)
    
    return json.dumps(examples, indent=2)


@server.tool()
def list_available_characters() -> str:
    """List all available character operators."""
    characters = {
        "characters": [
            {
                "name": "Endora",
                "type": "sitcom_character",
                "source": "Bewitched (1960s-70s)",
                "core_worldview": "Aristocratic supernatural authority",
                "available": True
            },
            {
                "name": "Mork",
                "type": "sitcom_character",
                "source": "Mork & Mindy (1970s-80s)",
                "core_worldview": "Alien absurdist sincerity",
                "available": False,
                "status": "planned"
            }
        ]
    }
    return json.dumps(characters, indent=2)


@server.tool()
def get_server_info() -> str:
    """Get information about the sitcom-character-styles MCP server."""
    info = {
        "server": "sitcom-character-styles",
        "version": "1.0.0",
        "description": "MCP server for applying sitcom character sensory logic to image prompts",
        "repository": "https://github.com/dmarsters/sitcom-character-styles"
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    server.run()
