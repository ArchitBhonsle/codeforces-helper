class Testcase:
    """
        * A Testcase object with inp and out attributes.
        ? Could this be a simple tuple or a NamedTuple? Probably 
    """

    def __init__(self, inp: str, out: str):
        self.inp = inp
        self.out = out
    
    def __str__(self) -> str:
        return f"Input:\n{self.inp}\nOutput:\n{self.out}"