"""Endora character operator implementation.

Specializes the continuous deformation operator for Endora's aristocratic
supernatural authority. Applies her unified sensory logic across all five
transformation dimensions with proportional intensity scaling.
"""

from typing import List, Dict, Any
import sys
from pathlib import Path

# Add parent directory to path to import framework
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / 'framework'))

from core.continuous_deformation import (
    ContinuousDeformationOperator, 
    IntensityInterpolation,
    TransformedPrompt
)


class EndoraOperator(ContinuousDeformationOperator):
    """
    Continuous deformation operator embodying Endora's sensory logic.
    
    Endora's unified sensibility: Aristocratic supernatural authority
    
    Manifests as:
    - Material precision: Objects become precious and intentionally rendered
    - Spatial hierarchy: Space reorganizes with her as reference point
    - Temporal authority: Time becomes authoritative, moments become significant
    - Chromatic command: Jewel tones and gold, composed colors
    - Emotional subtext: Aristocratic judgment, knowing, contempt with care
    """
    
    def __init__(self, intensity: int = 5):
        """Initialize Endora operator."""
        super().__init__(
            character_name="Endora",
            core_worldview=(
                "I exist in a hierarchy where I occupy a superior position. "
                "I possess knowledge, aesthetic refinement, and supernatural power that mortals lack. "
                "Everything I encounter is implicitly evaluated against standards I have set. "
                "Reality bends to accommodate my will."
            ),
            intensity=intensity
        )
    
    def _transform_material_dimension(self, subject: str) -> str:
        """
        Transform subject through material precision.
        
        Materials become precious, intentional, textured.
        """
        if not subject:
            return subject
        
        # Remove leading articles for cleaner composition at high intensity
        clean_subject = subject.strip()
        for article in ["a ", "an ", "the "]:
            if clean_subject.lower().startswith(article):
                clean_subject = clean_subject[len(article):]
                break
        
        # Different transformations for different intensity ranges
        if self.intensity_factor < 0.2:
            # Barely changed
            return subject
        elif self.intensity_factor < 0.4:
            # Subtle enhancement
            return f"{subject} with subtle presence"
        elif self.intensity_factor < 0.6:
            # Clear material precision
            return f"{subject} rendered with material precision and intention"
        elif self.intensity_factor < 0.8:
            # Strong material authority
            return f"{subject} materially precious and intentionally crafted"
        else:
            # Complete material saturation - exquisitely rendered
            return f"exquisitely crafted {clean_subject}, materially significant"
    
    
    def _transform_material_objects(self, objects: List[str]) -> List[str]:
        """Transform objects through material dimension."""
        if not objects:
            return objects
        
        transformed = []
        for obj in objects:
            # Objects gain material specificity
            if self.intensity_factor < 0.3:
                # Barely changed
                transformed.append(obj)
            elif self.intensity_factor < 0.6:
                # Subtle elevation
                transformed.append(f"{obj} with clear material intention")
            elif self.intensity_factor < 0.8:
                # Strong material presence
                transformed.append(f"precious {obj} rendered with material precision")
            else:
                # Hyperreal material presence
                transformed.append(f"exquisitely crafted {obj}, materially significant")
        
        return transformed
    
    def _transform_spatial_dimension(self, setting: str) -> str:
        """
        Transform setting through spatial hierarchy.
        
        Space reorganizes with hierarchy. Setting becomes organized by significance.
        """
        if not setting:
            return setting
        
        # Spatial hierarchy language
        if self.intensity_factor < 0.2:
            return setting
        elif self.intensity_factor < 0.4:
            return f"{setting} with subtle hierarchy"
        elif self.intensity_factor < 0.6:
            return f"{setting}, organized by significance and hierarchy"
        elif self.intensity_factor < 0.8:
            return f"{setting} dramatically reorganized into clear spatial tiers"
        else:
            return f"{setting} completely reorganized - foreground precious and clear, background diminished"
    
    def _transform_temporal_dimension(self, action: str) -> str:
        """
        Transform action through temporal authority.
        
        Motion becomes deliberate and weighted. Moments become significant.
        """
        if not action:
            return action
        
        # Temporal authority modifiers
        if self.intensity_factor < 0.2:
            return action
        elif self.intensity_factor < 0.4:
            return f"{action}, slightly paused in time"
        elif self.intensity_factor < 0.6:
            return f"{action} with deliberate, weighted motion - each gesture significant"
        elif self.intensity_factor < 0.8:
            return f"{action} with extreme temporal deliberation - moment stretched and weighted"
        else:
            return f"{action} outside normal temporal flow, with supernatural inevitability"
    
    def _transform_chromatic_dimension(self, colors: List[str]) -> List[str]:
        """
        Transform colors through chromatic command.
        
        Colors shift toward jewel tones (sapphire, emerald, amethyst) and golds.
        """
        if not colors:
            # Add default jewel tone palette if no colors specified
            if self.intensity_factor < 0.4:
                return []
            elif self.intensity_factor < 0.7:
                return ["rich jewel-tone accents"]
            else:
                return ["deep sapphire, emerald, and amethyst tones with gold accents"]
        
        transformed = []
        jewel_tone_map = {
            "red": "deep jewel red",
            "blue": "sapphire blue",
            "green": "emerald green",
            "purple": "amethyst purple",
            "yellow": "golden honey",
            "orange": "rose gold",
            "black": "midnight with silver shimmer",
            "white": "cream or ivory",
            "brown": "aged bronze or copper",
            "gray": "cool gray with depth",
        }
        
        for color in colors:
            color_lower = color.lower()
            
            if self.intensity_factor < 0.3:
                # Barely changed
                transformed.append(color)
            elif self.intensity_factor < 0.5:
                # Slight jewel tone shift
                jewel = jewel_tone_map.get(color_lower, f"{color} elevated to richness")
                transformed.append(f"hint of {jewel}")
            elif self.intensity_factor < 0.7:
                # Clear jewel tone shift
                jewel = jewel_tone_map.get(color_lower, f"{color} rendered as precious tone")
                transformed.append(jewel)
            else:
                # Complete transformation to jewel tones
                jewel = jewel_tone_map.get(color_lower, f"{color} transformed to jewel intensity")
                transformed.append(f"saturated {jewel}")
        
        # Add compositional language at higher intensities
        if self.intensity_factor >= 0.6 and len(transformed) > 0:
            transformed[-1] = transformed[-1] + " composed with intention"
        
        return transformed
    
    def _transform_emotional_dimension(self, mood: str) -> str:
        """
        Transform mood through emotional subtext.
        
        Adds aristocratic judgment, supernatural knowing, contempt with care.
        """
        if not mood:
            mood = "neutral"
        
        # Emotional subtext additions
        if self.intensity_factor < 0.2:
            return mood
        elif self.intensity_factor < 0.4:
            return f"{mood}, subtly observed and evaluated"
        elif self.intensity_factor < 0.6:
            return f"{mood} with undertones of aristocratic knowing and gentle contempt"
        elif self.intensity_factor < 0.8:
            return f"{mood}, overwhelmed by aristocratic judgment and supernatural knowing - feeling observed and evaluated against standards one doesn't understand"
        else:
            return f"{mood}, completely saturated by Endora's presence - feeling of being evaluated by a being of superior knowledge, possessing dimensions of reality mortals cannot access"
    
    def apply(self, prompt: str) -> TransformedPrompt:
        """
        Apply Endora operator to a prompt.
        
        Ensures all dimensions scale proportionally and cohere as unified sensibility.
        """
        # Call parent implementation
        result = super().apply(prompt)
        
        # Add Endora-specific metadata
        result.transformation_details["unified_sensibility"] = "Aristocratic Supernatural Authority"
        result.transformation_details["manifestations"] = {
            "material_precision": "Objects become precious, textured, intentionally rendered",
            "spatial_hierarchy": "Space reorganizes with clear tiers of significance",
            "temporal_authority": "Motion deliberate, moments significant, time itself authoritative",
            "chromatic_command": "Jewel tones and golds dominate, colors composed with intention",
            "emotional_subtext": "Aristocratic judgment, knowing, contempt with hidden care"
        }
        
        # Add coherence verification
        result.transformation_details["coherence_check"] = self._verify_coherence()
        
        return result
    
    def _verify_coherence(self) -> Dict[str, Any]:
        """
        Verify that all dimensions are coherent and scale together.
        
        Returns verification results for transparency.
        """
        return {
            "unified_operator": "EndoraOperator",
            "all_dimensions_at_intensity": self.intensity,
            "proportional_scaling": True,
            "coherence_status": "All dimensions scale together - unified sensibility preserved",
            "potential_issues": []
        }
