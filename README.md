# Sitcom Character Styles - MCP Server

Transform image generation prompts with the sensory logic of iconic sitcom characters.

## Overview

Sitcom Character Styles is an MCP (Model Context Protocol) server that encodes the distinctive sensory logic of sitcom characters as categorical structures and makes them executable as prompt enhancement operators.

### Core Concept

Each character embodies a **unified sensory logic** - a coherent worldview that manifests across five transformation dimensions:

- **Material**: How objects are rendered (precious, textured, intentional)
- **Spatial**: How space is organized (hierarchy, arrangement, significance)
- **Temporal**: How time/motion is experienced (deliberate, weighted, authoritative)
- **Chromatic**: How colors function (jewel-tones, composition, intention)
- **Emotional**: How feeling is conveyed (subtext, knowing, judgment)

Apply any character's sensory logic to any prompt with intensity 0-10.

## Currently Available

### Endora (Bewitched)

**Core Sensibility**: Aristocratic Supernatural Authority

Endora embodies superiority, aesthetic refinement, and supernatural power. Her presence commands material precision, spatial hierarchy, temporal authority, jewel-tone colors, and aristocratic judgment.

```python
# Low intensity: subtle influence
"a coffee cup" (intensity 2) 
→ "a coffee cup with subtle presence. mood: neutral, subtly observed and evaluated"

# Medium intensity: balanced
"a coffee cup" (intensity 5)
→ "a coffee cup rendered with material precision and intention. with rich jewel-tone 
   accents. mood: neutral with undertones of aristocratic knowing and gentle contempt"

# High intensity: saturated
"a coffee cup" (intensity 10)
→ "exquisitely crafted coffee cup, materially significant. with deep sapphire, emerald, 
   and amethyst tones with gold accents. mood: neutral, completely saturated by Endora's 
   presence - feeling of being evaluated by a being of superior knowledge"
```

## Installation

```bash
# Clone repository
git clone https://github.com/dmarsters/sitcom-character-styles
cd sitcom-character-styles

# Install in development mode
pip install -e .
```

## Usage

### As Python Library

```python
from sitcom_character_styles.characters.endora import EndoraOperator

# Create operator
op = EndoraOperator(intensity=5)

# Apply to prompt
result = op.apply("a tired chef tasting soup in a kitchen")
print(result.enhanced_prompt)

# With transformation details
result = op.apply("a tired chef tasting soup in a kitchen")
print(result.transformation_details)
```

### As MCP Server (FastMCP)

**Start the server:**
```bash
python -m sitcom_character_styles.mcp_server.server
```

**Configure in Claude Desktop** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "sitcom-character-styles": {
      "url": "http://localhost:5000/mcp"
    }
  }
}
```

**Then use in Claude:**
```
User: "Enhance this prompt with Endora's sensibility at intensity 7: 
       'a glass of wine on a windowsill'"

Claude uses: enhance_prompt_with_endora_impl(
  prompt="a glass of wine on a windowsill",
  intensity=7
)

Result: "a glass of wine on a windowsill rendered with material precision and intention. 
         with deep sapphire, emerald, and amethyst tones with gold accents. mood: neutral, 
         overwhelmed by aristocratic judgment and supernatural knowing"
