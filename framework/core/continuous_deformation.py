"""Continuous deformation operator for character sensory logic.

Implements unified character operators that continuously transform visual fields
with intensity parameter 0-10. Each operator preserves coherence across all 
transformation dimensions by applying a single unified sensibility.
"""

from dataclasses import dataclass
from typing import Dict, List, Any
from enum import Enum
import re


class TransformationDimension(Enum):
    """The five dimensions of character transformation."""
    MATERIAL = "material"
    SPATIAL = "spatial"
    TEMPORAL = "temporal"
    CHROMATIC = "chromatic"
    EMOTIONAL = "emotional"


@dataclass
class ParsedPrompt:
    """Semantic components extracted from a prompt."""
    base_prompt: str
    subject: str
    action: str
    setting: str
    objects: List[str]
    colors: List[str]
    mood: str
    other_details: str


@dataclass
class TransformedPrompt:
    """Result of applying character operator to a prompt."""
    enhanced_prompt: str
    transformation_details: Dict[str, Any]
    intensity_applied: int


class PromptParser:
    """Parses natural language prompts into semantic components."""
    
    @staticmethod
    def parse(prompt: str) -> ParsedPrompt:
        """
        Parse a prompt into semantic components.
        
        This is a simplified parser. In production, this could use NLP.
        """
        # Extract basic components using heuristics
        subject = PromptParser._extract_subject(prompt)
        action = PromptParser._extract_action(prompt)
        setting = PromptParser._extract_setting(prompt)
        objects = PromptParser._extract_objects(prompt)
        colors = PromptParser._extract_colors(prompt)
        mood = PromptParser._extract_mood(prompt)
        
        other_details = prompt
        for word in [subject, action, setting] + objects + colors + [mood]:
            if word:
                other_details = other_details.replace(word, "", 1)
        other_details = other_details.strip()
        
        return ParsedPrompt(
            base_prompt=prompt,
            subject=subject,
            action=action,
            setting=setting,
            objects=objects,
            colors=colors,
            mood=mood,
            other_details=other_details
        )
    
    @staticmethod
    def _extract_subject(prompt: str) -> str:
        """Extract the main subject (person/object being depicted)."""
        # Look for common patterns
        patterns = [
            r"(?:a|an|the)\s+([a-z\s]+?)(?:\s+(?:in|on|at|with|wearing|holding))",
            r"^([a-z\s]+?)(?:\s+(?:in|on|at|with|wearing|holding|is|are))",
        ]
        for pattern in patterns:
            match = re.search(pattern, prompt.lower())
            if match:
                return match.group(1).strip()
        
        # Fallback: first few words before a preposition or punctuation
        words = prompt.split()
        # Include articles and adjectives
        subject_words = []
        for word in words:
            # Stop at prepositions
            if word.lower() in ['in', 'on', 'at', 'with', 'wearing', 'holding', 'near', 'by', 'under', 'above']:
                break
            subject_words.append(word)
        
        return " ".join(subject_words[:min(4, len(subject_words))])
    
    @staticmethod
    def _extract_action(prompt: str) -> str:
        """Extract the main action/verb."""
        verbs = [
            "walking", "running", "standing", "sitting", "eating", "drinking",
            "looking", "holding", "wearing", "riding", "driving", "cooking",
            "reading", "writing", "talking", "singing", "dancing", "playing",
            "tasting", "smelling", "touching", "building", "creating"
        ]
        
        prompt_lower = prompt.lower()
        for verb in verbs:
            if verb in prompt_lower:
                # Find context around verb
                idx = prompt_lower.find(verb)
                start = max(0, idx - 10)
                end = min(len(prompt), idx + len(verb) + 20)
                return prompt[start:end].strip()
        
        return ""
    
    @staticmethod
    def _extract_setting(prompt: str) -> str:
        """Extract the location/setting."""
        settings = [
            "kitchen", "bedroom", "living room", "office", "street", "park",
            "forest", "beach", "mountain", "city", "village", "house", "building",
            "room", "garden", "library", "cafe", "restaurant", "bar", "stage"
        ]
        
        prompt_lower = prompt.lower()
        for setting in settings:
            if setting in prompt_lower:
                return setting
        
        return ""
    
    @staticmethod
    def _extract_objects(prompt: str) -> List[str]:
        """Extract notable objects mentioned (excluding those already in subject)."""
        objects = []
        object_keywords = [
            "cup", "bottle", "glass", "table", "chair", "book",
            "flower", "plant", "lamp", "window", "door", "painting", "mirror",
            "knife", "fork", "plate", "bowl", "pot", "pan", "mug"
        ]
        
        prompt_lower = prompt.lower()
        # Common compound noun adjectives that shouldn't be double-counted
        adjective_nouns = ["coffee", "soup", "wine", "water", "tea", "beer", "milk"]
        
        for obj in object_keywords:
            if obj in prompt_lower:
                # Don't add if it's part of a compound noun (preceded by adjective)
                skip = False
                for adj in adjective_nouns:
                    if f"{adj} {obj}" in prompt_lower:
                        skip = True
                        break
                
                if not skip:
                    objects.append(obj)
        
        return objects
    
    @staticmethod
    def _extract_colors(prompt: str) -> List[str]:
        """Extract color mentions."""
        colors = [
            "red", "blue", "green", "yellow", "orange", "purple", "pink",
            "black", "white", "gray", "grey", "brown", "gold", "silver",
            "sapphire", "emerald", "amethyst", "ruby", "jade", "bronze"
        ]
        
        prompt_lower = prompt.lower()
        found_colors = []
        for color in colors:
            if color in prompt_lower:
                found_colors.append(color)
        
        return found_colors
    
    @staticmethod
    def _extract_mood(prompt: str) -> str:
        """Extract mood/emotional tone."""
        moods = [
            "happy", "sad", "angry", "peaceful", "tense", "cheerful", "somber",
            "playful", "serious", "warm", "cold", "inviting", "mysterious",
            "anxious", "calm", "chaotic", "orderly", "bright", "dark"
        ]
        
        prompt_lower = prompt.lower()
        for mood in moods:
            if mood in prompt_lower:
                return mood
        
        return "neutral"


