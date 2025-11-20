"""OlogLoader for sitcom character styles framework.

Loads and parses YAML olog specifications (categorical structure and intentionality).
Provides typed access to character operators and their transformation dimensions.
"""

import yaml
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Dict, Any, List


@dataclass
class TransformationDimension:
    """Represents one dimension of character transformation."""
    name: str
    description: str
    properties: Dict[str, Any]
    intensification_curve: Dict[int, str]
    coherence_mechanism: str
    example: str

    @classmethod
    def from_dict(cls, name: str, data: Dict[str, Any]) -> "TransformationDimension":
        """Create from YAML dictionary."""
        return cls(
            name=name,
            description=data.get("description", ""),
            properties=data.get("properties", {}),
            intensification_curve={
                int(k.split("_")[2]): v 
                for k, v in data.get("intensification_curve", "").split("\n")
                if "intensity" in k
            },
            coherence_mechanism=data.get("coherence_mechanism", ""),
            example=data.get("example", "")
        )


@dataclass
class CharacterOperator:
    """Represents a character's unified sensory logic as a continuous deformation operator."""
    name: str
    core_worldview: str
    unified_sensory_logic: str
    transformation_dimensions: Dict[str, TransformationDimension]
    intensity_parameter: Dict[str, Any]
    unified_operator_coherence: Dict[str, str]
    intensity_progression: Dict[int, str]
    failure_modes: Dict[str, Dict[str, str]]
    quality_checks: Dict[str, Dict[str, str]]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CharacterOperator":
        """Create from YAML dictionary."""
        # Parse transformation dimensions
        dimensions = {}
        for dim_name, dim_data in data.get("transformation_dimensions", {}).items():
            dimensions[dim_name] = TransformationDimension.from_dict(dim_name, dim_data)
        
        return cls(
            name=data.get("character_name", "Unknown"),
            core_worldview=data.get("core_worldview", ""),
            unified_sensory_logic=data.get("unified_sensory_logic", ""),
            transformation_dimensions=dimensions,
            intensity_parameter=data.get("intensity_parameter", {}),
            unified_operator_coherence=data.get("unified_operator_coherence", {}),
            intensity_progression=data.get("intensity_progression", {}),
            failure_modes=data.get("failure_modes_to_avoid", {}),
            quality_checks=data.get("quality_checks_for_endora", {})
        )


@dataclass
class FrameworkIntentionality:
    """Framework-level sensory principles."""
    core_principle: str
    sensory_principles: Dict[str, Dict[str, str]]
    intensity_semantics: Dict[str, str]
    coherence_mechanisms: Dict[str, Dict[str, str]]
    application_guidelines: Dict[str, str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FrameworkIntentionality":
        """Create from YAML dictionary."""
        return cls(
            core_principle=data.get("core_principle", ""),
            sensory_principles=data.get("framework_sensory_principles", {}),
            intensity_semantics=data.get("intensity_semantics", {}),
            coherence_mechanisms=data.get("coherence_mechanisms", {}),
            application_guidelines=data.get("application_guidelines", {})
        )


class OlogLoader:
    """Loads and provides access to olog specifications."""
    
    def __init__(self, framework_olog_path: str, character_olog_path: str, 
                 character_intentionality_path: str, framework_intentionality_path: str):
        """
        Initialize loader with paths to olog files.
        
        Args:
            framework_olog_path: Path to framework categorical structure YAML
            character_olog_path: Path to character-specific categorical structure YAML
            character_intentionality_path: Path to character intentionality YAML
            framework_intentionality_path: Path to framework intentionality YAML
        """
        self.framework_olog_path = Path(framework_olog_path)
        self.character_olog_path = Path(character_olog_path)
        self.character_intentionality_path = Path(character_intentionality_path)
        self.framework_intentionality_path = Path(framework_intentionality_path)
        
        # Load all ologs
        self._framework_categorical = self._load_yaml(self.framework_olog_path)
        self._character_categorical = self._load_yaml(self.character_olog_path)
        self._character_intentionality = self._load_yaml(self.character_intentionality_path)
        self._framework_intentionality = self._load_yaml(self.framework_intentionality_path)
        
        # Parse into typed structures
        self.framework_intentionality = FrameworkIntentionality.from_dict(
            self._framework_intentionality
        )
        self.character_operator = CharacterOperator.from_dict(
            self._character_intentionality
        )

    @staticmethod
    def _load_yaml(path: Path) -> Dict[str, Any]:
        """Load YAML file and return as dictionary."""
        if not path.exists():
            raise FileNotFoundError(f"Olog file not found: {path}")
        
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        
        if data is None:
            raise ValueError(f"Empty YAML file: {path}")
        
        return data

    def get_framework_categorical(self) -> Dict[str, Any]:
        """Get raw framework categorical structure."""
        return self._framework_categorical

    def get_character_categorical(self) -> Dict[str, Any]:
        """Get raw character categorical structure."""
        return self._character_categorical

    def get_character_intentionality(self) -> Dict[str, Any]:
        """Get raw character intentionality specification."""
        return self._character_intentionality

    def get_framework_intentionality(self) -> FrameworkIntentionality:
        """Get parsed framework intentionality."""
        return self.framework_intentionality

    def get_character_operator(self) -> CharacterOperator:
        """Get parsed character operator."""
        return self.character_operator

    def get_intensity_progression(self, intensity: int) -> str:
        """Get description of what happens at a specific intensity."""
        if intensity < 0 or intensity > 10:
            raise ValueError(f"Intensity must be 0-10, got {intensity}")
        
        progression = self.character_operator.intensity_progression
        return progression.get(intensity, "")

    def get_transformation_dimension(self, dimension_name: str) -> Optional[TransformationDimension]:
        """Get a specific transformation dimension."""
        return self.character_operator.transformation_dimensions.get(dimension_name)

    def validate_coherence(self) -> List[str]:
        """Validate that ologs are coherent. Returns list of issues found."""
        issues = []
        
        # Check that all transformation dimensions are defined in both categorical and intentionality
        dim_names_categorical = set(self._character_categorical.get("transformation_dimensions", {}).keys())
        dim_names_intentionality = set(self.character_operator.transformation_dimensions.keys())
        
        missing_in_intentionality = dim_names_categorical - dim_names_intentionality
        if missing_in_intentionality:
            issues.append(f"Transformation dimensions missing in intentionality: {missing_in_intentionality}")
        
        extra_in_intentionality = dim_names_intentionality - dim_names_categorical
        if extra_in_intentionality:
            issues.append(f"Extra transformation dimensions in intentionality: {extra_in_intentionality}")
        
        # Check intensity parameter range
        intensity_data = self.character_operator.intensity_parameter
        if not (0 <= intensity_data.get("default", 5) <= 10):
            issues.append(f"Default intensity out of range: {intensity_data.get('default')}")
        
        # Check that all transformation dimensions have intensity progression
        for dim_name, dimension in self.character_operator.transformation_dimensions.items():
            if not dimension.intensification_curve:
                issues.append(f"Missing intensification curve for dimension: {dim_name}")
        
        return issues


def load_endora_ologs(ologs_dir: str = "characters/endora/olog") -> OlogLoader:
    """Convenience function to load Endora ologs from standard location."""
    return OlogLoader(
        framework_olog_path=f"{ologs_dir}/../../../framework/core/categorical_structure.yaml",
        character_olog_path=f"{ologs_dir}/categorical.yaml",
        character_intentionality_path=f"{ologs_dir}/intentionality.yaml",
        framework_intentionality_path=f"{ologs_dir}/../../../framework/core/intentionality.yaml"
    )
