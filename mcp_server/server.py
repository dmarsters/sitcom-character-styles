"""FastMCP server for sitcom character styles.

Exposes character operators as MCP tools.
Currently supports: Endora
Future support: Mork, other sitcom characters
"""

import json
from typing import Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    import sys
    print("Error: fastmcp not installed. Install with: pip install fastmcp", file=sys.stderr)
    exit(1)

# Import character operators using absolute imports
try:
    from characters.endora.src.endora_operator import EndoraOperator
    from characters.endora.src.prompt_enhancement import (
        enhance_prompt_with_endora,
        get_endora_intensity_description,
        get_endora_examples
    )
except ImportError as e:
    import sys
    print(f"Error importing character operators: {e}", file=sys.stderr)
    print("Make sure you're running from the sitcom-character-styles project root directory.", file=sys.stderr)
    exit(1)

# Initialize FastMCP server
server = FastMCP("sitcom-character-styles")

# ============================================================================
# ENDORA TOOLS
# ============================================================================

@server.tool()
def enhance_prompt_with_endora_impl(
    prompt: str,
    intensity: int = 5,
    include_details: bool = False
) -> str:
    """Enhance an image generation prompt with Endora's sensory logic.
    
    Endora embodies aristocratic supernatural authority. Her sensory logic
    transforms visual fields through five dimensions:
    - Material precision: Objects become precious, textured, intentional
    - Spatial hierarchy: Space reorganizes with clear tiers of significance
    - Temporal authority: Motion becomes deliberate, moments become weighted
    - Chromatic command: Colors shift toward jewel tones (sapphire, emerald, amethyst, gold)
    - Emotional subtext: Aristocratic judgment, knowing, contempt with hidden care
    
    Args:
        prompt: The base prompt to transform (natural language description)
        intensity: Intensity level 0-10 (default 5 for balanced)
        include_details: If true, include transformation details and metadata
    
    Returns:
        Enhanced prompt text (or JSON with details if include_details=True)
    """
    try:
        result = enhance_prompt_with_endora(
            base_prompt=prompt,
            intensity=intensity,
            include_details=include_details
        )
        
        if include_details:
            return json.dumps(result, indent=2)
        else:
            return result['enhanced_prompt']
    
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


@server.tool()
def get_endora_intensity_info(intensity: int) -> str:
    """Get a description of what a specific intensity level means for Endora.
    
    Args:
        intensity: Intensity level 0-10
    
    Returns:
        Human-readable description of the intensity level
    """
    try:
        return get_endora_intensity_description(intensity)
    except Exception as e:
        return f"Error: {str(e)}"


@server.tool()
def get_endora_examples(intensity: Optional[int] = None) -> str:
    """Get example transformations at specific intensities.
    
    Args:
        intensity: Optional specific intensity (0-10) to get example for.
    
    Returns:
        JSON formatted examples showing original → enhanced transformations
    """
    try:
        examples = get_endora_examples(intensity=intensity)
        return json.dumps(examples, indent=2)
    except Exception as e:
        return f"Error: {str(e)}"


@server.tool()
def list_available_characters() -> str:
    """List all available character operators.
    
    Returns:
        JSON listing of available characters and their descriptions
    """
    characters = {
        "characters": [
            {
                "name": "Endora",
                "type": "sitcom_character",
                "source": "Bewitched (1960s-70s)",
                "core_worldview": "Aristocratic supernatural authority",
                "available": True,
                "tool": "enhance_prompt_with_endora_impl"
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
    """Get information about the sitcom-character-styles MCP server.
    
    Returns:
        JSON with server metadata, capabilities, and usage information
    """
    info = {
        "server": "sitcom-character-styles",
        "version": "1.0.0",
        "description": "MCP server for applying sitcom character sensory logic to image prompts",
        "framework": {
            "type": "Olog-based continuous deformation operators",
            "layers": [
                "Layer 1: Categorical structure",
                "Layer 2: Intentionality",
                "Layer 3: Execution"
            ]
        },
        "capabilities": {
            "enhance_prompt_with_endora_impl": "Transform prompts with Endora's sensory logic (intensity 0-10)",
            "get_endora_intensity_info": "Describe what specific intensity levels mean",
            "get_endora_examples": "See example transformations",
            "list_available_characters": "List current and planned characters",
            "get_server_info": "Get this information"
        },
        "repository": "https://github.com/dmarsters/sitcom-character-styles"
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    server.run()