class ContinuousDeformationOperator:
    """
    Base class for character-based continuous deformation operators.
    
    Applies a unified character sensory logic to visual fields with intensity 0-10.
    All transformation dimensions scale proportionally with intensity to maintain coherence.
    """
    
    def __init__(self, character_name: str, core_worldview: str, intensity: int = 5):
        """
        Initialize the operator.
        
        Args:
            character_name: Name of the character
            core_worldview: The character's underlying philosophy
            intensity: Application intensity (0-10)
        """
        self.character_name = character_name
        self.core_worldview = core_worldview
        self.intensity = self._validate_intensity(intensity)
        self.intensity_factor = self.intensity / 10.0  # Convert to 0-1 range for calculations
    
    @staticmethod
    def _validate_intensity(intensity: int) -> int:
        """Validate and constrain intensity to 0-10."""
        if not isinstance(intensity, int):
            raise TypeError(f"Intensity must be int, got {type(intensity)}")
        
        if intensity < 0:
            return 0
        elif intensity > 10:
            return 10
        else:
            return intensity
    
    def apply(self, prompt: str) -> TransformedPrompt:
        """
        Apply character operator to a prompt.
        
        Args:
            prompt: The prompt to transform
        
        Returns:
            TransformedPrompt with enhanced prompt and transformation details
        """
        # Parse prompt into semantic components
        parsed = PromptParser.parse(prompt)
        
        # Apply transformations to each dimension
        transformed_subject = self._transform_material_dimension(parsed.subject)
        transformed_action = self._transform_temporal_dimension(parsed.action)
        transformed_setting = self._transform_spatial_dimension(parsed.setting)
        transformed_objects = self._transform_material_objects(parsed.objects)
        transformed_colors = self._transform_chromatic_dimension(parsed.colors)
        transformed_mood = self._transform_emotional_dimension(parsed.mood)
        
        # Reconstruct enhanced prompt
        enhanced_parts = []
        
        if transformed_subject:
            enhanced_parts.append(transformed_subject)
        
        if transformed_action:
            enhanced_parts.append(transformed_action)
        
        if transformed_setting:
            enhanced_parts.append(f"in {transformed_setting}")
        
        if transformed_objects:
            enhanced_parts.append(", ".join(transformed_objects))
        
        if transformed_colors:
            enhanced_parts.append(f"with {', '.join(transformed_colors)}")
        
        if transformed_mood:
            enhanced_parts.append(f"mood: {transformed_mood}")
        
        if parsed.other_details:
            enhanced_parts.append(parsed.other_details)
        
        enhanced_prompt = ". ".join(filter(None, enhanced_parts))
        
        # Compile transformation details for transparency
        transformation_details = {
            "character": self.character_name,
            "intensity": self.intensity,
            "intensity_factor": self.intensity_factor,
            "original_components": {
                "subject": parsed.subject,
                "action": parsed.action,
                "setting": parsed.setting,
                "objects": parsed.objects,
                "colors": parsed.colors,
                "mood": parsed.mood,
            },
            "transformed_components": {
                "subject": transformed_subject,
                "action": transformed_action,
                "setting": transformed_setting,
                "objects": transformed_objects,
                "colors": transformed_colors,
                "mood": transformed_mood,
            },
            "dimensions_applied": [
                TransformationDimension.MATERIAL.value,
                TransformationDimension.SPATIAL.value,
                TransformationDimension.TEMPORAL.value,
                TransformationDimension.CHROMATIC.value,
                TransformationDimension.EMOTIONAL.value,
            ]
        }
        
        return TransformedPrompt(
            enhanced_prompt=enhanced_prompt,
            transformation_details=transformation_details,
            intensity_applied=self.intensity
        )
    
    # Transformation methods - to be overridden by subclasses
    
    def _transform_material_dimension(self, subject: str) -> str:
        """Transform subject through material dimension."""
        raise NotImplementedError
    
    def _transform_material_objects(self, objects: List[str]) -> List[str]:
        """Transform objects through material dimension."""
        raise NotImplementedError
    
    def _transform_spatial_dimension(self, setting: str) -> str:
        """Transform setting through spatial dimension."""
        raise NotImplementedError
    
    def _transform_temporal_dimension(self, action: str) -> str:
        """Transform action through temporal dimension."""
        raise NotImplementedError
    
    def _transform_chromatic_dimension(self, colors: List[str]) -> List[str]:
        """Transform colors through chromatic dimension."""
        raise NotImplementedError
    
    def _transform_emotional_dimension(self, mood: str) -> str:
        """Transform mood through emotional dimension."""
        raise NotImplementedError


