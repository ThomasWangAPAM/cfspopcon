"""Plasma geometry (inside the last-closed-flux-surface)."""
import numpy as np

from ...algorithm_class import Algorithm
from ...unit_handling import Unitfull


@Algorithm.register_algorithm(return_keys=["plasma_volume"])
def calc_plasma_volume(major_radius: Unitfull, inverse_aspect_ratio: Unitfull, areal_elongation: Unitfull) -> Unitfull:
    """Calculate the plasma volume inside the last-closed-flux-surface.

    Args:
        major_radius: [m] :term:`glossary link<major_radius>`
        inverse_aspect_ratio: [~] :term:`glossary link<inverse_aspect_ratio>`
        areal_elongation: [~] :term:`glossary link<areal_elongation>`

    Returns:
        :term:`plasma_volume` [m^3]
    """
    return (
        2.0
        * np.pi
        * major_radius**3.0
        * inverse_aspect_ratio**2.0
        * areal_elongation
        * (np.pi - (np.pi - 8.0 / 3.0) * inverse_aspect_ratio)
    )

@Algorithm.register_algorithm(return_keys=["surface_area"])
def calc_plasma_surface_area(major_radius: Unitfull, inverse_aspect_ratio: Unitfull, areal_elongation: Unitfull) -> Unitfull:
    """Calculate the plasma surface area inside the last-closed-flux-surface.

    Args:
        major_radius: [m] :term:`glossary link<major_radius>`
        inverse_aspect_ratio: [~] :term:`glossary link<inverse_aspect_ratio>`
        areal_elongation: [~] :term:`glossary link<areal_elongation>`

    Returns:
        :term:`surface_area` [m^2]
    """
    return (
        2.0 * np.pi * (major_radius**2.0) * inverse_aspect_ratio * areal_elongation * (np.pi + 2.0 - (np.pi - 2.0) * inverse_aspect_ratio)
    )

@Algorithm.register_algorithm(
    return_keys=[
        "separatrix_elongation",
        "separatrix_triangularity",
        "minor_radius",
        "vertical_minor_radius",
    ]
)
def calc_geometry_from_ratios(
    major_radius: Unitfull,
    inverse_aspect_ratio: Unitfull,
    areal_elongation: Unitfull,
    triangularity_psi95: Unitfull,
    elongation_ratio_sep_to_areal: Unitfull,
    triangularity_ratio_sep_to_psi95: Unitfull,
) -> tuple[Unitfull, ...]:
    """Calculate dependent geometry parameters.

    Args:
        major_radius: :term:`glossary link<major_radius>`
        inverse_aspect_ratio: :term:`glossary link<inverse_aspect_ratio>`
        areal_elongation: :term:`glossary link<areal_elongation>`
        triangularity_psi95: :term:`glossary link<triangularity_psi95>`
        elongation_ratio_sep_to_areal: :term:`glossary link<elongation_ratio_sep_to_areal>`
        triangularity_ratio_sep_to_psi95: :term:`glossary link<triangularity_ratio_sep_to_psi95>`

    Returns:
        :term:`separatrix_elongation`, :term:`separatrix_triangularity`, :term:`minor_radius`, :term:`vertical_minor_radius`
    """
    separatrix_elongation = areal_elongation * elongation_ratio_sep_to_areal

    separatrix_triangularity = triangularity_psi95 * triangularity_ratio_sep_to_psi95

    minor_radius = major_radius * inverse_aspect_ratio
    vertical_minor_radius = minor_radius * separatrix_elongation

    return (separatrix_elongation, separatrix_triangularity, minor_radius, vertical_minor_radius)

