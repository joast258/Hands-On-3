#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2021 MDMolecule developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
This module defines the HDMolecule class closely inspired by one
of the ASE example at: https://wiki.fysik.dtu.dk/ase/tutorials/atomization.html

It also provides a couple of example functions to show how to use this class.
"""

from ase import Atoms
from ase.calculators.emt import EMT


class HDMolecule:
    """A HDMolecule represents a homonuclear diatomic molecule, i.e., a
    linear molecule that consists of two atoms of the same element.

    A homonuclear diatomic molecule is fully defined by the element and distance
    between the two atoms.

    The class provides a number of methods to calculate various energy
    expressions for this type of molecule using the ASE EMT energy calculator.
    """

    def __init__(self, element_symbol, distance):
        """Create a HDMolecule

        Args:
            element_symbol (string): The chemical element symbol for the element
                that the molecule consists of.
            distance (float): The distance between the two atoms.
        """
        self.atom = Atoms(element_symbol)
        self.molecule = Atoms(
            "2" + element_symbol, [(0.0, 0.0, 0.0), (0.0, 0.0, distance)]
        )

    def atom_energy(self):
        """Calculate the energy of one separated atom of the element the
        homonuclear diatomic molecule consists of using the ASE EMT energy
        calculator.

        Returns:
            float: the energy of the atom in eV
        """
        self.atom.calc = EMT()
        return self.atom.get_potential_energy()

    def molecule_energy(self):
        """Calculate the energy of the homonuclear diatomic molecule using
        the ASE EMT energy calculator.

        Returns:
            float: the energy of the molecule in eV
        """
        self.molecule.calc = EMT()
        return self.molecule.get_potential_energy()

    def atomization_energy(self):
        """Calculate the atomization energy of the homonuclear diatomic
        molecule using the ASE EMT energy calculator.

        The atomization energy is the energy it takes to break apart a
        molecule into separate atoms. It is calculated as: the energy
        of the individual atoms - the energy of the molecule.

        Returns:
            float: the atomization energy of the molecule in eV
        """

        e_atom = self.atom_energy()
        e_molecule = self.molecule_energy()

        return (2 * e_atom) - e_molecule


def analyze_N2(distance):
    """
    Skriva kommentar är najs, inte skriva kommentar är bajs
    """


    N2 = HDMolecule("N", distance)

    print("Nitrogen atom energy: %5.2f eV" % N2.atom_energy())
    print("Nitrogen molecule energy: %5.2f eV" % N2.molecule_energy())
    print("Atomization energy: %5.2f eV" % N2.atomization_energy())


def analyze_exp_N2():
    """Print out an energy analysis an N2 molecule with a
    bond length of 1.1 Å as found in experiments.
    """
    exp_bond_length = 1.1

    analyze_N2(exp_bond_length)
