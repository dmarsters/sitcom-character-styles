"""Sitcom Character Styles - Transform prompts with character sensory logic.

A framework for encoding domain expertise (character sensibilities) as categorical
structures and executing them as MCP servers.

Core concept: Characters embody unified sensory logics that can be applied to any
visual field with varying intensity. Endora's aristocratic supernatural authority,
Mork's alien absurdist sincerity, etc.

Layers:
  1. Categorical: Types, morphisms, commutative diagrams (YAML ologs)
  2. Intentionality: Sensory principles and coherence mechanisms (YAML ologs)
  3. Execution: Python operators and MCP server

Usage:
  # Direct operator
  from sitcom_character_styles.characters.endora import EndoraOperator
  op = EndoraOperator(intensity=5)
  result = op.apply("a coffee cup")
  
  # MCP server (FastMCP)
  python -m sitcom_character_styles.mcp_server.server

Repository: https://github.com/dmarsters/sitcom-character-styles
"""

__version__ = "1.0.0"
__author__ = "Dal Marsters"
__license__ = "MIT"

from . import framework
from .characters import endora

__all__ = ["framework", "endora", "__version__"]