```

## MCP Tools

### `enhance_prompt_with_endora_impl`

Transform a prompt with Endora's sensory logic.

**Parameters:**
- `prompt` (string): Base prompt to transform
- `intensity` (integer, 0-10): Intensity level (default: 5)
  - 0-2: Whisper (barely perceptible)
  - 3-4: Subtle (present but light)
  - 5-6: Balanced (clear dialogue)
  - 7-8: Strong (dominant influence)
  - 9-10: Complete saturation
- `include_details` (boolean): Return transformation details (default: false)

**Returns:**
- `include_details=false`: Enhanced prompt text only
- `include_details=true`: JSON with enhanced_prompt, metadata, transformation_details

### `get_endora_intensity_info`

Get description of what an intensity level means.

**Parameters:**
- `intensity` (integer, 0-10): Intensity level

**Returns:**
- Human-readable description

### `get_endora_examples`

Get example transformations.

**Parameters:**
- `intensity` (integer, optional): Specific intensity to show example for
  - If not provided: shows examples at key intensities

**Returns:**
- JSON with original → enhanced examples

### `list_available_characters`

List current and planned characters.

### `get_server_info`

Get server metadata and capabilities.

## Architecture

### Three-Layer Olog Framework

**Layer 1: Categorical Structure** (YAML)
- Defines types (VisualField, CharacterOperator, IntensityParameter, etc.)
- Specifies morphisms (transformations between types)
- Documents commutative diagrams (coherence guarantees)

**Layer 2: Intentionality** (YAML)
- Explains *why* transformations work through sensory principles
- Documents how all dimensions cohere under unified sensibility
- Provides intensity scaling semantics
- Lists coherence mechanisms and quality checks

**Layer 3: Execution** (Python)
- ContinuousDeformationOperator: Abstract base class
- EndoraOperator: Endora-specific implementation
- PromptParser: Extracts semantic components
- MCP server: Exposes operators as tools

### Design Philosophy

1. **Unified Operator Logic**: One sensibility, not independent rules
2. **Proportional Scaling**: All dimensions intensify together
3. **Intentionality Preservation**: Every choice serves character's worldview
4. **Coherence by Design**: Categorical structure ensures consistency
5. **Transparency**: Transformation details logged for verification
6. **Extensibility**: Base classes support adding new characters

## Planned Characters

### Mork (Mork & Mindy)

**Core Sensibility**: Alien Absurdist Sincerity

Mork embraces productive incongruity and sincere emotion despite (or because of) contradiction. His sensory logic will transform prompts through:
- Material: Unexpected combinations and clashing materials
- Spatial: Asymmetry and surprise
- Temporal: Unpredictable rhythm
- Chromatic: Surprising color adjacencies
- Emotional: Sincere emotion despite formal contradiction

## Project Structure

```
sitcom_character_styles/
├── __init__.py
├── framework/
│   ├── __init__.py
│   └── core/
│       ├── __init__.py
│       ├── categorical_structure.yaml
│       ├── intentionality.yaml
│       ├── olog_loader.py
│       └── continuous_deformation.py
├── characters/
│   ├── __init__.py
│   └── endora/
│       ├── __init__.py
│       ├── olog/
│       │   ├── categorical.yaml
│       │   └── intentionality.yaml
│       ├── src/
│       │   ├── __init__.py
│       │   ├── endora_operator.py
│       │   └── prompt_enhancement.py
│       └── tests/
│           └── test_endora.py
└── mcp_server/
    ├── __init__.py
    └── server.py
```

## Testing

```bash
# Run unit tests
pytest characters/endora/tests/

# Run specific test
pytest characters/endora/tests/test_endora.py::TestEndoraOperator::test_full_prompt_transformation

# With coverage
pytest --cov=sitcom_character_styles characters/
```

## Development

### Adding a New Character

1. **Create character directory**:
   ```
   characters/mork/
   ├── olog/
   │   ├── categorical.yaml
   │   └── intentionality.yaml
   ├── src/
   │   ├── __init__.py
   │   ├── mork_operator.py
   │   └── prompt_enhancement.py
   └── tests/
       └── test_mork.py
   ```

2. **Implement three layers**:
   - Layer 1: Define categorical structure in YAML
   - Layer 2: Define intentionality principles in YAML
   - Layer 3: Implement operator in Python

3. **Extend MCP server** (`mcp_server/server.py`):
   - Import the new character operator
   - Add tools: `enhance_prompt_with_mork_impl`, `get_mork_intensity_info`, `get_mork_examples`
   - Update `list_available_characters()`

4. **Test thoroughly**:
   - Unit tests for operator
   - Integration tests for MCP server
   - Examples demonstrating sensory logic

### Design Workflow

1. **Understand the character**: Watch clips, identify core sensibility
2. **Extract transformation dimensions**: How would this character transform materials, space, time, color, emotion?
3. **Define categorical structure**: Types and morphisms in YAML
4. **Write intentionality**: Why do these transformations cohere? What's the underlying logic?
5. **Implement operator**: Translate YAML into Python transformations
6. **Test coherence**: Verify all dimensions support unified sensibility
7. **Document examples**: Show transformations at different intensities

## Resources

- **Repository**: https://github.com/dmarsters/sitcom-character-styles
- **MCP Specification**: https://modelcontextprotocol.io/
- **FastMCP**: https://github.com/jlouis/fastmcp
- **Category Theory**: https://arxiv.org/abs/1910.01856 (Spivak's Ologs paper)

## License

MIT

## Author

Dal Marsters (dal@lushy.ai)

## Citation

If you use this project in research or publications, please cite:

```
@software{marsters2024sitcomcharacterstyles,
  title={Sitcom Character Styles: Applying Categorical Theory to Character Sensibility},
  author={Marsters, Dal},
  year={2024},
  url={https://github.com/dmarsters/sitcom-character-styles}
}
```

## Acknowledgments

This project is part of the Lushy platform for encoding domain expertise as categorical structures and executing it as composable MCP servers. Built following principles from:

- Spivak's Ontology Logs (Ologs) - categorical knowledge representation
- Natural transformations - structure-preserving mappings between domains
- Model Context Protocol - extensible AI system architecture