class IntensityInterpolation:
    """Utilities for interpolating values across intensity ranges."""
    
    @staticmethod
    def lerp(intensity_factor: float, min_val: str, mid_val: str, max_val: str) -> str:
        """
        Linear interpolation between three values based on intensity factor (0-1).
        
        intensity_factor 0.0 → returns min_val
        intensity_factor 0.5 → returns mid_val
        intensity_factor 1.0 → returns max_val
        """
        if intensity_factor < 0.5:
            # Interpolate between min and mid
            t = intensity_factor * 2  # Scale to 0-1
            return min_val if t < 0.5 else mid_val
        else:
            # Interpolate between mid and max
            t = (intensity_factor - 0.5) * 2  # Scale to 0-1
            return mid_val if t < 0.5 else max_val
    
    @staticmethod
    def apply_intensity_modifier(text: str, intensity_factor: float, 
                                 modifiers: Dict[str, str]) -> str:
        """
        Apply intensity-dependent modifiers to text.
        
        Args:
            text: Original text
            intensity_factor: Intensity as 0-1
            modifiers: Dict with keys "low", "medium", "high" for intensity ranges
        
        Returns:
            Modified text appropriate for intensity level
        """
        if intensity_factor < 0.33:
            return text + modifiers.get("low", "")
        elif intensity_factor < 0.66:
            return text + modifiers.get("medium", "")
        else:
            return text + modifiers.get("high", "")
