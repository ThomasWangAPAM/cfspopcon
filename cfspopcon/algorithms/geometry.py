"""Calculate dependent geometry parameters."""
from .. import deprecated_formulas
from ..algorithm_class import Algorithm
from ..unit_handling import Unitfull


@Algorithm.register_algorithm(
    return_keys=[
        "separatrix_elongation",
        "separatrix_triangularity",
        "minor_radius",
        "vertical_minor_radius",
        "plasma_volume",
        "surface_area",
    ]
)
def calc_geometry(
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
        :term:`separatrix_elongation`, :term:`separatrix_triangularity`, :term:`minor_radius`, :term:`vertical_minor_radius`, :term:`plasma_volume`, :term:`surface_area`
    """
    separatrix_elongation = areal_elongation * elongation_ratio_sep_to_areal

    separatrix_triangularity = triangularity_psi95 * triangularity_ratio_sep_to_psi95

    minor_radius = major_radius * inverse_aspect_ratio
    vertical_minor_radius = minor_radius * separatrix_elongation

    plasma_volume = deprecated_formulas.calc_plasma_volume(major_radius, inverse_aspect_ratio, areal_elongation)
    surface_area = deprecated_formulas.calc_plasma_surface_area(major_radius, inverse_aspect_ratio, areal_elongation)

    return (separatrix_elongation, separatrix_triangularity, minor_radius, vertical_minor_radius, plasma_volume, surface_area)
