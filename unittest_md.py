import sys, unittest
from hdmolecule import calcenergy

class MdTests(unittest.TestCase):
    def test_calcenergy(self):
        from ase.lattice.cubic import FaceCenteredCubic
        from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
        from ase import units

        from asap3 import EMT
        size = 10
        
        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol="Cu",
                          size=(size, size, size),
                          pbc=True)
                          
        atoms.calc = EMT()
        
        epot, ekin = calcenergy(atoms)
        
        if(ekin<0):
            self.assertTrue(False)
        else:
            self.assertTrue(True)
            
if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
